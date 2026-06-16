#案例: 根据输入的长方形的长m, 宽n, 打印一个长方形. 用*表示

m = int(input("请输入长方形的长: "))
n = int(input("请输入长方形的宽: "))

for j in range(n):
    for i in range(m):
        print("*", end="  ")
    print()  #-->表示换行

#案例2: 做一个99乘法表
for i in range(1,10):  #外循环 - 控制行
    for j in range(1,i+1):  #内循环 - 控制列
        print(f"{i} x {j} = {i*j}",end="\t")
    print()

#需求1:根据输入的直角边的边长，打印等腰直角三角形 (如下为直角边为5的等腰直角三角形)
for i in range(6):   #外循环 - 控制行
    for j in range(i):   #内循环- 控制列
        print("*", end="  ")
    print()  #表示换行

#需求2:根据输入的数字，打印对应的数字金字塔 1-6
for i in range(1,7):   #外循环 - 控制行
    for j in range(1,i+1):   #外循环 - -控制列
        print(j, end="  ")
    print()
#需求3:打印国际象棋棋盘
for i in range(8):  #外循环 - 控制行  i=行
    for j in range(8):   #外旋环 - -控制列 j=列
        if(i + j) % 2 == 0:
            print("■", end="  ")
        else:
            print("□", end="  ")
    print()