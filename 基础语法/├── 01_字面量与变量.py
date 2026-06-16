# # 字面量的写法
# print("100") # 整数(int)
# print("3.14") # 小数/浮点数(float)
# print(True) # 布尔(bool)
# print(False) # 布尔(bool)
# print("Hello python") # 字符串(str)  所有用加引号引起来的都是字符串!!!
# print("--------------------------") # 字符串(str)  所有用加引号引起来的都是字符串!!!
# print(None) # 空值(NoneType)
#
# # 布尔类型本质也是整数类型(True 表示 1;False 表示 0)
# print(True + 1)# 表示2
# print(False - 1)# 表示-1
#
#
# # 变量-----> Python是动态类型语言,一个变量是可以存储不同类型的数值(但是开发项目中,推荐变量只存储一种类型的变量)
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = True
# print(num)
#
# num = "Ok"
# print(num)
#
# # 案例  基础量为20.7w  每月新增量为50w  求输出未来两个月的播放总量
# base = 20.7 #基础量
# incr = 50  #每月新增量
# print("未来第一个月的播放量: ", base + incr)
# print("未来第二的播放量: ", base + incr +incr)
#
# # 案例 - 升级: 一次性可以定义多个变量
# base,incr = 20.7,50
# print("未来第一个月的播放量: ", base + incr)
# print("未来第二的播放量: ", base + incr +incr)


# 作业:a=100 b=200 c=300 现需要将这三个变量值进行互换,将a,b,c的值分别赋值给c,a,b,
a = 100
b = 200
c = 300

d = a # d = 100
e = b # e = 200
f = c # f = 300

c = d # c = 100
a = e # e = 200
b = f # b = 300

print(c, a, b)

