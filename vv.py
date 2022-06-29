from PIL import Image
import random
img = Image.open('monte.png')  #读取图片
total = [10, 100, 1000, 10000, 100000, 1000000, 5000000]  #随机点数
for t in total:
    in_count = 0
    for i in range(t):
        x = random.randint(0, img.width-1)
        y = random.randint(0, img.height-1)
        if img.getpixel((x,y))==(255,255,255,255):   #数据输出格式：(R, G, B, A)
            in_count += 1
    print(t,'个随机点时，白色面积为：', int(img.width*img.height*in_count/t))