
order_records = [
    "张三: 88.5",
    "李四:520",
    "王五:",
    " :99",
    "赵六:abc",
    "",
    "钱七:60",
    "孙八:0",
    "周九:300.5",
    "吴十:72",
    "郑十一:45",
    "王十二:210"
]

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0

high_customer_list = []
high_amount_list = []
high_total_amount = 0

normal_customer_list = []
normal_amount_list = []
normal_total_amount = 0

low_customer_list = []
low_amount_list = []
low_total_amount = 0

for record in order_records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 200:
                high_customer_list.append(customer)
                high_amount_list.append(amount)
                high_total_amount += amount

            elif amount >= 50:
                normal_customer_list.append(customer)
                normal_amount_list.append(amount)
                normal_total_amount += amount
            else:
                low_customer_list.append(customer)
                low_amount_list.append(amount)
                low_total_amount += amount

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

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

else:
    avg_amount = 0
    max_amount = 0
    max_customer = ""
    min_amount = 0
    min_customer = ""

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

print("有效客户数量:", len(valid_customer_list))
print("有效客户名单:", valid_customer_list)
print("有效金额列表:", valid_amount_list)
print("无效记录数量:", invalid_count)
print("总金额:", total_amount)
print("平均金额:", round(avg_amount, 2))

print("最高消费客户:", max_customer)
print("最高消费金额:", max_amount)
print("最低消费客户:", min_customer)
print("最低消费金额:", min_amount)

print("高订单客户列表:", high_customer_list)
print("高订单金额列表:", high_amount_list)
print("高订单数量:", len(high_amount_list))
print("高订单总金额:", high_total_amount)
print("高订单平均金额:", round(high_avg_amount, 2))

print("普通订单客户列表:", normal_customer_list)
print("普通订单金额列表:", normal_amount_list)
print("普通订单数量:", len(normal_amount_list))
print("普通订单总金额:", normal_total_amount)
print("普通订单平均金额:", round(normal_avg_amount, 2))

print("低订单客户列表:", low_customer_list)
print("低订单金额列表:", low_amount_list)
print("低订单数量:", len(low_amount_list))
print("低订单总金额:", low_total_amount)
print("低订单平均金额:", round(low_avg_amount, 2))