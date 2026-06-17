#案例
#1 计算输入的三个整数的平均值
# x = int(input("请输入x的值: "))
# y = int(input("请输入y的值: "))
# z = int(input("请输入z的值: "))
# print(f"计算这三个整数的平均值为: {(x + y + z) / 3}")

#2 要求输入一个梯形的上底,下底,高, 然后计算梯形的面积
# a = float(input("请输入梯形上底a的值: "))
# b = float(input("请输入梯形下底b的值: "))
# h = float(input("请输入梯形高h的值: "))
# print(f"计算这个梯形的面积为: {(a + b) / 2 * h}")

#3 要求输入圆的半径, 然后计算圆的周长和面积 (周长: 2πr 面积: πr**2)
# r = float(input("请输入圆形的半径r的值: "))
# pi = 3.14
#
# c = 2 * pi * r
# s = pi * r ** 2
# print(f"圆的周长为: {c}")
# print(f"圆的面积为: {s}")

#4 身体质量指数BMI的计算BMI = 体重(kg) / 身高(m)**2)
# w = float(input("请输入你的体重(单位kg): "))
# h = float(input("请输入你的身高(单位m): "))
# bmi = w / h ** 2
# print(f"计算身体质量指数bmi为: {bmi}")

#0611晚间作业
#1单价= a, 数量= b, 总价= c
# a = float(input("输入商品单价(单位: 元): "))
# b = int(input("输入商品数量(单位: kg): "))
# c = a * b
# print(f"计算总价位: {c}元")

#2
# age = int(input("请输入你的年龄"))
# is_adult = age >= 18
# print(f"是否成年:{is_adult}")

#3
# num =int(input("请输入一个三位数: "))
# hundreds = num // 100  #百位:整除100
# tens = num // 10 % 10  #十位:先除10, 再除10取余
# ones = num % 10  #个位: 在直接对个位取余
#
# print(f"百位: {hundreds}")
# print(f"十位: {tens}")
# print(f"个位: {ones}")

#4
# time = float(input("请输入今天你的学习时间: "))
# is_qualified = 3 <= time <= 8
# print(f"今天学习时间是否达标: {is_qualified}")

#5
lucky_nums = int(input("请输入一个喜欢的整数: "))
lucky_nums1 = lucky_nums * 8 + 6
is_big = lucky_nums1 > 50
print(f"幸运数字是否大于50: {is_big}")
