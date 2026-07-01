order_text = " 张三:500, 李四:1200, , 王五:0, 赵六:80, 钱七:2000, 错误数据, 孙八:abc, :300, 周九: "

order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0
valid_count = 0
avg_amount = 0

big_order_customer_list = []
normal_order_customer_list = []
zero_order_customer_list = []

big_order_count = 0
normal_order_count = 0
zero_order_count = 0

for record in order_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text_item = parts[1].strip()

        if customer == "" or amount_text_item == "":
            invalid_count += 1
        elif amount_text_item.replace(".", "", 1).isdigit():
            amount = float(amount_text_item)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 1000:
                big_order_customer_list.append(customer)
                big_order_count += 1
            elif amount > 0:
                normal_order_customer_list.append(customer)
                normal_order_count += 1
            else:
                zero_order_customer_list.append(customer)
                zero_order_count += 1

        else:
            invalid_count += 1

valid_count = len(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count

    max_customer = valid_customer_list[0]
    max_amount = valid_amount_list[0]

    min_customer = valid_customer_list[0]
    min_amount = valid_amount_list[0]

    for i in range(valid_count):
        if valid_amount_list[i] > max_amount:
            max_customer = valid_customer_list[i]
            max_amount = valid_amount_list[i]

        if valid_amount_list[i] < min_amount:
            min_customer = valid_customer_list[i]
            min_amount = valid_amount_list[i]

else:
    avg_amount = 0
    max_customer = ""
    max_amount = 0
    min_customer = ""
    min_amount = 0

print("原始订单记录列表: ", order_list)
print("有效客户列表: ", valid_customer_list)
print("有效金额列表: ", valid_amount_list)
print("无效记录数量: ", invalid_count)
print("有效记录数量: ", valid_count)
print("订单总金额: ", total_amount)
print("平均订单金额: ", round(avg_amount, 2))
print("最高金额客户: ", max_customer)
print("最高金额: ", max_amount)
print("最低金额客户: ", min_customer)
print("最低金额: ", min_amount)
print("大额订单客户列表: ", big_order_customer_list)
print("大额订单数量: ", big_order_count)
print("普通订单客户列表: ", normal_order_customer_list)
print("普通订单数量: ", normal_order_count)
print("零元订单客户列表: ", zero_order_customer_list)
print("零元订单数量: ", zero_order_count)


