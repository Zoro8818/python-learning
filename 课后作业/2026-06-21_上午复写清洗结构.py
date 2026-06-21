#1. 输出：
# 原始列表
# 清洗后客户列表
# 有效客户数量
# 无效客户数量
customer_text = " 张三, 李四, , 王五, , 赵六, 钱七 "
customer_list = customer_text.split(",")

clean_customer_list = []
invalid_count = 0

for customer in customer_list:
    clean_customer = customer.strip()

    if clean_customer != "":
        clean_customer_list.append(clean_customer)

    else:
        invalid_count += 1

print("原始列表:", customer_list)
print("清洗后客户列表:", clean_customer_list)
print("有效客户数量:", len(clean_customer_list))
print("无效客户数量:", invalid_count)

# 注释:输入是什么：customer_text
# 处理过程是什么：split() 拆分成原始列表, for 遍历,strip()去客户的前后空格,if 判断是否为有效客户,
# 成功: append 添加进clean_customer_list,否则 invalid_count += 1
# 输出结果是什么：customer_list, clean_customer_list, len(clean_customer_list), invalid_count


#2. 输出：
# 原始列表
# 清洗后订单金额列表
# 有效订单数量
# 无效数量
# 大额订单列表，金额 >= 100
# 大额订单数量
# 普通订单数量
order_text = " 99.9, 200, , 35.5, 500, , 120.8, 60 "
order_list = order_text.split(",")

clean_order_list = []
large_order_list = []
invalid_count = 0
normal_count = 0


for order in order_list:
    clean_order = order.strip()

    if clean_order != "":
        order_amount = float(clean_order)
        clean_order_list.append(order_amount)

        if order_amount >= 100:
            large_order_list.append(order_amount)
        else:
            normal_count += 1

    else:
        invalid_count += 1

print("原始列表:",order_list)
print("清洗后订单金额列表:",clean_order_list)

print("有效订单数量:", len(clean_order_list))
print("无效订单数量:", invalid_count)

print("大额订单列表:", large_order_list)
print("大额订单数量:", len(large_order_list))
print("普通订单数量:", normal_count)

# 输入是什么：order_text
# 处理过程是什么：split拆开成原始列表,for遍历,strip 去遍历后订单的前后空格, if判断是否为有效订单,失败 invalid_count += 1
# 判断成功append添加订单进clean_order_list, 判断订单金额>= 100,成功 append添加订单进large_order_list,否则normal_count += 1
# 输出结果是什么：order_list, clean_order_list,len(clean_order_list), invalid_count, large_order_list,
# len(large_order_list), normal_count