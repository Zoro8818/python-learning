#1: 题型：判断题 + 计数题 + 固定循环题 优秀人数：成绩 >= 85, 及格人数：60 <= 成绩 < 85, 不及格人数：成绩 < 60

score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71]
excellent_count = 0
pass_count = 0
fail_count = 0
for score in score_list:
    if score >= 85:
        excellent_count += 1
    elif score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("优秀人数: ", excellent_count)
print("及格人数: ", pass_count)
print("不及格人数: ", fail_count)

""" 
题型：固定循环题 + 累加题 + 计数题
题目 2：1 到 100 中，能被 3 整除的数字求和并计数
要求：
找出 1~100 中所有能被 3 整除的数字。
统计：

1. 一共有多少个
2. 它们的总和是多少
"""
count = 0  #求个数
total = 0  #求总和
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
        total += i

print(f"一共有: {count}个, 总和为: {total}")


"""
题目 3：猜数字，最多 5 次机会

题型：综合循环题 + while + if + break

设定一个答案：18   
"""
answer = 18
count = 0

while count < 5:
    guess = int(input("请输入您猜的有效数字: "))
    count += 1

    if guess == answer:
        print("恭喜你答对了")
        break
    elif guess > answer:
        print("您输入的数字太大了")
    else:
        print("您输入的数字太小了")

    print(f"还剩: {5 - count}次")
else:
    print("机会用完")


"""
题目 4：打印数字三角形

题型：图形题 + 嵌套 for 循环

要求打印：

1
12
123
1234
12345
"""
for i in range(1, 6):  #-->外循环,控制行
    for j in range(1, i + 1):   #-->内循环,控制列
        print(j , end="")
    print()

"""
题目 5：账号密码登录系统

题型：字典题 + while + if + break + 5 次机会

"""
users = {
    "admin": "123456",
    "zoro": "888888",
    "python": "666666"
}

count = 0

while count < 5:
    username = input("请输入账号：")
    password = input("请输入密码：")

    if username in users and password == users[username]:
        print("欢迎登录")
        break
    else:
        count += 1
        print("账号或密码错误")
        print(f"还剩: {5 - count}次")
else:
    print("机会用完")

