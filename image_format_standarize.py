import os
from PIL import Image

CURRENT_PATH = '.'


def convert_image(img_list):
    for webp in img_list:
        ext = os.path.splitext(webp)[1]
        if ext != ".webp":
            continue
        print(webp)
        img_name = webp[0:webp.rindex('.')]
        print(img_name + " to " + img_name + ".jpg")
        # 打开图片并赋值一份新的图片
        webp_path = os.path.join(CURRENT_PATH, webp)
        img = Image.open(webp_path)
        img.load()
        # 将赋值的图片修改后缀保存在原路径
        jpg_path = os.path.join(CURRENT_PATH, img_name + ".jpg")
        print(jpg_path)
        img.save(jpg_path)
        # 删除原webp图
        os.remove(webp_path)

if __name__ == '__main__':
    img_list = []
    for root, dirs, files in os.walk(CURRENT_PATH):
        for f in files:
            img_list.append(os.path.join(root, f))
    convert_image(img_list)
