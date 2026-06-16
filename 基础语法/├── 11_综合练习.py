# #需求1:将1-1000之间(含1000)所有的5的倍数的数字累加起来。
#
# total = 0
# for i in range(5,1001,5):
#     total += i
#
# print(f"1~1000所有的5的倍数的数字累加的和为: {total}")
#
# #需求2:统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
# s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# count = s.count("a") + s.count("k")
#
# print(count)

# #① 判断奇偶:输入一个数，判断是奇数还是偶数
# num = int(input("请输入一个整数: "))
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
#
# #② 判断成绩等级: ≥90 优秀, ≥80 良好, ≥60 及格, <60 不及格
# score = float(input("请输入你的分数: "))
#
# if score >= 90:  #90-100为优秀
#     print("优秀")
# elif score >= 80:   #80-89为良好
#     print("良好")
# elif score >= 60:   #60-79为及格
#     print("及格")
# else:
#     print("不及格")
#
#
# #③ 判断是否成年:输入年龄，判断是否成年（18岁）
# age = int(input("请输入你的年龄: "))
#
# if age < 0 or age > 120:
#     print("输入的信息有误")
# elif age >= 18:
#     print("已成年")
# else:
#     print("未成年")
#
# #登录系统（无限循环）:, admin / 123456 登录成功退出, 否则继续输入
#
# while True:
#     username = input("请输入账号: ")
#     password = input("请输入密码: ")
#
#     if username == "admin" and password == "123456":
#         print("登录成功")
#         break
#     else:
#         print("继续输入")
#
# #登录系统（5次）:, admin / 123456 登录成功退出, 错误5次后提示“锁定”
# count = 5
# while count > 0:
#     username = input("请输入账号: ")
#     password = input("请输入密码: ")
#
#     if username == "admin" and password == "123456":
#         print("登录成功")
#         break
#     count -= 1
# if count == 0:
#     print("锁定")


# #⑥ 猜数字（简单版）:系统随机1~20, 用户一直猜，直到猜对
# import random
# random_num = random.randint(1, 20)
# while True:
#     num = int(input("请输入1-20间的数字: "))
#     if num < random_num:
#         print("输入的数字太小了")
#     elif num > random_num:
#         print("输入的数字太大了")
#     else:
#         print("恭喜你答对了")
#         break
#第三组：for循环（计数）, ⑦ 1~100求和
total = 0

for i in range(1,101):
    total += i

print(total)

#1~100偶数求和
total = 0

for i in range(1,101):
    if i % 2 == 0:
        total += i

print(total)

#求 1~100 中所有能被 3 整除的数之和
total = 0

for i in range(3 , 101, 3):
    total += i

print(total)

#统计1~100有多少个5的倍数
count = 0

for i in range(5 , 101, 5):
    count += 1

print(count)

#第四组：字符串（统计） 统计字符串中 a 的个数
s = "abacadaeafag"
count = 0

for a in s:
    if a == "a":
        count += 1

print(count)

#统计 a 和 b 的总个数
s = "abacadaeafag"

count = 0
for a in s:
    if a == "a" or a == "b":
        count += 1

print(count)

# 第五组：嵌套循环（图形） 输入3行5列，输出
m = int(input("请输入长方形的长: "))
n = int(input("请输入长方形的宽: "))

for i in range(n):
    for j in range(m):
        print("*", end="")
    print()

#数字三角形
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")

    print()

#打印国际象棋棋盘
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end="  ")
    print()

#第六组：综合题（提升）猜数字 + 次数限制, 5次机会, 猜对结束, 猜错提示大小
import random
random_num = random.randint(1, 100)
n = 5

while n > 0:
    num = int(input("请输入数字: "))
    if num > random_num:
        print("输入的数字太大了")
    elif num < random_num:
        print("输入的数字太小了")
    else:
        print("恭喜你答对了")
        break

    n -= 1
    print(f"剩余次数还剩:{n} ")
if n == 0:
    print("BOOM，次数用完了！")

print("随机生成的数字是: ",random_num)

#users = {"admin": "123"}
users = {
    "admin": "123",
    "zhangsan": "123465",
    "xige": "1858",
}
while True:
    username = input("请输入你的账号:")
    password = input("请输入你的密码:")

    if username == "" or password == "":
        print("用户名或密码错误，请重新输入")
        continue

    if username in users and users[username] == password:
        print("恭喜登录")
        break
    else:
        print("用户名或密码错误，请重新输入!")



