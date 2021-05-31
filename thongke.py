import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(1,21):
    x.append(i)
    y.append(0)
f = open('All.txt', 'r', encoding='utf-8')
str = f.read()
mang_data = str.split('\n')
f.close()

plt.title('Biểu đồ phân bố')
plt.xlabel('Số từ')
plt.ylabel('Số lượng câu')

temp = 0

for i in range(0, len(mang_data) - 1):
    a = mang_data[i].strip().split(' ')
    # try:
    # if len(a) >= 20:
    #     y[len(y)-1]+=1
    # else:
    try:
        y[len(a)-1] += 1
    except:
        print(i+1)
    # except:
    #     print(i+1)
    #     temp+=1

print('Có: ',temp)
plt.bar(x, y)
plt.plot(x, y, color='red',linestyle='dashed')
print(y)
plt.show()


# anim = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=True)
#
# anim.save('vi-du-2.gif', writer='imagemagick')
