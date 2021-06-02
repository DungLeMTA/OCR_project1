from PIL import Image
from PIL import ImageFont, ImageDraw
import  random
import multiprocessing
import time

from pyasn1_modules.rfc2315 import Data

dem = 1
def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

def Data_Gen(fromfile,fonts,colorText,colorBackground,height,min_width,max_width): #start

    f = open(fromfile, 'r', encoding="utf8")

    str1 = f.read()
    mang_data = str1.split('\n')
    f.close()

    TONG = len(mang_data)-1
    # print(TONG)
    temp = 1
    # dem = start+1
    # print('Bắt đầu từ: ',start)
    for line in mang_data:
        i = 1

        words = line.split(' ')

        fontsize = random.randint(17, 19)
        x = 0
        y = random.randint(1, 4)
        # remain_x = random.randint(0, 1)
        # remain_y = random.randint(0,10)

        # chuyển đổi vai trò giữa các kiểu font
        if temp == int(TONG*0.85): fonts[0], fonts[1], fonts[2], fonts[3] = fonts[1], fonts[0], fonts[2], fonts[3]
        if temp == int(TONG*0.91): fonts[0], fonts[1], fonts[2], fonts[3] = fonts[2], fonts[1], fonts[0], fonts[3]
        if temp == int(TONG*0.96): fonts[0], fonts[1], fonts[2], fonts[3] = fonts[3], fonts[2], fonts[1], fonts[0]
        if temp == int(TONG*0.98): fonts[0], fonts[1], fonts[2], fonts[3] = fonts[1], fonts[2], fonts[3], fonts[0]
        if temp < int(TONG*0.98):
            for word in words:
                random1 = random.randint(0, 4000)
                if random1 == 0:
                    word = '\u0332'.join(' ' + word + ' ')
                    # thongke[4] += 1
                if i != len(words):
                    word = ' ' + word
                else:
                    word = ' ' + word + ' '+fromfile
                    # print(word)
                text = word
                # colorOutline = "red"
                random2 = random.randint(0, 1000)
                font_d = fonts[0]
                if random2 == 1:
                    font_d = fonts[1]
                    # thongke[1] += 1
                if random2 == 2:
                    font_d = fonts[2]
                    # thongke[2] += 1
                if random2 == 3:
                    font_d = fonts[3]
                if random2 == 4:
                    text = text.upper()
                    # thongke[3] += 1
                # if random1 != 1 and 2 and 3 and 4:
                    # thongke[0] += 1

                font_u = ImageFont.truetype(font_d, fontsize)
                width, h = getSize(text, font_u)
                img = Image.new('RGB', (width, height), colorBackground)  # 704 , 9
                d = ImageDraw.Draw(img)
                d.text((x, y), text, fill=colorText, font=font_u)
                img.save("./line"+fromfile.replace('.txt','')+"/test" + str(i) + ".png")
                i += 1
        else:
            for word in words:
                random1 = random.randint(0 , 20)
                if random1 == 0:
                    word = '\u0332'.join(' ' + word + ' ')
                    # thongke[4] += 1
                if i != len(words):
                    word = ' ' + word
                else:
                    word = ' ' + word + ' '+fromfile
                    # print(word)
                text = word
                # colorOutline = "red"
                random2 = random.randint(0, 6)
                font_d = fonts[0]
                if random2 == 1:
                    font_d = fonts[1]
                    # thongke[1] += 1
                if random2 == 2:
                    font_d = fonts[2]
                    # thongke[2] += 1
                if random2 == 3:
                    font_d = fonts[3]
                    # thongke[3] += 1
                # if random1 != 1 and 2 and 3 and 4:
                    # thongke[0] += 1

                font_u = ImageFont.truetype(font_d, fontsize)
                width, h = getSize(text, font_u)
                img = Image.new('RGB', (width, height), colorBackground)  # 704 , 9
                d = ImageDraw.Draw(img)
                d.text((x, y), text, fill=colorText, font=font_u)
                img.save("./line"+fromfile.replace('.txt','')+"/test" + str(i) + ".png")
                i += 1

        length = 0
        hight = 0
        for j in range(1, i):
            image = Image.open('./line'+fromfile.replace('.txt','')+'/test' + str(j) + '.png')
            image_size = image.size
            length += image_size[0]
            hight = image_size[1]
        new_image = Image.new('RGB', (length, hight), (250, 250, 250))
        if length > max_width: max_width = length

        if length < min_width: min_width = length
        coordinate_x = 0
        for j in range(1, i):
            image = Image.open('./line'+fromfile.replace('.txt','')+'/test' + str(j) + '.png')
            image_size = image.size
            new_image.paste(image, (coordinate_x, 0))
            coordinate_x += image_size[0]
        global dem
        new_image.save("./line_result/image" + str(dem) + ".png")
        print(dem)
        temp += 1
        dem += 1

    # print(thongke)
    print(min_width, max_width)

