# 获取键盘上输入的数据 --- input(...)
# name = input("请输入你的姓名: ")
# age = input("请输入你的年龄: ")
#
# print(f"您的姓名是 {name}, 您的年龄为 {age}")

# #案例 :银行卡ATM取款
# #总金额
# total = 10000
#
# #1 输入密码
# password = input("请输入你的取款密码: ")
# print(f"密码正确,{password}")
#
# #2 输入取款金额
# num = input("请输入你的取款金额: ")
#
# #3 计算余额并输出
# print(f"取款后您的银行卡余额为: {total - int(num)}")

#作业1
#需求: 根据用户输入的两个数字, 计算两个数之和, 并将其输出到控制台
# num = input("请输入你的数字: ")
# num1 = input("请输入你的数字: ")
# print(f"两个数字的和为: {int(num) + int(num1)}")

#作业2
#需求: 根据用户输入的6个数字, 计算6个数之和, 并将其输出到控制台
# num = input("请输入您的数字: ")
# num1 = input("请输入您的数字: ")
# num2 = input("请输入您的数字: ")
# num3 = input("请输入您的数字: ")
# num4 = input("请输入您的数字: ")
# num5 = input("请输入您的数字: ")
# print(f"计算结果为: {int(num1)+int(num2)-int(num3)*int(num4)/int(num5)}")

#Python小游戏
#1幸运数字
# name = input("请输入您的名字: ")
#
# num = int(input("请输入一个你喜欢的整数:"))
#
# lucky_num = num * 8 + 6
#
# print(f"名字:{name}, 你今天的幸运数字为:{lucky_num},今天也要努力学习哦")

#2 自我介绍
#1. 让用户输入姓名
# #2. 让用户输入年龄
#3. 让用户输入所在城市
#4. 让用户输入一个爱好
#5. 最后生成一段完整的自我介绍
# 案例:
#大家好，我叫张三，今年18岁，来自北京。
#我的爱好是打篮球。
#明年我就19岁了，希望自己继续努力学习 Python。

name = "曦哥"
age = 25
city = "北京"
hobby = "Python和魔兽世界"
print(f"大家好,我是{name},今年{age},来自{city},我的爱好是{hobby},明年我就要{age + 1}岁了,\n希望自己努力学好Python,赚更多的钱钱,让老婆和孩子过上幸福的生活")
