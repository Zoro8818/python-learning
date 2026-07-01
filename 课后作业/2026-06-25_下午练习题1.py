# 题目1:
valid_customer_list = ["张三", "李四", "钱七", "孙八", "周九", "吴十"]
valid_amount_list = [88.5, 120.0, 60.0, 0.0, 300.5, 72.0]

max_amount = valid_amount_list[0]
max_customer = valid_customer_list[0]

min_amount = valid_amount_list[0]
min_customer = valid_customer_list[0]

for i in range(len(valid_amount_list)):
    if valid_amount_list[i] > max_amount:
        max_amount = valid_amount_list[i]
        max_customer = valid_customer_list[i]

    if valid_amount_list[i] < min_amount:
        min_amount = valid_amount_list[i]
        min_customer = valid_customer_list[i]


print("最高金额客户:", max_customer)
print("最高金额:", max_amount)
print("最低金额客户:", min_customer)
print("最低金额:", min_amount)

# 题目2:

high_amount_list = [520.0, 300.5]
high_total_amount = 820.5

normal_amount_list = [88.5, 60.0, 72.0]
normal_total_amount = 220.5

low_amount_list = [0.0, 45.0]
low_total_amount = 45.0

if len(high_amount_list) > 0:
    high_avg_amount = high_total_amount / len(high_amount_list)
else:
    high_avg_amount = 0

if len(normal_amount_list) > 0:
    normal_avg_amount = normal_total_amount / len(normal_amount_list)
else:
    normal_avg_amount = 0

if len(low_amount_list) > 0:
    low_avg_amount = low_total_amount / len(low_amount_list)
else:
    low_avg_amount = 0


print("高订单平均金额:", round(high_avg_amount, 2))
print("普通订单平均金额:", round(normal_avg_amount, 2))
print("低订单平均金额:", round(low_avg_amount, 2))