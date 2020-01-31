"""
问题：
1、如何计算两个像素点间的厘米距离？（ps有些像素点差0.01cm)
1、需要安装python库colormath，使用pip install colormath
2、现在大致的处理思路
    1、需要给我的是psd图像，这样的话就需要分离图层，找到需要的图层（
"""
import cv2
import math
import numpy as np
from PIL import Image
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000


def psd_get_layer():
    """
    对psd文件图层处理
    :return: 处理后需要的图层图片
    """
    pass


def rgb_color_distance(rgb_1, rgb_2):
    """
    使用rgb计算色差
    :param rgb_1: 颜色一(RGB)
    :param rgb_2: 颜色二(RGB)
    :return:  两个色差值
    """
    R_1, G_1, B_1 = rgb_1
    R_2, G_2, B_2 = rgb_2
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    return math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))


def rgb_calculation():
    # im = cv2.imread('./pictures/1.png')
    im = Image.open("./pictures/1.png")
    # cv2.cvtColor(im, im, cv2.COLOR_BGR2HSV)
    target_pixels = [im.getpixel((2, y)) for y in range(0, im.size[1])]
    # print(target_pixels)
    for i in range(0, len(target_pixels)):
        if i <= 250:
            different_value = rgb_color_distance(target_pixels[i], target_pixels[i+1])
            print(different_value)


def lab_calculation():
    im = cv2.imread('./pictures/1.png')
    lab_im = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
    height, width = im.shape[:2]
    delta_e = []
    # 处理图像
    for i in range(0, height):
        if i+1 <= 251:
            lab_a = LabColor(lab_l=lab_im[i][2][0], lab_a=lab_im[i][2][1], lab_b=lab_im[i][2][2])
            lab_b = LabColor(lab_l=lab_im[i+1][2][0], lab_a=lab_im[i+1][2][1], lab_b=lab_im[i+1][2][2])
            delta_e_value = delta_e_cie2000(lab_a, lab_b)
            if delta_e_value <= 2:
                delta_e.append(0.0)
            else:
                delta_e.append(delta_e_value)
    # print(delta_e)
    # 计算
    count = 1
    for i in range(0, len(delta_e)):
        if delta_e[i] == 0.0:
            count += 1
            continue
        else:
            # print(count)
            count = 1

    # p(0, 0) q(5, 0) p(x,y)和q(s,t)
    distance = math.sqrt(np.square(0-5) - np.square(0-0))
    print(distance)



if __name__ == '__main__':
    # rgb_calculation()
    lab_calculation()

