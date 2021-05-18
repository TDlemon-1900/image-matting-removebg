from PIL import Image
import numpy as np

img_origin = Image.open("H:/抠图数据集/500_images/td已完成/xg/1/no-bg.png")
print("pillow读入img_origin图片尺寸:", img_origin .size, len(img_origin .split()))

r, g, b, alpha = img_origin.split()
image_rgb = Image.merge("RGB", (r, g, b))
image_alpha = alpha
img_rgba2rgb = img_origin.convert("RGB")

image_rgb.save("H:/抠图数据集/500_images/td已完成/xg/1/image_rgb.jpg")
image_alpha.save("H:/抠图数据集/500_images/td已完成/xg/1/alpha.jpg")
img_rgba2rgb.save("H:/抠图数据集/500_images/td已完成/xg/1/img_rgba2rgb.jpg")

alpha_arr = np.array(image_alpha)
print("alpha像素的通道级别：", len(set(alpha_arr.flatten().tolist())))