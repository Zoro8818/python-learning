#第 1 题：统计字符串长度,要求输出字符串长度。-->len() 只统计“有几个”，不负责求和。
s = "Python学习真有意思"
len_str = len(s)
print(len_str)

#第 2 题：统计某个字符出现次数,要求统计字符 "a" 出现了多少次。-->统计个数 次数 -->count
s = "abacadaeafag"
#方法1
count = 0

for i in s:
    if i == "a":
        count += 1
print(count)

#方法2
s = "abacadaeafag"

count = s.count("a")

print(count)
#第 3 题：判断字符串里是否包含某个关键词, 要求判断 text 里面是否包含 keyword。-->判断某个内容是否在字符串里，用 in
text = "我正在学习Python基础语法"
keyword = "Python"
if keyword in text:
    print("包含")
else:
    print("不包含")

#第 4 题：去掉字符串前后空格,要求去掉字符串前后的空格。-->strip() 只去掉前后空格，不会去掉中间空格
name = "   zhangsan   "
new_name = name.strip()
print(new_name)

#第 5 题：用 split() 把字符串变成列表,要求用英文逗号 , 分割字符串，变成列表。-->用什么符号分割，就把什么符号放进 split() 里面

names = "张三,李四,王五"
new_names = names.split(",")
print(new_names)

#有一个姓名字符串 "张三,李四,王五"，拆成列表后统计人数。
name = "张三,李四,王五"
name_list = name.split(",")
print("列表为:",name_list)
count = len(name_list)
print("人数为:",count)

#找出所有包含 "Python" 的句子，放进一个新列表，最后输出新列表。-->包含用in
sentence_list = [
    "我正在学习Python基础语法",
    "今天练习字符串和列表",
    "Python可以处理Excel",
    "明天继续学习函数"
]
python_list = []

for sentence in sentence_list:
    if "Python" in sentence:    #-->如果当前句子里包含"Python" sentence=句子
        python_list.append(sentence)

print(python_list)


#第 3 题：去掉商品名称前后空格，生成新列表.  goods=商品 货物
goods_list = ["  苹果  ", " 香蕉", "橙子  ", "  牛奶"]
new_goods_list = []
for goods in goods_list:  #-->循环处理每个goods
    new_goods = goods.strip()  #-->strip() 去掉goods前后空格,不会去掉中间空格。
    new_goods_list.append(new_goods)  #--> 放入新的列表

print(new_goods_list)

#然后做一个小工具雏形：


goods_list = ["  苹果  ", " 香蕉", "橙子  ", "  牛奶", "  牛肉", "玉米  ", "洗衣粉  ", " 抱枕 "]
new_goods_list = []
for goods in goods_list:   #-->循环中每次拿到goods
     #处理：去掉前后空格
    new_goods = goods.strip()          #输入：带空格的商品列表
    # 把清洗后的商品名添加到新列表
    new_goods_list.append(new_goods)

#输出：干净的新商品列表
print("原始商品列表:", goods_list)
print("清洗后商品列表:", new_goods_list)




