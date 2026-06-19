#1. 用 split(",") 把字符串切成列表
#2. 用 for 循环遍历列表里的每个商品名
#3. 对每个商品名使用 strip() 去掉前后空格
#4. 用 append() 把清洗后的商品名保存到新列表
goods_text = "  苹果  , 香蕉,橙子  ,  牛奶, 牛肉 ,玉米  , 洗衣粉  , 抱枕 "

goods_list = goods_text.split(",")  #split(",") 把字符串切成列表
print("拆分后的原始列表:", goods_list)
new_goods_list = []

for goods in goods_list:       #遍历列表里的每个商品名
    #strip() 去掉前后空格 .append() 把清洗后的商品添加到新列表
    new_goods_list.append(goods.strip())

print(new_goods_list)  #输出最后结果

#2.要求：
#用 split(",") 把字符串切成列表。
#用 for 循环遍历每个客户姓名。
#用 strip() 去掉每个姓名前后的空格。
#用 append() 把清洗后的姓名保存到新列表。
#最后输出新列表。

customer_text = "  张三 , 李四,王五  ,  赵六, 钱七 ,孙八  "
customer_list = customer_text.split(",")
print("拆分后的原始列表:",customer_list) #split(",")把字符串切成列表
new_customer_list = []

for customer in customer_list:  #遍历列表里的每个姓名
    #strip() 去掉前后空格 .append() 把清洗后的姓名添加到新列表
    new_customer_list.append(customer.strip())

print(new_customer_list)


#3要求：
# 用 split(",") 把字符串切成列表。
# 用 for 遍历每个客户姓名。
# 用 strip() 去掉前后空格。
# 如果清洗后不是空字符串，才添加到新列表。
# 最后输出清洗后的客户列表。
customer_text = "  张三 , 李四, ,王五  ,  , 赵六, 钱七 ,   ,孙八  "
customer_list = customer_text.split(",")
print("拆分后的原始列表:", customer_list)    #split(",")把字符串切成列表

new_customer_list = []

for customer in customer_list:   #遍历列表里的每个姓名
    #strip() 去掉前后空格
    new_customer = customer.strip()
    #判断是否符合条件
    if new_customer != "":
        #append() 把清洗后的姓名添加到新列表
        new_customer_list.append(new_customer)

print("清洗后的客户列表:", new_customer_list)


