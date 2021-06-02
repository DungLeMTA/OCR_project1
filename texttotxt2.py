f = open('Test.txt','r',encoding ='utf-8')

str1 = f.read()
mang_data = str1.split('\n')
mang=[]
for i in range(0,len(mang_data)):
    mang.append(mang_data[i])
f.close()
print(len(mang))
Tong = len(mang)
count_Times = 0.4
count_Tahoma = 0.2
count_Segoe = 0.2
count_Hel = 0.1
count_Open = 0.1

f = open('All_TIMES.txt', 'w', encoding='utf-8')
b=0
count = 1
for i in range(0,int(Tong*count_Times)):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a
    if i != int(b + Tong * count_Times) - 1:
        f.writelines(mang[i].strip() + '\n')
    else:
        f.writelines(mang[i].strip())
    count += 1
f.close()
b= int(Tong*count_Times)

f = open('All_TAHOMA.txt', 'w', encoding='utf-8')
for i in range(b,int(b+Tong*count_Tahoma)):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a
    if i != int(b + Tong * count_Tahoma) - 1:
        f.writelines(mang[i].strip() + '\n')
    else:
        f.writelines(mang[i].strip())
    count += 1
f.close()

b += int(Tong*count_Tahoma)
f = open('All_SEGOEUI.txt', 'w', encoding='utf-8')
for i in range(b,int(b+Tong*count_Segoe)):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a
    if i != int(b+Tong*count_Segoe)-1:
        f.writelines(mang[i].strip() + '\n')
    else:
        f.writelines(mang[i].strip())
    count += 1
f.close()

b += int(Tong*count_Segoe)
f = open('All_HELVETICA.txt', 'w', encoding='utf-8')
for i in range(b,int(b+Tong*count_Hel)):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a
    if i != int(b + Tong * count_Hel) - 1:
        f.writelines(mang[i].strip() + '\n')
    else:
        f.writelines(mang[i].strip())
    count += 1
f.close()

b += int(Tong*count_Hel)
f = open('All_OPEN.txt', 'w', encoding='utf-8')
for i in range(b,Tong):
    a = str(count)
    if   count<10: a='0000000'+a
    elif count<100: a='000000'+a
    elif count<1000: a='00000'+a
    elif count<10000: a='0000'+a
    elif count<100000: a='000'+a
    elif count<1000000: a='00'+a
    elif count<10000000: a='0'+a
    if i != Tong - 1:
        f.writelines(mang[i].strip() + '\n')
    else:
        f.writelines(mang[i].strip())
    count += 1
f.close()
#
# b += int(Tong*count_Arial)
# f = open('All_SEGOEUI.txt', 'w', encoding='utf-8')
# for i in range(b,int(b+Tong*count_Segoe)):
#     a = str(count)
#     if   count<10: a='0000000'+a
#     elif count<100: a='000000'+a
#     elif count<1000: a='00000'+a
#     elif count<10000: a='0000'+a
#     elif count<100000: a='000'+a
#     elif count<1000000: a='00'+a
#     elif count<10000000: a='0'+a
#     f.writelines(mang[i].strip() + '\n')
#     count += 1
# f.close()
#
# b += int(Tong*count_Segoe)
# f = open('All_CALIBRI.txt', 'w', encoding='utf-8')
# for i in range(b,int(b+Tong*count_Cali)):
#     a = str(count)
#     if   count<10: a='0000000'+a
#     elif count<100: a='000000'+a
#     elif count<1000: a='00000'+a
#     elif count<10000: a='0000'+a
#     elif count<100000: a='000'+a
#     elif count<1000000: a='00'+a
#     elif count<10000000: a='0'+a
#     f.writelines(mang[i].strip() + '\n')
#     count += 1
# f.close()
#
# b += int(Tong*count_Cali)
# f = open('All_OPEN.txt', 'w', encoding='utf-8')
# for i in range(b,Tong):
#     a = str(count)
#     if   count<10: a='0000000'+a
#     elif count<100: a='000000'+a
#     elif count<1000: a='00000'+a
#     elif count<10000: a='0000'+a
#     elif count<100000: a='000'+a
#     elif count<1000000: a='00'+a
#     elif count<10000000: a='0'+a
#     f.writelines(mang[i].strip() + '\n')
#     count += 1
f.close()