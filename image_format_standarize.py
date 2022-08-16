import os
import uuid

from PIL import Image

CURRENT_PATH = '.'

TO_SWITCH_EXT = ['.webp', '.png', '.jpg']


def convert_image(img_list):
    for img, img_root in img_list:
        ext = os.path.splitext(img)[1]
        if ext.lower() not in TO_SWITCH_EXT:
            continue
        new_img_fullname = str(uuid.uuid4())
        # 打开图片并赋值一份新的图片
        img_path = os.path.join(CURRENT_PATH, img)
        img = Image.open(img_path)
        img.load()
        if img.height >= 500 and img.width >= 500:
            # 转换通道模式为 RGB
            img = img.convert("RGB")

            # 方形裁切
            if img.height > img.width:
                x1 = 0
                x2 = 0 + img.width
                y1 = int((img.height - img.width) / 2)
                y2 = int((img.height - img.width) / 2) + img.width
            else:
                x1 = int((img.width - img.height) / 2)
                x2 = int((img.width - img.height) / 2) + img.height
                y1 = 0
                y2 = 0 + img.height
            img = img.crop((x1, y1, x2, y2))

            # 重定为 500 * 500 大小的图片以输出
            img = img.resize((500, 500))

            # 将赋值的图片修改后缀保存在原路径
            jpg_path = os.path.join(CURRENT_PATH, os.path.join(img_root, f"{new_img_fullname}.jpg"))
            img.save(jpg_path)
        # 删除原图
        os.remove(img_path)


if __name__ == '__main__':
    img_list = []
    for root, dirs, files in os.walk(CURRENT_PATH):
        for f in files:
            img_list.append((os.path.join(root, f), root))
    convert_image(img_list)
