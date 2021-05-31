
f = open('All.txt','r',encoding ='utf-8')

str1 = f.read()
mang_data = str1.split('\n')
mang=[]
for i in range(0,len(mang_data)):
    mang.append(mang_data[i])
f.close()
print(len(mang))
f = open('image1000K/validation.txt', 'w', encoding='utf-8')

count=1000000
for i in range(1000000,1050001):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a

    f.writelines('image/' + a + '.png\t' + mang[i].strip() + '\n')

    count += 1
# f1.close()
f.close()