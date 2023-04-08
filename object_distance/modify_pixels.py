# 导入需要的模块
from glob import glob
from PIL import Image
import os

# 图片路径
# 使用 glob模块 获得文件夹内所有jpg图像
img_path = glob("images/*.jpg")
# 存储（输出）路径
path_save = "./result"

for i, file in enumerate(img_path):
    name = os.path.join(path_save, "%d.jpg" % i)
    im = Image.open(file)
    # im.thumbnail((720,1280))
    reim = im.resize((740, 555))
    print(im.format, reim.size, reim.mode)
    reim.save(name, im.format)