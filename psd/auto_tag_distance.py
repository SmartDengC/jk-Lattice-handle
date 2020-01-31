import cv2  # opencv python package
import numpy as np


img_view = cv2.imread("./pictures/1.png", 0)
cv2.cvtColor(img_view, img_view, cv2.COLOR_BGR2HSV)
print(img_view[0])
print(img_view.shape)  #(252,252,3) width height channel
img_view_shape = img_view.shape
height, width = img_view.shape[:2]
print(type(width), width)
print(type(height), height)
# resize_img = cv2.resize(img_view, (3*height, 3*width), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('origin.png', resize_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

count = 0
num = img_view[0][0]
for i in range(img_view_shape[1]):
    if i+1 <= img_view_shape[1]:
        if img_view[0][i] == img_view[0][i+1]:
            count += 1
        else:
            # 更换底数
            num = img_view[0][i+1]
            print(count)
            count = 0


# cv2.cvtColor(img_view,img_view)
# cv2.namedWindow("show")
# cv2.imshow("shwo", img_view)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(type(img_view))
# get_pixel = img_view.shape  # height, wight, channel numberh
# get_size = img_view.size
# get_dtype = img_view.dtype
# print(get_pixel)
# tag = 0
# # 获得了 他的每一个像素点
#
# pixel_list = []

#
# # 获得了 他的每一个像素点
# for i in range(get_pixel[0]+1-6, get_pixel[0]+1):
#         pixel_list.extend(img_view[i,1])
#
#
# for j in range(len(pixel_list)):
#     print(pixel_list[i])
#






