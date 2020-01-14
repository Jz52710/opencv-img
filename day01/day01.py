'''
存储图像
'''
#导入cv模块
import cv2 as cv

# 读取一张400x600分辨率的图像
color_img = cv.imread('psb.jpg')
print(color_img.shape)

# 直接读取单通道灰度图
gray_img = cv.imread('psb.jpg', cv.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
cv.imwrite('img/test_grayscale.jpg', gray_img)
reload_grayscale = cv.imread('img/test_grayscale.jpg')
print(reload_grayscale.shape)

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
cv.imwrite('img/test_imwrite.jpg', color_img, (cv.IMWRITE_JPEG_QUALITY, 80))

# cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
cv.imwrite('img/test_imwrite.png', color_img, (cv.IMWRITE_PNG_COMPRESSION, 5))



