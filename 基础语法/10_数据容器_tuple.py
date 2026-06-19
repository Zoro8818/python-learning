# 元组的基本操作 -- tuple-->元素可以重复,有序,不能修改
#定义
t1 = (80, 90, 48, 654, 4654, 1, 80, 11)

print(t1)
print(type(t1))

#索引访问
print(t1[0])
print(t1[-1])

#切片
print(t1[0:5:1])


#count() 统计元素个数
print(t1.count(80))

#index() 获取元素的索引(第一个元素的位置)
print(t1.index(80))


#注意点:如果定义单元素的元组,单个元素之后需要加上逗号,比如(1,)
t2 = ()
print(t2)
print(type(t2))


t3 = (1,)
print(t3)
print(type(t3))

#
info = ("张三", 18, "销售")
print(info[0])
print(len(info))

for item in info:
    print(item)

name, age, department = info
print(name, age, department)

#
text = "  apple,banana,orange  "
text = text.strip()
goods_list = text.split(",")
print(goods_list)

new_goods_list = []

for goods in goods_list:
    new_goods_list.append(goods)

print(new_goods_list)

#
user_info = ("张三", "销售", 5000)
name, department, salary = user_info
print(name, department, salary)

user_info = ("张三", "销售", 5000)
n, d, s= user_info
print(n, d, s)

