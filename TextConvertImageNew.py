from PIL import Image
import fontstyle
from termcolor import colored
from PIL import ImageFont, ImageDraw
import  random
from simple_colors import *

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    thongke = [0,0,0,0,0]
    max_width = 200
    min_width = 200
    height = 30

    fontname1 = "B:\PycharmProjects\OCR_project\\font\Times\\times.ttf"
    fontname2 = "B:\PycharmProjects\OCR_project\\font\Times\\timesi.ttf"
    fontname3 = "B:\PycharmProjects\OCR_project\\font\Times\\timesbd.ttf"
    fontname4 = "B:\PycharmProjects\OCR_project\\font\Times\\timesbi.ttf"

    colorText = "black"
    colorBackground = "white"

    f = open('Test.txt','r',encoding="utf8")

    str1 = f.read()
    mang_data = str1.split('\n')

    temp = 1
    for line in mang_data:
        i = 1

        words = line.split(' ')

        fontsize = random.randint(17, 19)
        x = 0
        y = random.randint(1, 4)
        # remain_x = random.randint(0, 1)
        # remain_y = random.randint(0,10)

        for word in words:
            random1 = random.randint(1,100)
            if random1 == 1:
                word='\u0332'.join(' '+word+' ')
                thongke[4] += 1
            if i != len(words):
                word = ' '+word
            else:
                word = ' '+word+' '
                # print(word)
            text = word
            # colorOutline = "red"
            font_d = fontname1
            if random1 == 2:
                font_d = fontname2
                thongke[1] +=1
            if random1 == 3:
                font_d = fontname3
                thongke[2] +=1
            if random1 == 4:
                font_d = fontname4
                thongke[3] +=1
            if random1 != 1 and 2 and 3 and 4:
                thongke[0]+=1

            font = ImageFont.truetype(font_d, fontsize)
            width, h = getSize(text, font)

            img = Image.new('RGB', (width, height), colorBackground) # 704 , 9

            d = ImageDraw.Draw(img)

            d.text((x,y), text, fill=colorText, font=font)

            img.save("./line/test"+str(i)+".png")

            i += 1

        length = 0
        hight = 0
        for j in range(1, i):
            image = Image.open('./line/test' + str(j) + '.png')
            image_size = image.size
            length += image_size[0]
            hight = image_size[1]
        new_image = Image.new('RGB', (length, hight), (250, 250, 250))
        if length > max_width: max_width = length

        if length < min_width: min_width = length
        coordinate_x = 0
        for j in range(1,i):
            image = Image.open('./line/test'+str(j)+'.png')
            image_size = image.size
            new_image.paste(image, (coordinate_x, 0))
            coordinate_x += image_size[0]
        new_image.save("./line_result/image"+str(temp)+".png")

        temp += 1

    print(thongke)
    print(min_width,max_width)

