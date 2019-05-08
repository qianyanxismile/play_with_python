# coding=utf-8

import PIL

from PIL import Image

# 打开原始图片

image_obj = Image.open(r"D:\pic_data\2.jpg")

# 截取一定区域获得新图片
new_image = image_obj.crop((0, 0,300, 395))  # (x1, y1)为区域左上角，(x2, y2)为区域右下角。

new_image.save(r"D:\pic_data\3003951.jpg")

