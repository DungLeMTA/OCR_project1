import json

f = open('./0916_DataSamples2Label/labels.json','r',encoding ='utf-8')

str1 = f.read()
mang_data = str1.split('"')
mang=[]
for i in range(3,len(mang_data)-1,4):
    mang.append(mang_data[i])
f.close()

# f = open('img.txt','w',encoding ='utf-8')
# for i in mang:
#     f.writelines(i+'\n')
# f.close()


f = open('labels1.json', 'w', encoding='utf-8')

f.writelines('{\n')

# f1 = open('img.txt','r',encoding='utf-8')
#
# count=1
# str1 = f1.read()
# mang_data = str1.split('\n')
count=1
for i in mang:
    a = str(count)
    if count<10: a='0000'+a
    elif count<100: a='000'+a
    elif count<1000: a='00'+a
    elif count<10000: a='0'+a

    if count == 100:
        f.writelines('  "' + a + '.png": "' + i.strip() + '"\n')
    else:
        f.writelines('  "'+a+'.png": "'+i.strip()+'",\n')

    count += 1
# f1.close()
f.writelines('}')
f.close()