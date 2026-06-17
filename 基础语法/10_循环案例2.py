""""猜数字游戏
1.系统随机生成一个随机数
import random  -->系统随机生成数字
random_number = random.randint( a: 1, b: 100)
2.用户根据提示猜数字，并将所猜的数字输入系统
3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4.如果猜对，系统自动退出，游戏结束
"""
import random
random_num = random.randint(1,100)
n = 6
while n > 0:
    num = int(input("请输入一个随机数: "))

    if num > random_num:
        print("您输入的数字大了")
    elif num < random_num:
        print("您输入的数字小了")
    else:
        print("恭喜你,答对了!!")
        break

    n -= 1
    print(f"剩余次数还剩:{n} ")
if n == 0:
    print("BOOM，次数用完了！")

print("随机生成的数字是: ",random_num)