if __name__ == '__main__':

    thongke = [0,0,0,0,0]

    fonts_dir =  "B:\PycharmProjects\OCR_project\\font"

    fontname1  =  fonts_dir+"\TIMES\TIMES.ttf"   # 85% song song đó là 95% thường, 5% in
    fontname2  =  fonts_dir+"\TIMES\TIMESI.ttf"  # 6%
    fontname3  =  fonts_dir+"\TIMES\TIMESB.ttf"  # 6%
    fontname4  =  fonts_dir+"\TIMES\TIMESBI.ttf" # 3%

    fontname5  =  fonts_dir+"\SEGOEUI\SEGOEUI.ttf"
    fontname6  =  fonts_dir+"\SEGOEUI\SEGOEUII.ttf"
    fontname7  =  fonts_dir+"\SEGOEUI\SEGOEUIB.ttf"
    fontname8  =  fonts_dir+"\SEGOEUI\SEGOEUIBI.ttf"

    fontname9  =  fonts_dir+"\TAHOMA\TAHOMA.ttf"
    fontname10 =  fonts_dir+"\TAHOMA\TAHOMAI.ttf"
    fontname11 =  fonts_dir+"\TAHOMA\TAHOMAB.ttf"
    fontname12 =  fonts_dir+"\TAHOMA\TAHOMABI.ttf"

    fontname13 =  fonts_dir+"\HELVETICA\HELVETICA.ttf"
    fontname14 =  fonts_dir+"\HELVETICA\HELVETICAI.ttf"
    fontname15 =  fonts_dir+"\HELVETICA\HELVETICAB.ttf"
    fontname16 =  fonts_dir+"\HELVETICA\HELVETICABI.ttf"

    fontname17 =  fonts_dir+"\OPEN\OPEN.ttf"
    fontname18 =  fonts_dir+"\OPEN\OPENI.ttf"
    fontname19 =  fonts_dir+"\OPEN\OPENB.ttf"
    fontname20 =  fonts_dir+"\OPEN\OPENBI.ttf"

    # fontname21 =  fonts_dir+"\VNTIME\VNTIME.ttf"
    # fontname22 =  fonts_dir+"\VNTIME\VNTIMEI.ttf"
    # fontname23 =  fonts_dir+"\VNTIME\VNTIMEB.ttf"
    # fontname24 =  fonts_dir+"\VNTIME\VNTIMEBI.ttf"
    #
    # fontname25 =  fonts_dir+"\CALIBRI\CALIBRI.ttf"
    # fontname26 =  fonts_dir+"\CALIBRI\CALIBRII.ttf"
    # fontname27 =  fonts_dir+"\CALIBRI\CALIBRIB.ttf"
    # fontname28 =  fonts_dir+"\CALIBRI\CALIBRIBI.ttf"
    #
    # fontname29 =  fonts_dir+"\GEO\GEO.ttf"
    # fontname30 =  fonts_dir+"\GEO\GEOI.ttf"
    # fontname31 =  fonts_dir+"\GEO\GEOB.ttf"
    # fontname32 =  fonts_dir+"\GEO\GEOBI.ttf"

    colorText = "black"
    colorBackground = "white"
    max_width = 200
    min_width = 200
    height = 30

    # f = open('Test.txt', 'r', encoding="utf8")
    #
    # str1 = f.read()
    # mang_data = str1.split('\n')
    # f.close()
    # TONG = len(mang_data) -1

    start = time.time()
    font_Times = [fontname1, fontname2, fontname3, fontname4]
    Data_Gen('All_TIMES.txt',font_Times,colorText,colorBackground,height,min_width,max_width)
    # p1 = multiprocessing.Process(target=Data_Gen, args=('All_TIMES.txt',font_Times,colorText,
    #                                                     colorBackground,height,min_width,max_width,0))

    font_Segoe = [fontname5, fontname6, fontname7, fontname8]
    Data_Gen('All_SEGOEUI.txt',font_Segoe,colorText,colorBackground,height,min_width,max_width)
    # p2 = multiprocessing.Process(target=Data_Gen, args=('All_SEGOEUI.txt',font_Segoe,colorText,
    #                                                     colorBackground,height,min_width,max_width,int(TONG*0.4)))

    font_Taho = [fontname9, fontname10, fontname11, fontname12]
    Data_Gen('All_TAHOMA.txt',font_Taho,colorText,colorBackground,height,min_width,max_width)
    # p3 = multiprocessing.Process(target=Data_Gen, args=('All_TAHOMA.txt',font_Taho,colorText,
    #                                                     colorBackground,height,min_width,max_width,int(TONG*0.6)))

    font_Hel = [fontname13, fontname14, fontname15, fontname16]
    Data_Gen('All_HELVETICA.txt',font_Hel,colorText,colorBackground,height,min_width,max_width)
    # p4 = multiprocessing.Process(target=Data_Gen, args=('All_HELVETICA.txt',font_Hel,colorText,
    #                                                     colorBackground,height,min_width,max_width,int(TONG*0.8)))

    font_Open = [fontname17, fontname18, fontname19, fontname20]
    Data_Gen('All_OPEN.txt',font_Open,colorText,colorBackground,height,min_width,max_width)

    print("Tổng thời gian là: %.5f"%(time.time()-start))
    # p5 = multiprocessing.Process(target=Data_Gen, args=('All_OPEN.txt',font_Open,colorText,
    #                                                     colorBackground,height,min_width,max_width,int(TONG*0.9)))



