#1
name = input("请输入姓名：")
age = int(input("请输入年龄："))

print(name + "今年" + str(age) + "岁")
#注释:输入姓名,年龄  输出:XXX今年XX岁的格式

#2
price = float(input("请输入商品单价："))
count = int(input("请输入购买数量："))

total = price * count
print("商品总价为:" + str(total) + "元")
#注释:输入商品单价和数量,输出商品总价,处理总价=单价*数量

#3
price = float(input("请输入商品单价："))
count = int(input("请输入购买数量："))

total = price * count
print("商品总价为:" + str(total) + "元")
#注释:输入商品单价和数量,输出商品总价,处理总价=单价*数量
#
total_score = float(input("请输入总分: "))
people_count = int(input("请输入人数: "))

avg_score = total_score / people_count

print("平均分: " + str(avg_score) + "分")
#注释:输入总分和人数, 输出平均分
#
score = float(input("请输入分数: "))
if score >= 60:
    print("及格")
else:
    print("不及格")
##注释:输入分数,判断>= 60为及格,否则不及格,输出及格或不及格
#
age = int(input("请输入年龄: "))
if age >= 18:
    print("成年")
else:
    print("未成年")
##注释:输入年龄,判断>= 18为成年,否则未成年,输出成年或未成年
#
goods_count = int(input("请输入商品数量: "))
if goods_count > 3:
    print("库存充足")
else:
    print("库存不足")

##注释:输入商品数量,判断>3 为库存充足,否则为库存不足

#
products = ["苹果", "香蕉", "牛奶", "面包"]
for product in products:
    print(product)

#注释:输入"苹果", "香蕉", "牛奶", "面包",遍历列表里每个商品,输出每个商品名称

#
score_list = [88, 59, 76, 92, 45, 100, 67, 60, 4, 51]
greater_than_60_list = []

for score in score_list:
    if score > 60:
        greater_than_60_list.append(score)

pass_count = len(greater_than_60_list)

print("大于60的分数:", greater_than_60_list)
print("及格人数: ", pass_count)
#注释:输入88, 59, 76, 92, 45, 100, 67, 60, 4, 51,遍历列表里每个分数,判断是否> 60,符合要求添加到新列表,
# len()统计及格人数,输出及格人数和新列表

price = float(input("请输入商品单价："))
count = int(input("请输入购买数量："))

total = price * count
print("商品总价为:", total, "元")

