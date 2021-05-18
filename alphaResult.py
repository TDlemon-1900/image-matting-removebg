#!/usr/bin/python
# -*- coding:UTF-8 -*-
# @author:andy Meng


from PIL import Image
import numpy as np
import os


def alpha(filename, path):
    img_origin = Image.open(filename)         # img_origin = Image.open("H:/抠图数据集/500_images/td已完成/xg/1/no-bg.png")
    print("pillow读入img_origin图片尺寸:", img_origin.size, len(img_origin.split()))

    r, g, b, alpha = img_origin.split()
    image_rgb = Image.merge("RGB", (r, g, b))
    image_alpha = alpha
    img_rgba2rgb = img_origin.convert("RGB")

    #image_rgb.save("H:/抠图数据集/500_images/td已完成/xg/1/image_rgb.jpg")
    image_alpha.save(path)
    #img_rgba2rgb.save("H:/抠图数据集/500_images/td已完成/xg/1/img_rgba2rgb.jpg")

    alpha_arr = np.array(image_alpha)
    print("alpha像素的通道级别：", len(set(alpha_arr.flatten().tolist())))


if __name__ == '__main__':
    # alpha()
    path = r"resultColor/"
    for i in range(0, 1):
        newPath = path + str(i) + "/"
        files = os.listdir(newPath)
        fileNew = ' '.join(files)
        filename = newPath + fileNew
        savePath = newPath + "alpha" + str(i) + ".jpg"
        alpha(filename, savePath)