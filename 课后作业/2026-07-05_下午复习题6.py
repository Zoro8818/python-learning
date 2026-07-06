input_file = "D:/python-project/课后作业/input/order_input.txt"
report_file = "D:/python-project/课后作业/output/order_report.txt"

with open(input_file, "r", encoding="utf-8") as f:
    order_text= f.read()

valid_customer_list = []
valid_amount_list = []

invalid_list = []

big_order_customer_list = []
normal_order_customer_list = []
zero_order_customer_list = []

total_amount = 0
order_records = order_text.splitlines()

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
            elif amount >0:
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

print("订单金额统计报告")
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

with open(report_file, "w", encoding="utf-8") as f:
    f.write("订单金额统计报告\n")
    f.write("\n")

    f.write("原始订单记录：" + str(order_records) + "\n")
    f.write("有效客户列表：" + str(valid_customer_list) + "\n")
    f.write("有效金额列表：" + str(valid_amount_list) + "\n")
    f.write("\n")

    f.write("无效记录列表：" + str(invalid_list) + "\n")
    f.write("无效记录数量：" + str(len(invalid_list)) + "\n")
    f.write("\n")

    f.write("大额订单客户列表：" + str(big_order_customer_list) + "\n")
    f.write("大额订单数量：" + str(len(big_order_customer_list)) + "\n")
    f.write("\n")

    f.write("普通订单客户列表：" + str(normal_order_customer_list) + "\n")
    f.write("普通订单数量：" + str(len(normal_order_customer_list)) + "\n")
    f.write("\n")

    f.write("零元订单客户列表：" + str(zero_order_customer_list) + "\n")
    f.write("零元订单数量：" + str(len(zero_order_customer_list)) + "\n")
    f.write("\n")

    f.write("订单总金额：" + str(total_amount) + "\n")
    f.write("订单平均金额：" + str(round(avg_amount, 2)) + "\n")
    f.write("\n")

    f.write("最高金额客户：" + max_customer + "\n")
    f.write("最高金额：" + str(max_amount) + "\n")
    f.write("最低金额客户：" + min_customer + "\n")
    f.write("最低金额：" + str(min_amount) + "\n")