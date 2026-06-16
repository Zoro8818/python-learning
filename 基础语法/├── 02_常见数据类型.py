# # 常见数据类型 ----->  type() 获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))  # str
#
# print(type(20))  # int
# print(type(3.14))  # float
# print(type(True))  #bool
# print(type(False)) #bool
# print(type(None)) #NoneType
#
# num = -200
# print(type(num))  # int
# # 常见数据类型 --->  isinstance(数据, 类型) -->bool值 --> 判断数值是否是指定的类型, 如果是: True, 否则: False
# print(isinstance(num, int)) #True
# print(isinstance(num, bool)) #False
# print(isinstance(num, str)) #False
#
#
#
# 字符串
# 定义字符串的三种方式
# s1 = "Hello"  # 双引号
# s2 = "Python" # 单引号
# s3 = """
# Hello:
#     欢迎大家进入到Zoro的课堂学习魔兽知识!
#     大家记得一键三连~~
# """  # 三引号
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))

# 定义字符串 ---> It's very good
# 转义字符 \' \" \n=换行 \t=Tab 缩进
# msg = 'It\'s very good'
# print(msg)
#
# msg2 = "It's very good"
# print(msg2)
#
# msg3 = "Hello 的意思是 \"你好\""
# print(msg3)
#
# msg4 = 'Hello 的意思是 "你好"'
# print(msg4)
#
# print("\t欢迎大家进入到Zoro的课堂学习魔兽知识!\n\t大家记得一键三连~~")

# 字符串拼接
# s1 = "人生苦短" "我玩魔兽" ", OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我玩魔兽"
# print("女帝大人说:" + msg1 +" , " + msg2)
# print("女帝大人说:" + msg1 + "," +msg2)
#案例
# name = "郑平"
# name1 = "胡洋"
# name2 = "泽希"
# age = 38
# age1 = 38
# age2 = 13
# pro = "电子游戏"
# pro1 = "传统设计"
# pro2 = "中国舞"
# hobby = "Python和魔兽世界"
# hobby1 = "魔兽世界"
# hobby2 = "传统舞蹈,各种吃吃吃和三角洲"
# print("大家好,我是" + name + ",这是我的宝贝老婆和儿子,他们分别是"+ name1 +"和"+ name2+",今年我"+ str(age)+ ",我老婆也是"+ str(age1) +",\n我们俩共同的爱好是"+ hobby1 +",我们的儿子今年"+ str(age2) + ",他的爱好是"+ hobby2+ ",\n今年是他考上北舞的第一年,他学习的专业是"+ pro2 + ",愿他前程似锦,早日当上首席")

##字符串格式化 ---> 方式一: %s 占位符
# name = "郑平"
# age = 38
# pro = "电子竞技"
# hobby = "Python和魔兽世界"
# print("大家好,我是 %s,今年 %s 岁,学习的专业是 %s , 爱好 %s" %(name,age,pro,hobby))

#字符串格式化 ---> 方式二: f"....{字符串/表达式}....." 推荐方式!!
# name = "郑平"
# age = 38
# pro = "电子竞技"
# hobby = "Python和魔兽世界"
# print(f"大家好,我是 {name},今年 {age} 岁,学习的专业是 {pro} , 爱好 {hobby}" )
#
# name = "泽希"
# age = 13
# pro = "中国舞"
# hobby = "跳舞,魔兽世界和三角洲"
# print(f"大家好,我是 {name},今年 {age}岁, 学习的专业是 {pro}, 爱好是 {hobby}")



