import random

letters = 'aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’ '
dau = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’'
dic = []
f = open('dictionary.txt','r',encoding='utf-8')
str = f.read()
mang = str.split('\n')
for j in mang:
    if j.strip() != '':
        dic.append(j)
f.close()

f = open('All3.txt','r',encoding='utf-8')
f1 = open('All4.txt','w',encoding='utf-8')
str = f.read()
mang = str.split('\n')
temp = 1
for i in range(0,len(mang)-1):

    # j = random.randint(0, 500)
    # if j == 1:
    #     mang[i] = mang[i].upper()
    #     print(i)
    # words = mang[i].split(' ')
    # count = len(words)
    # cau1 = ''
    # cau2 = ''
    #
    #
    # if count > 20:
    #     for j in range(0,20):
    #         cau1 += words[j] + ' '
    #     for j in range(20,count-1):
    #         cau2 += words[j] + ' '
    # else:
    #     cau1 = mang[i]
    # if cau1.strip() != '':
    #     f1.writelines(cau1.strip()+'\n')
    # if cau2.strip() != '' and '\n':
    #     f1.writelines(cau2.strip() + '\n')


    # if mang[i].strip() != '':
    #     for j in mang[i]:
    #         if j not in letters:
    #             mang[i]=mang[i].replace(j,'')
    #             print('dòng ',i,' kí tự: ',j)
    #     f1.writelines(mang[i]+'\n')

    ''' kiểm tra từ bị dính vào nhau
    
    word = mang[i].split(' ')
    for j in word:

        for k in j:
            if k in dau:
                j = j.replace(k,'')
        if j.lower() not in dic and j.isnumeric() == False and j.strip() != '':
            # print('dòng ',i, ' từ: ',j )
            t = True
            m=1
            while(t):
                if m>= len(j)-1:
                    break
                word1 =''
                word2 = ''
                for m1 in range(0,m):
                    word1+=j[m1]
                for m1 in range(m,len(j)):
                    word2+=j[m1]

                # print(word1,' + ', word2)
                if word1.lower() in dic and word2.lower() in dic:
                    t = False
                    print(i,word1,word2)
                    mang[i] = mang[i].replace(j,word1+' '+word2)

                else:
                    m+=1
    '''

f1.close()
f.close()

# f = open('All1.txt','w',encoding='utf-8')
# temp = 1
# for i in mang:
#     f.writelines(i+'\n')
#     print(temp)
#     temp+=1
# f.close()