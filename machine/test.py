import argparse
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random
from models.experimental import attempt_load
from utils.datasets import LoadStreams
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh, set_logging
from utils.plots import plot_one_box
from utils.torch_utils import select_device, time_synchronized
import pygame

# Initialize pygame
pygame.mixer.init()

# Load audio files
correct_sound = pygame.mixer.Sound('/home/ezio/PycharmProjects/squretest/按壓位置正確.mp3')  # Replace with your correct sound file
incorrect_sound = pygame.mixer.Sound('/home/ezio/PycharmProjects/squretest/按壓位置不正確.mp3')  # Replace with your incorrect sound file

# 计算两个边界框之间的水平距离
def calculate_distance(box1, box2):
    x1_min, y1_min, x1_max, y1_max = box1
    x2_min, y2_min, x2_max, y2_max = box2
    x1_center = (x1_min + x1_max) / 2
    x2_center = (x2_min + x2_max) / 2
    distance = abs(x1_center - x2_center)
    return distance

def detect():
    source, weights, imgsz = str(opt.source), opt.weights, opt.img_size
    webcam = source.isnumeric() or source.startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Initialize
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size

    if half:
        model.half()  # to FP16

    # Set Dataloader
    cudnn.benchmark = True  # set True to speed up constant image size inference
    dataset = LoadStreams(source, img_size=imgsz)

    # Get names and colors
    names = model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Initialize the timer
    last_sound_time = time.time()

    # Run inference
    t0 = time.time()
    for path, img, im0s, _ in dataset:
        if im0s is None or len(im0s) == 0:
            continue  # Skip empty frames

        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = time_synchronized()

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            p, s, im0, _ = path, '', im0s[0], dataset.count

            p = Path(p[0])  # to Path
            save_path = str(p.name)  # img.jpg

            if len(det):
                # Convert det to a PyTorch tensor
                det = torch.tensor(det)

                # Rescale boxes from img_size to im0 size
                im0_shape = im0.shape if isinstance(im0, torch.Tensor) else im0.shape[:2]  # 获取当前图像的形状
                det[:, :4] = scale_coords(im0_shape, det[:, :4], im0_shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Draw distance between boxes
                if len(det) >= 2:
                    box1, box2 = det[:2, :4].cpu().numpy()  # Get the first two boxes
                    distance = calculate_distance(box1, box2)
                    s += f"Distance: {distance:.2f}px"

                    # Determine if the distance is correct or not
                    if 70 <= distance <= 90 and time.time() - last_sound_time >= 3.0:
                        distance_text = "Correct"
                        distance_color = (0, 255, 0)  # Green color for correct distance
                        correct_sound.play()  # Play correct sound
                        last_sound_time = time.time()
                    else:
                        distance_text = "Incorrect"
                        distance_color = (0, 0, 255)  # Red color for incorrect distance
                        if time.time() - last_sound_time >= 3.0:
                            incorrect_sound.play()  # Play incorrect sound
                            last_sound_time = time.time()
                    # Display distance and correctness in the top-left corner
                    cv2.putText(im0, f"Distance: {distance:.2f}px {distance_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, distance_color, 2)

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if opt.save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / torch.tensor(im0_shape[1::-1])).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                        with open(save_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if opt.save_img or opt.view_img:  # Add bbox to image
                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

            # Print time (inference + NMS)
            print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms)')

            # Stream results
            if opt.view_img:
                cv2.imshow('YOLOv7 Real-Time Detection', im0)
                if cv2.waitKey(1) == ord('q'):  # 等待按下 'q' 键来退出
                    raise StopIteration

    print(f'Done. ({time.time() - t0:.3f}s)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='best.pt', help='model.pt path(s)')  # 更改默认权重文件为 "best.pt"
    parser.add_argument('--source', type=int, default=0, help='source')  # 0 表示摄像头索引
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-img', action='store_true', help='save results as image files')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')

    opt = parser.parse_args()
    print(opt)

    with torch.no_grad():
        detect()
