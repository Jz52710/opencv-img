'''

相机功能

'''
#导入cv模块
import time
import cv2
import os
import sys


interval = 1  # 捕获图像的间隔，单位：秒
num_frames = 50  # 捕获图像的总帧数
out_fps = 24  # 输出文件的帧率

# VideoCapture(0)表示打开默认的相机
cap = cv2.VideoCapture(0)

# 获取捕获的分辨率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 设置要保存视频的编码，分辨率和帧率
video = cv2.VideoWriter(
    "img/demo.avi",
    cv2.VideoWriter_fourcc('M', 'P', '4', '2'),   # 视频编码格式参考  http://www.fourcc.org/codecs.php
    out_fps,
    size
)

# 对于一些低画质的摄像头，前面的帧可能不稳定，略过
for i in range(42):
    cap.read()

# 开始捕获，通过read()函数获取捕获的帧
try:
    for i in range(num_frames):
        _, frame = cap.read()
        video.write(frame)

        # 如果希望把每一帧也存成文件，比如制作GIF，则允许下面的代码运行
        # filename = '{:0>6d}.png'.format(i)
        # cv2.imwrite(filename, frame)

        print('Frame {} is captured.'.format(i))
        time.sleep(interval)
except KeyboardInterrupt:
    # 捕获提前停止。方便后面使已经捕获好的部分视频可以顺利生成
    print('Stopped! {}/{} frames captured!'.format(i, num_frames))

# 释放资源并写入视频文件
video.release()
cap.release()
