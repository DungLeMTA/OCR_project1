
from PIL import Image
#import ImageDraw
#import ImageFont
import fontstyle
from PIL import ImageFont, ImageDraw
import  random
from simple_colors import *

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    max_width = 200
    min_width = 200
    height = 0

    # fontname = "B:\PycharmProjects\OCR_project\\roadway_regular.ttf"
    fontname= "B:\PycharmProjects\OCR_project\\font\\times.ttf"
    # colorText = "white"
    # colorBackground = "black"
    colorText = "black"
    colorBackground = "white"

    with open('Test.txt',encoding="utf8") as file:
        i = 1
        for line in file:
            text_line = line

            # fontsize = random.randint(14,16)
            fontsize = 15
            # colorOutline = "red"

            # x = random.randint(3,7)
            # y = random.randint(3,7)
            # remain_x= random.randint(5,10)
            # remain_y = random.randint(0,10)
            x,y = 3,3
            remain_x,remain_y = 5, 5
            font = ImageFont.truetype(fontname, fontsize)
            width, height = getSize(text_line, font)

            height = 25
            img = Image.new('RGB', (width+remain_x, height), colorBackground) # 704 , 9

            if width+remain_x > max_width:
                max_width = width+remain_x

            if width+remain_x < min_width:
                min_width = width+remain_x

            d = ImageDraw.Draw(img)
            # new_text = ''
            # for i in range(0,len(text_line)):
            #     if text_line[i] == ' ':
            #         new_text += text_line[i]
            #     else:
            #         new_text += text_line[i]+str('\u0332')
            # new_text = '\u0332'.join(' '+text_line)
            # new_text = fontstyle.apply('Hello anh em',
            #           'bold/Italic/UNDERLINE')
            d.text((x,y), text_line, fill=colorText, font=font)

            #d.rectangle((0, 0, width+3, height+3), outline=colorOutline)

            name = str(i)+ '.png'

            if   i<10: name='0000000'+str(i)+ '.png'
            elif i<100: name='000000'+str(i)+ '.png'
            elif i<1000: name='00000'+str(i)+ '.png'
            elif i<10000: name='0000'+str(i)+ '.png'
            elif i<100000: name='000'+str(i)+ '.png'
            elif i<1000000: name='00'+str(i)+ '.png'
            elif i<10000000: name='0'+str(i)+ '.png'
            print(i)
            i+=1

            # img.save("./image100K/image/" + name)
            img.save("test1.png")
    print(max_width,',',min_width)
            #################################################################################

            # for j in range(1,31):
            #
            #     fontsize = random.randint(45,60)
            #     # colorOutline = "red"
            #
            #     x = random.randint(2,8)
            #     y = random.randint(-8,0)
            #
            #     if text.strip() == 'W':
            #         fontsize = random.randint(40, 50)
            #         x = random.randint(2, 7)
            #         y = random.randint(-6, 6)
            #     font = ImageFont.truetype(fontname, fontsize)
            #     # width, height = getSize(text, font)
            #     # print( height)
            #     img = Image.new('RGB', (30, 60), colorBackground) # 460,20
            #     d = ImageDraw.Draw(img)
            #     d.text((x,y), text, fill=colorText, font=font)
            #
            #     name = text.strip()+'_'+str(j)+ '.png'
            #
            #     # name = str(i)+ '.png'
            #     img.save("./A_Z_BW_leaguegothic/"+text.strip()+"/"+name)
            # print(i)
            # i += 1