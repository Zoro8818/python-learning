order_records = [
    "小王:260",
    "小李:80",
    " :100",
    "小张:",
    "小周:0",
    "小吴:abc",
    "小赵:600"
]

valid_customer_list = []
valid_amount_list = []
total_amount = 0

invalid_list = []

big_order_customer_list = []
normal_order_customer_list = []
zero_order_customer_list = []
for record in order_records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_list.append(clean_record)
    elif ":" not in clean_record:
        invalid_list.append(clean_record)
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_list.append(clean_record)
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)
            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 200:
                big_order_customer_list.append(customer)
            elif amount > 0:
                normal_order_customer_list.append(customer)
            else:
                zero_order_customer_list.append(customer)

        else:
            invalid_list.append(clean_record)

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



print("原始订单记录：", order_records)
print("有效客户列表：", valid_customer_list)
print("有效金额列表：", valid_amount_list)
print("无效记录列表：", invalid_list)
print("无效记录数量：", len(invalid_list))

print("大额订单客户列表：", big_order_customer_list)
print("大额订单数量：", len(big_order_customer_list))

print("普通订单客户列表：", normal_order_customer_list)
print("普通订单数量：", len(normal_order_customer_list))

print("零元订单客户列表：", zero_order_customer_list)
print("零元订单数量：", len(zero_order_customer_list))

print("订单总金额：", total_amount)
print("订单平均金额：", round(avg_amount, 2))
print("最高金额客户：", max_customer)
print("最高金额：", max_amount)
print("最低金额客户：", min_customer)
print("最低金额：", min_amount)