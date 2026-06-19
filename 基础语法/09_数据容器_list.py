#列表操作
#定义列表_ list
s = [56, 44, 97, 456, 77, 66, 77, "A", "Hello"]

print(type(s))

#访问列表元素
#获取
print(s[0])    #-->正向索引,从0开始
print(s[-2])    #-->反向索引,从-1开始

print(s[-1])
print(s[5])

#修改
s[7] = "ABCD"
print(s)


#注意:如果指定的索引, 超出范围, 将会报错 IndexError: list index out of range
#s[10]

#删除
del s[7]
print(s)

#遍历
for item in s:
    print(item)

#列表的切片
#定义列表
#切片操作: s[开始索引,结束索引.步长]
s = ["A", "H", "I", "G", "K", "O", "W", "R", "T", "N", "G", "K", "A", "H", "G", "G"]
print(s[0:6:1])
print(s[:6:1])
print(s[:6])   #--默认可以不写,但是开始的冒号不能省略

print(s[1:-2:3])


# ------------------------------------------ 列表_list_常用方法 -------------------------------------------------------------
# 定义列表
s = [86, 18, 75, 15, 2, 2 , 66, 74, 34, 39, 18, 1]
print(s)

# append(): --> 在列表尾部追加元素
s.append(99)
print(s)

# instert(): -->在指定索引之前, 插入元素
s.insert(1, 88)
print(s)

# remove():   -->移除列表中第一个匹配到的元素
s.remove(2)
print(s)

# pop():    -->删除列表中指定索引位置的元素并返回(如果未指定,默认删除最后一个)
e = s.pop(3)
print(e)

e = s.pop()
print(e)


#sort():   -->排序 默认从小到大
s.sort()
print(s)


#reverse():  -->反转列表元素
s.reverse()
print(s)


#------------------------------------------ 列表_list_常用方法 -------------------------------------------------------------
#案例1 将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值, 最大值和平均值

#1. 定义列表
num_list = []

#2. 将用户输入的10个数字存入列表
for i in range(10):
    num = int(input("请输入十个有效数字: "))
    num_list.append(num)    #-->从列表的尾部追加元素

print(num_list)
#3. 将列表中的数字进行排序
num_list.sort()
print("排序后的数字为", num_list)
#4. 输出其中的最小值, 最大值和平均值  sum() 表示求和 len() 表示 获取元素的个数(列表的长度)
print("最小值:", num_list[0])
print("最大值:", num_list[-1])
print("平均值:", sum(num_list)/len(num_list))


#案例2 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
# 定义列表
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#1. 合并列表
num_list = num_list1 + num_list2
print("合并后的列表：", num_list)
#2. 去除列表中的重复元素
new_list = []

for num in num_list:
    if num not in new_list:
        new_list.append(num)

print("去重后的数字为: ", new_list)


#案例: 1.生成1-20的平方列表。
#方式1:
num_list =[]
for i in range(1,21):
    num_list.append(i**2)

print(num_list)

#方式2: 列表推导式1--->就是按照一定的规则快速生成一个列表的方法-->语法格式:[表达式 for 变量 in 可迭代对象]
num_list1 = [i**2 for i in range(1,21)]

print(num_list1)



#案例2.从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
#列表推导式2--->就是按照一定的规则快速生成一个列表的方法-->语法格式:[表达式 for 变量 in 可迭代对象 if 条件]
num_list = [12, 55, 44, 68, 71, 64, 1, 34, 57, 91, 592]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)

#方法2
num_list = [12, 55, 44, 68, 71, 64, 1, 34, 57, 91, 592]

new_list = []

for i in num_list:
    if i % 2 == 0:
        new_list.append(i ** 2)

print(new_list)


#作业1: 将如下多个列表合并为一个列表，并去重重复元素，排好序(升序)后输出到控制台。
# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
new_list = list1 + list2 + list3

print("新的列表为: ",new_list)

new_list1 = []
for i in new_list:
    if i not in new_list1:
        new_list1.append(i)

print(new_list1)


#作业2: 将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
new_list = [i**2 for i in range(1, 31) if i%3 == 0 or i%5 == 0]

print(new_list)

#作业3:3.将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
new_list = [i for i in list1 if i >= 0]

print(new_list)
