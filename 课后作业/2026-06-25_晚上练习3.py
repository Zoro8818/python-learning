valid_customer_list = ["张三", "李四", "王五", "赵六"]
valid_amount_list = [88.5, 300.0, 12.0, 450.0]

max_customer = valid_customer_list[0]
max_amount = valid_amount_list[0]

min_customer = valid_customer_list[0]
min_amount = valid_amount_list[0]

for i in range(len(valid_amount_list)):
    if valid_amount_list[i] > max_amount:
        max_amount = valid_amount_list[i]
        max_customer = valid_customer_list[i]

    if valid_amount_list[i] < min_amount:
        min_customer = valid_customer_list[i]
        min_amount = valid_amount_list[i]

print("最高客户:", max_customer)
print("最高金额:", max_amount)
print("最低客户:", min_customer)
print("最低金额:", min_amount)