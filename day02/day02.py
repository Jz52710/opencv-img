
'''
缩放，裁剪和补边
'''
#导入cv模块
import cv2 as cv


# 读取一张原始图片
img = cv.imread('img/b.jpg')

# 缩放成200x200的方形图像
img_200x200 = cv.resize(img, (200, 200))

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
# 等效于img_100x100 = cv2.resize(img, (100, 100))，注意指定大小的格式是(宽度,高度)
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
img_100x100 = cv.resize(img_200x200, (0, 0), fx=0.5, fy=0.5,interpolation=cv.INTER_NEAREST)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
img_200x100 = cv.copyMakeBorder(img_100x100, 50, 50, 0, 0,cv.BORDER_CONSTANT,value=(0, 0, 0))

# 对照片中局部进行剪裁
patch_img = img[220:550, -180:-50]

cv.imwrite('img/cropped_img.jpg', patch_img)
cv.imwrite('img/resized_200x200.jpg', img_200x200)
cv.imwrite('img/resized_100x100.jpg', img_100x100)
cv.imwrite('img/bordered_200x100.jpg', img_200x100)
