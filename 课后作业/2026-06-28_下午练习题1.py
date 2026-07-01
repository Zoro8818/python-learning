# 要求输出：
#
# 原始订单记录列表
# 有效客户列表
# 有效金额列表
# 有效记录数量
# 无效记录数量
# 总金额
# 平均金额，保留 2 位小数
order_text = " 张三:120.5, 李四, , 王五:300, 赵六, 钱七: , 孙八:80 "

order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
valid_count = 0
invalid_count = 0
total_amount = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order == "":
        invalid_count += 1
    elif ":" not in clean_order:
        invalid_count += 1
    else:
        parts = clean_order.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

        else:
            invalid_count += 1

valid_count = len(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count
else:
    avg_amount = 0

print("原始订单记录列表: ", order_list)
print("有效客户列表: ", valid_customer_list)
print("有效金额列表: ", valid_amount_list)
print("有效记录数量: ", valid_count)
print("无效记录数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))


