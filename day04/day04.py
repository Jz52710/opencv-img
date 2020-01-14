'''

色调，明暗，直方图和Gamma曲线

'''
#导入cv模块
import cv2 as cv
import numpy as np
# =====================图像的仿射变换===============================
# 仿射变换具体到图像中的应用，主要是对图像的缩放，旋转，剪切，翻转和平移的组合。

# 读取一张原始照片
img = cv.imread('img/b.jpg')

# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
M_crop_elephant = np.array([
    [1.6, 0, -150],
    [0, 1.6, -240]
], dtype=np.float32)

img_elephant = cv.warpAffine(img, M_crop_elephant, (400, 600))
cv.imwrite('img/lanka_elephant.jpg', img_elephant)

# x轴的剪切变换，角度15°
theta = 15 * np.pi / 180
M_shear = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)

img_sheared = cv.warpAffine(img, M_shear, (400, 600))
cv.imwrite('img/lanka_safari_sheared.jpg', img_sheared)

# 顺时针旋转，角度15°
M_rotate = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)

img_rotated = cv.warpAffine(img, M_rotate, (400, 600))
cv.imwrite('img/lanka_safari_rotated.jpg', img_rotated)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)

img_transformed = cv.warpAffine(img, M, (400, 600))
cv.imwrite('img/lanka_safari_transformed.jpg', img_transformed)
