import time
while True:
    correct_pose_start_time = None
    if correct_pose_start_time is None:
        correct_pose_start_time = time.time()
    elif time.time() - correct_pose_start_time >= 5.0:
        final = time.time() - correct_pose_start_time
        print(final)
        yolo_not_detect_once = False
        break  # 跳出for循環
    else:
        print("correct_posetime",end='')
        print(correct_pose_start_time)