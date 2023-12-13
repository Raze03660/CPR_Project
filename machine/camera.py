# Camera
import re
import socket
from queue import Queue
from threading import Thread
import numpy as np
from PySide6.QtCore import QThread, QCoreApplication
# from pymongo import MongoClient
import pyopenpose as op
from gui.signal_container import SignalContainer, LabelContainer, LabelDeepContainer, \
    FrequencyLabelContainer, DepthPostureLabelContainer, PositionLabelContainer, \
    RateLabelContainer, FrequencyLabelResultContainer, DeepLabelResultContainer, PostureLabelResultContainer, \
    textEditResultContainer
from keypoints.angle import Angle
from machine.BODY_25 import BODY_25
from machine.position_config import PositionConfig
from pdf_test import create_certificate_with_specified_background
# from machine.Scratch import Scratch
from fancy import config as cfg
import playsound
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


class Camera(QThread):
    y1: float
    y2: float
    y3: float
    depth: float
    play_sound: int
    is_test: bool
    is_pose_abnormal: bool  #
    is_deep_abnormal: bool
    is_freq_abnormal: bool

    def __init__(self, num_camera, width=800, height=600):
        super(Camera, self).__init__()
        pygame.mixer.init()
        self.num_camera = num_camera
        self.cap = cv2.VideoCapture(2)
        self.width = width
        self.height = height
        # todo y1,y2,de
        args = self.get_arg_parser().parse_args()
        position_config = PositionConfig(cfg.YamlConfigLoader(args.position))
        # self.y1 = 381
        # self.y2 = 391
        # self.depth = 53
        self.y1 = position_config.y1
        self.y2 = position_config.y2
        self.received_data = 0
        self.max = 0
        self.lastmin = 0
        self.depth = position_config.depth
        self.ratio = 0.4
        self.result_str_save = 0
        self.control = True
        self.counter = 0
        self.Round = 1
        self.deepnum = 0
        self.frequencynum = 0
        self.poseturenum = 0
        self.frequencycounter = 0
        self.passed1 = "Passed"
        self.passed2 = "Passed"
        self.passed3 = "Passed"
        self.is_play_sound = None
        self.is_test = position_config.is_test
        self.is_stop = False
        self.float_array = []  # test2
        self.result_array = []
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.rawdata = SignalContainer()  # original image
        self.right_hand = LabelContainer()  # angle of pose
        self.left_hand = LabelContainer()
        self.frequency_label = FrequencyLabelContainer()
        self.depth_estimate_label = LabelDeepContainer()
        self.depth_posture_label = DepthPostureLabelContainer()
        self.rate_label = RateLabelContainer()
        self.deep_result_label = DeepLabelResultContainer()
        self.frequency_result_label = FrequencyLabelResultContainer()
        self.position_label = PositionLabelContainer()
        self.posture_result_label = PostureLabelResultContainer()
        self.textEdit_result_label = textEditResultContainer()
        # self.time_label = TimeLabelContainer()
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # 初始化yolo參數
        self.weights = '/home/ezio/CPR_Project_Demo/models/best.pt'
        self.source = args.source
        self.img_size = args.img_size
        self.conf_thres = args.conf_thres
        self.iou_thres = args.iou_thres
        self.device = args.device
        self.save_txt = args.save_txt
        self.save_conf = args.save_conf
        self.save_img = args.save_img
        self.classes = args.classes
        self.agnostic_nms = args.agnostic_nms
        self.augment = args.augment
        self.correct_pose_start_time = None  # 用於跟踪YOLO姿勢正確的開始時間
        self.yolo_not_detect_once = True
        self.view_img = args.view_img

        # 深度初始化 设置服务器 IP 和端口
        self.server_ip = "140.128.18.98"
        self.server_port = 8080
        # Load audio files
        self.incorrect_sound = pygame.mixer.Sound(
            '/home/ezio/CPR_Project_Demo/sound/postition_abnormal.wav')  # Replace with your incorrect sound file
        self.start_openpose_sound = pygame.mixer.Sound(
            '/home/ezio/CPR_Project_Demo/sound/start_openpose.wav')  # Replace with your incorrect sound file
        # if self.is_play_sound:
        #     self.is_deep_abnormal = True
        #     self.is_pose_abnormal = True
        #     self.is_freq_abnormal = True

        self.sound_queue = Queue()
        self.sound_thread = Thread(target=handle_playsound, args=(self.sound_queue,), daemon=True)
        self.sound_thread.start()

        if self.cap is None or not self.cap.isOpened():
            self.running = False
            self.connect = False
            self.is_preview = False
        else:
            self.connect = True
            self.running = True
            self.is_preview = True

    def setId(self, Id="Default User"):
        self.id = Id

    # 计算两个边界框之间的水平距离
    def calculate_distance(self, box1, box2):
        x1_min, y1_min, x1_max, y1_max = box1
        x2_min, y2_min, x2_max, y2_max = box2
        x1_center = (x1_min + x1_max) / 2
        x2_center = (x2_min + x2_max) / 2
        distance = abs(x1_center - x2_center)
        return distance

    def run_yolo(self):
        count = 0
        source, weights, imgsz = str(self.source), self.weights, self.img_size
        print("初始化...")
        # Initialize
        set_logging()
        device = select_device(self.device)
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
        print("載入模型成功")
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
            if self.yolo_not_detect_once:
                if im0s is None or len(im0s) == 0:
                    continue  # Skip empty frames

                img = torch.from_numpy(img).to(device)
                img = img.half() if half else img.float()  # uint8 to fp16/32
                img /= 255.0  # 0 - 255 to 0.0 - 1.0
                if img.ndimension() == 3:
                    img = img.unsqueeze(0)

                # Inference
                t1 = time_synchronized()
                pred = model(img, augment=self.augment)[0]

                # Apply NMS
                pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes=self.classes,
                                           agnostic=self.agnostic_nms)
                t2 = time_synchronized()

                # Process detections
                for i, det in enumerate(pred):  # detections per image
                    count += 1
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
                            distance = self.calculate_distance(box1, box2)
                            s += f"Distance: {distance:.2f}px"
                            # Determine if the distance is correct or not
                            if 82.5 <= distance <= 100:
                                print("按壓位置正確")
                                self.position_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                 u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Normal</span></p></body></html>",
                                                                                                 None))

                                # self.correct_sound.play()
                                distance_text = "Correct"
                                distance_color = (0, 255, 0)  # Green color for correct distance
                                self.rawdata.update_image.emit(im0)  # 發送 YOLO 處理後的圖像
                                if self.correct_pose_start_time is None:
                                    self.correct_pose_start_time = time.time()  # 开始计时
                                elif time.time() - self.correct_pose_start_time >= 5.0:
                                    print(f"現在timer目前為{5.0}秒")
                                    self.yolo_not_detect_once = False
                                    print("維持5秒位置正確")
                                    break
                                else:
                                    print(f"現在timer目前為{time.time() - self.correct_pose_start_time:.2f}秒")
                            else:
                                distance_text = "Incorrect"
                                distance_color = (0, 0, 255)  # Red color for incorrect distance
                                self.position_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                 u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>",
                                                                                                 None))
                                if count % 40 == 0:
                                    self.incorrect_sound.play()

                                # self.incorrect_sound.play()
                                print("按壓位置異常請重新調整")
                                self.rawdata.update_image.emit(im0)  # 發送 YOLO 處理後的圖像
                                self.correct_pose_start_time = None  # 重置计时器

                            # Display distance and correctness in the top-left corner
                            cv2.putText(im0, f"Distance: {distance:.2f}px {distance_text}", (10, 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, distance_color, 2)

                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            if self.save_txt:  # Write to file
                                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / torch.tensor(im0_shape[1::-1])).view(
                                    -1).tolist()  # normalized xywh
                                line = (cls, *xywh, conf) if self.save_conf else (cls, *xywh)  # label format
                                with open(save_path + '.txt', 'a') as f:
                                    f.write(('%g ' * len(line)).rstrip() % line + '\n')

                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)
                    else:
                        self.rawdata.update_image.emit(im0)  # 发送原始图像，因为没有检测到任何对象

                    self.position_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>",
                                                                                     None))
                    self.rawdata.update_image.emit(im0)  # 發送 YOLO 處理後的圖像
                    # Print time (inference + NMS)
                    print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms)')
            else:
                break

                # print("發送 YOLO 處理後的圖像")
        # print(f'Done. ({time.time() - t0:.3f}s)')

    def run(self) -> None:

        frame_cnt = 0
        # todo
        # openpose using model
        num_keypoint = 25
        FRAME_CNT = 50000
        #
        seq_length = int(FRAME_CNT)
        feature_array = np.zeros([seq_length, num_keypoint, 3], np.float32)
        is_play_sound = False
        poseModel = op.PoseModel.BODY_25

        params = dict()
        params["model_folder"] = "/home/ezio/openpose/models/"
        # resolution:320*camera(height/2)
        params["net_resolution"] = "320x-1"
        params['number_people_max'] = 1
        op_wrapper = op.WrapperPython()
        op_wrapper.configure(params)
        op_wrapper.start()
        datum = op.Datum()
        path = '/home/ezio/CPR_Project_Demo/output.txt'
        i = 0
        j = 0
        countNum = 0
        is_trace_down = True
        # 建立套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定 IP 和端口
        server_socket.bind((self.server_ip, self.server_port))

        # 開始監聽
        server_socket.listen(1)
        print(f"等待連接在 {self.server_ip}:{self.server_port} 上的消息...")
        # 接收端連線
        client_socket, client_address = server_socket.accept()
        print(f"已連接到 {client_address}")

        while self.running and self.connect:
            # yolo還沒偵測過
            if self.yolo_not_detect_once and not self.is_preview and not self.is_stop:
                self.sound_queue.put("/home/ezio/CPR_Project_Demo/sound/CPR_Start.wav")
                print("開始執行YOLO辨識")
                self.sound_queue.put("/home/ezio/CPR_Project_Demo/sound/yolo_start.wav")
                self.run_yolo()
                self.yolo_not_detect_once = False
                self.start_openpose_sound.play()
                print("YOLO辨識執行結束")

                start_time = time.time()
            ret, frame = self.cap.read()
            if ret and self.is_preview:
                self.rawdata.update_image.emit(frame)  # 發
                self.right_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                             None))

                self.left_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                            None))
                self.depth_estimate_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                       u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                                       None))
                self.frequency_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                  u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                                  None))
                self.depth_posture_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                                      None))
                self.rate_label.update_label.emit(QCoreApplication.translate("Form",
                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">尚未開始偵測</span></p></body></html>",
                                                                             None))

            if ret and not self.is_preview and not self.is_stop:
                try:
                    data = client_socket.recv(4096)  # 接收数据
                    received_data = data.decode('utf-8').strip()  # 去除空白字符

                    if not received_data:
                        continue
                    numbers = re.findall(r'\d+\.*\d*', received_data)

                    # 將提取的數字轉換為浮點數，這里假設使用浮點數進行操作
                    numbers = [float(num) for num in numbers]

                    # 假設進行除以 10 和減去 11.7 的操作
                    result = [(num / 10) - 11.7 for num in numbers]

                    # 將結果轉換為絕對值
                    abs_result = [abs(num) for num in result]

                    # 將結果四捨五入到小數點後第二位
                    rounded_result = [round(num, 2) for num in abs_result]

                    # 將結果轉換為純數字字符串，小數點後只保留一位
                    result_str = ''.join(map(lambda x: f"{x:.1f}", rounded_result))
                    print(result_str)

                    # last_time = datetime.datetime.now()
                    datum.cvInputData = frame
                    op_wrapper.emplaceAndPop(op.VectorDatum([datum]))
                    # get the 25 key points
                    keypoints = datum.poseKeypoints[0]
                    feature_array[frame_cnt, :, :] = keypoints

                    # Right hand position [wrist, shoulder ,elbow]
                    RWrist = feature_array[frame_cnt, BODY_25.RWrist.value, :]
                    RShoulder = feature_array[frame_cnt, BODY_25.RShoulder.value, :]
                    RElbow = feature_array[frame_cnt, BODY_25.RElbow.value, :]
                    right_hand = [RShoulder, RElbow, RWrist]
                    right_angle = Angle(right_hand).angle_between_point()

                    # Left hand position  [wrist, shouder ,elbow]
                    LWrist = feature_array[frame_cnt, BODY_25.LWrist.value, :]
                    LShoulder = feature_array[frame_cnt, BODY_25.LShoulder.value, :]
                    LElbow = feature_array[frame_cnt, BODY_25.LElbow.value, :]
                    left_hand = [LShoulder, LElbow, LWrist]
                    left_angle = Angle(left_hand).angle_between_point()

                    if float(result_str) > 5.5 and float(result_str) < 7.5 and self.control == True:
                        self.control = False
                        self.counter += 1
                        if float(result_str) >= 5 and float(result_str) <= 7:
                            self.deepnum += 1
                        print(self.counter)
                    if float(result_str) < 5.5 and self.control == False:
                        self.control = True
                    if self.counter == 30:
                        self.Round += 1
                        self.counter = 0

                    # if self.Round == 6 :
                    #     self.Round =1
                    # self.result_str_save = float(result_str)

                    if i % 5 == 0:
                        if 5.0 <= float(result_str) <= 7.0:
                            end_time = time.time()
                            current_time = end_time - start_time
                            timee = (60 / current_time)
                            # self.depth_posture_label.update_label.emit(QCoreApplication.translate("Form",
                            #                                                                  u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">Normal</span></p></body></html>",
                            #                                                                  None))
                            # if float(timee)-120 > 90 and float(timee) - 120 < 135:

                            if round(timee, 2) + 95 < 140:
                                self.frequencycounter += 1
                                self.frequency_label.update_label.emit(str(round(timee, 2) + 95))
                                print(round(timee, 2) + 95)

                                if round(timee, 2) + 95 > 122 and round(timee, 2) + 95 < 139:
                                    self.frequency_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">按壓頻率太快</span></p></body></html>",
                                                                                                      None))
                                    self.sound_queue.put('/home/ezio/CPR_Project_Demo/sound/frequency_fast.wav')
                                elif round(timee, 2) + 95 < 100 or (
                                        round(timee, 2) + 95 < 140 and round(timee, 2) + 95 > 139):
                                    self.frequency_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">按壓頻率太慢</span></p></body></html>",
                                                                                                      None))
                                    self.sound_queue.put('/home/ezio/CPR_Project_Demo/sound/frequency_low.wav')
                                elif round(timee, 2) + 95 < 122 and round(timee, 2) + 95 > 100:
                                    self.frequencynum += 1

                        start_time = end_time
                    if i % 20 == 0:
                        if self.is_play_sound:
                            # if self.is_deep_abnormal and (float(result_str) > 7 or float(result_str) < 5):
                            #     self.sound_queue.put('/home/ezio/openpose/CPR_Project_Demo/sound/deep_abnormal.mp3')
                            #     self.is_deep_abnormal = False

                            if right_angle <= 165 or left_angle <= 165:
                                self.sound_queue.put('/home/ezio/CPR_Project_Demo/sound/post_abnormal.mp3')
                                self.left_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">手臂角度異常</span></p></body></html>",
                                                                                            None))
                                self.poseturenum += 1

                        if right_angle <= 165 or left_angle <= 165:
                            self.is_play_sound = True
                        else:
                            self.is_play_sound = False
                    if i % 10 == 0:
                        # hands = self.collection.find({"Id": self.id, "items": i}).next()
                        if not self.is_test:
                            if left_angle == -1 or None:
                                self.left_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到左手臂</span></p></body></html>",
                                                                                            None))
                            else:
                                self.left_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">{}</span></p></body></html>".format(
                                                                                                left_angle),
                                                                                            None))

                            if right_angle == -1:
                                self.right_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到右手臂</span></p></body></html>",
                                                                                             None))
                            else:
                                self.right_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">{}</span></p></body></html>".format(
                                                                                                 right_angle),
                                                                                             None))

                        else:
                            if left_angle == -1:
                                self.left_hand.update_label.emit('無法偵測到左手臂')
                            else:
                                self.left_hand.update_label.emit(str(left_angle))

                            if right_angle == -1:
                                self.right_hand.update_label.emit('無法偵測到右手臂')
                            else:
                                self.right_hand.update_label.emit(str(RWrist[1]))

                            # self.left_hand.update_label.emit(str(hands['Left_Angle']))
                            # self.right_hand.update_label.emit(str(hands['Right_Angle']))
                            # self.left_hand.update_label.emit(str(left_angle))
                            # self.right_hand.update_label.emit(str(right_angle))

                        j = j + 1
                        # 2022.08.22

                        if (right_angle <= 165 or left_angle <= 165) and (left_angle != -1 or right_angle != -1):
                            if 5.0 <= float(result_str) <= 7.0:
                                self.depth_estimate_label.update_label.emit(str(result_str))
                        else:
                            if 5.0 <= float(result_str) <= 7.0:
                                self.depth_estimate_label.update_label.emit(str(result_str))

                    if self.Round == 2:
                        self.sound_queue.put('/home/ezio/CPR_Project_Demo/sound/round_end.wav')
                        # 判斷深度是否大於8成
                        if float(self.deepnum / 30) >= 0.8:
                            self.deep_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">通過</span></p></body></html>",
                                                                                                None))
                            self.result_array[0]=float(self.deepnum / 30)
                            print(f"深度:{self.deepnum}  按壓次數:{30} 正確率:{float(self.deepnum / 30)}")
                            self.passed1 = "Passed"
                        else:
                            self.deep_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">不通過</span></p></body></html>",
                                                                                                None))
                            self.result_array[0] = float(self.deepnum / 30)
                            print(f"深度:{self.deepnum}  按壓次數:{30} 正確率:{float(self.deepnum / 30)}")
                            self.passed1 = "Not Passed"

                        # 判斷頻率是否大於6成
                        if float(self.frequencynum / self.frequencycounter) >= 0.6:
                            self.frequency_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">通過</span></p></body></html>",
                                                                                                     None))
                            self.result_array[1] = float(self.frequencynum / self.frequencycounter)
                            print(
                                f"頻率:{self.frequencynum}  按壓次數:{self.frequencycounter} 正確率:{float(self.frequencynum / self.frequencycounter)}")
                            self.passed2 = "Passed"
                        else:
                            self.frequency_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">不通過</span></p></body></html>",
                                                                                                     None))
                            self.result_array[1] = float(self.frequencynum / self.frequencycounter)
                            print(
                                f"頻率:{self.frequencynum}  按壓次數:{self.frequencycounter} 正確率:{float(self.frequencynum / self.frequencycounter)}")
                            self.passed2 = "Not Passed"

                        # 判斷姿勢錯誤是否小於5次
                        if self.poseturenum <= 5:
                            self.posture_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                   u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">通過</span></p></body></html>",
                                                                                                   None))
                            self.result_array[2] = float(self.poseturenum)
                            print(f"姿勢:{self.poseturenum}  錯誤次數:{float(self.poseturenum)}")
                            self.passed3 = "Passed"
                        else:
                            self.posture_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                   u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">不通過</span></p></body></html>",
                                                                                                   None))
                            self.result_array[2] = float(self.poseturenum)
                            print(f"姿勢:{self.poseturenum}  錯誤次數:{float(self.poseturenum)}")
                            self.passed3 = "Not Passed"

                        # 最終結果輸出
                        if float(self.frequencynum / self.frequencycounter) >= 0.6 and float(self.deepnum / 30) >= 0.8:
                            self.textEdit_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                    u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ef2929;\">恭喜通過</span></p></body></html>",
                                                                                                    None))
                            create_certificate_with_specified_background(self.result_array, self.id, self.passed1,
                                                                         self.passed2,
                                                                         self.passed3,
                                                                         '/CPR_Certificate/cpr_certificate.pdf',
                                                                         '/pic/cpr_certificate_background3.png')
                        else:
                            self.textEdit_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                    u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ef2929;\">再接再厲</span></p></body></html>",
                                                                                                    None))
                            create_certificate_with_specified_background(self.result_array, self.id, self.passed1,
                                                                         self.passed2,
                                                                         self.passed3,
                                                                         '/CPR_Certificate/cpr_certificate.pdf',
                                                                         '/pic/cpr_certificate_background3.png')


                        # Reset info.
                        self.Round = 1
                        self.counter = 0
                        self.poseturenum = 0
                        self.deepnum = 0
                        self.frequencynum = 0
                        self.frequencycounter = 0

                    if self.is_preview == True:
                        self.deep_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\"></span></p></body></html>",
                                                                                            None))
                        self.frequency_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                                 u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\"></span></p></body></html>",
                                                                                                 None))
                        self.posture_result_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                               u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\"></span></p></body></html>",
                                                                                               None))

                except Exception as e:
                    if e:
                        self.left_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                    u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到左手臂</span></p></body></html>",
                                                                                    None))
                        self.right_hand.update_label.emit(QCoreApplication.translate("Form",
                                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到右手臂</span></p></body></html>",
                                                                                     None))
                        self.depth_estimate_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                               u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到深度</span></p></body></html>",
                                                                                               None))
                        self.frequency_label.update_label.emit(QCoreApplication.translate("Form",
                                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">無法偵測到頻率</span></p></body></html>",
                                                                                          None))

                        print("偵測中.....(無法偵測到人) ")
                    pass
                    # raise
                i = i + 1
                ''' '''
                self.rawdata.update_image.emit(datum.cvOutputData)  # 發
                # if not self.is_preview and self.out:
                #     self.out.write(frame)

    # preview the video
    def preview(self):
        if self.connect:
            self.running = True  # 啟動讀取狀態
            self.start()

    def open(self):
        if self.connect:
            self.running = True  # 啟動讀取狀態
            self.is_preview = False
            self.is_stop = False
            # self.is_Certificate = False
            # time_str = time.strftime("%Y%m%d-%H%M%S")
            # if self.num_camera == 0:
            #     # 寫入影片
            #     self.filename = '/home/ezio/openpose/CPR_Project1/medias/record/' + time_str + '.avi'
            #     self.out = cv2.VideoWriter(self.filename, self.fourcc, 30.0, (self.width, self.height))

    def stop(self):
        if self.connect:
            self.running = True  # 關閉讀取狀態
            self.is_preview = True
            self.is_stop = True
            # self.is_Certificate = True

    def exit(self, retcode=0):
        if self.connect:
            self.running = False  # 關閉讀取狀態
            # self.is_preview = False
        super().exit(retcode)

    def get_arg_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--position", type=Path,
                            default=Path("/home/ezio/CPR_Project_Demo/configs/config.yaml"))
        # yolo config
        parser.add_argument('--view-img', action='store_true', help='display results')
        parser.add_argument('--source', type=int, default=0, help='source')  # 0 表示摄像头索引
        parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.45, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
        parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
        parser.add_argument('--save-img', action='store_true', help='save results as image files')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
        return parser


def handle_playsound(queue: Queue):
    while True:
        # 佇列中取出下一個聲音資料的路徑
        sound_path = queue.get()
        playsound.playsound(sound_path)
