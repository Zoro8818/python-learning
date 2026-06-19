# 给你一个成绩列表：
# score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71, 60, 85]
# 要求统计：
#
# 优秀人数：成绩 >= 85
# 及格人数：60 <= 成绩 < 85
# 不及格人数：成绩 < 60
# 最高分
# 最低分
# 平均分

score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71, 60, 85]
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

print("优秀人数：", excellent_count)
print("及格人数: ", pass_count)
print("不及格人数: ", fail_count)
print("最高分为: ", max(score_list))
print("最低分为: ", min(score_list))
print("平均分为: ", sum(score_list) / len(score_list))

"""
题目 2：筛选偶数并求和
要求：

找出所有偶数，放入 even_list
统计偶数个数
计算所有偶数的总和
"""
count = 0
total = 0
num_list = [12, 55, 44, 68, 71, 64, 1, 34, 57, 91, 592]
even_list = [i for i in num_list if i % 2 == 0]

#遍历偶数列表,统计个数和总和
for i in even_list:
    total += i  #求偶数总和
    count += 1  #求个数

print("偶数列表为: ", even_list)
print("偶数个数为: ", count)
print("偶数总和为: ", total)


# 题目 3：找出大于平均分的学生成绩
# 要求：
#
# 先计算平均分
# 找出所有大于平均分的成绩
# 放入新列表 new_list

avg_list = [88, 76, 92, 65, 100, 43, 59, 71]
avg_list1 = sum(score_list) / len(score_list)
print("平均为为: ", avg_list1)

new_list = []

for score in score_list:
    if score > avg_list1:
        new_list.append(score)

print("大于平均分的为: ", new_list)


# 题目 4：合并三个列表并去重
# 要求：
#
# 合并三个列表
# 去除重复元素
# 保留原来的顺序

list1 = ['A', 'B', 'C', 'D', 'E']
list2 = ['C', 'D', 'F', 'G']
list3 = ['A', 'H', 'I', 'F']
new_list = list1 + list2 + list3
print("合并后列表为: ", new_list)
result_list = []

for i in new_list:
    if i not in result_list:
        result_list.append(i)

print("去除重复元素: ", result_list)


# 题目 5：购物金额统计
# 要求统计：
#
# 总消费金额
# 消费次数
# 平均消费金额
# 大于等于 300 的消费有几次

money_list = [120, 80, 560, 310, 45, 700, 260, 99]
count = 0
total = 0
big_count = 0

for money in money_list:
    count += 1
    total += money
    if money >= 300:
        big_count += 1

avg_money = sum(money_list) / len(money_list)

print("总消费金额: ", total)
print("消费次数为: ", count)
print("平均消费金额为: ", avg_money)
print("大于等于 300 的消费有: ", big_count)


# 题目 6：猜数字升级版
# 设定答案：
# answer = 36
# 要求用户最多猜 5 次。
# 规则：
# 如果猜大了：
# 猜大了
# 如果猜小了：
# 猜小了
# 如果猜对了：
# 猜对了，一共用了 X 次
# 如果 5 次都没猜对：
# 机会用完，正确答案是 36

answer = 36
count = 0

while count < 5:          #while循环
    guess = int(input("请输入您猜的有效数字: "))
    count += 1

    if guess == answer:
        print(f"恭喜猜对了,一共用了{count}次")
        break
    elif guess > answer:
        print("猜大了")
    else:
        print("猜小了")
else:
    print("机会用完，正确答案是 36")



# 题目 7：账号登录系统
# 要求：
#
# 用户最多登录 5 次
# 账号密码正确，输出：
# 登录成功
# 账号或密码错误，输出：
# 账号或密码错误
# 5 次失败后输出：
# 错误次数过多，账号已锁定

users = {
    "admin": "123456",
    "zoro": "888888",
    "python": "666666"
}

count = 0

while count < 5:
    username = input("请输入账号: ")
    password = input("请输入密码: ")

    if username in users and users[username] == password:
        print("登录成功")
        break
    else:
        count = count + 1
        print("账号或密码错误")
        print(f"剩余次数为: {5 - count}次")

else:
    print("错误次数过多，账号已锁定")


# 题目 8：学生成绩字典统计
# 要求统计：
#
# 输出所有学生姓名和成绩
# 统计及格人数，成绩 >= 60
# 统计不及格人数，成绩 < 60
# 找出最高分

students = {
    "张三": 88,
    "李四": 59,
    "王五": 76,
    "赵六": 92,
    "小明": 45,
    "小红": 100
}
pass_count = 0
fail_count = 0
for name, score in students.items():
    print(f"{name}：{score}")
    if score >= 60:
        pass_count += 1
    elif score < 60:
        fail_count += 1

print(f"及格人数为: {pass_count}个, 不及格人数为: {fail_count} 个")
print("最高分：", max(students.values()))