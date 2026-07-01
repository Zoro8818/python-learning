consume_text = " 张三:1500, 李四:0, 王五:300, , 赵六:abc, 钱七:800, 错误数据, :200, 孙八: "
consume_list = consume_text.split(",")

valid_customer_list = []
valid_amount_list = []
high_consume_customer_list = []
normal_consume_customer_list = []
zero_consume_customer_list = []
invalid_count = 0
total_amount = 0
valid_count = 0
avg_amount = 0

for record in consume_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text_item  = parts[1].strip()

        if amount_text_item == "" or customer == "":
            invalid_count += 1
        elif amount_text_item.replace(".", "", 1).isdigit():
            amount = float(amount_text_item)
            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 1000:
                high_consume_customer_list.append(customer)
            elif amount > 0:
                normal_consume_customer_list.append(customer)
            else:
                zero_consume_customer_list.append(customer)

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

print("原始消费记录列表: ", consume_list)
print("有效会员列表: ", valid_customer_list)
print("有效消费金额列表: ", valid_amount_list)
print("无效记录数量: ", invalid_count)
print("有效记录数量: ", valid_count)
print("消费总金额: ", total_amount)
print("平均消费金额: ", round(avg_amount, 2))
print("最高消费会员: ", max_customer)
print("最高消费金额: ", max_amount)
print("最低消费会员: ", min_customer)
print("最低消费金额: ", min_amount)
print("高消费会员列表: ", high_consume_customer_list)
print("普通消费会员列表: ", normal_consume_customer_list)
print("零消费会员列表: ", zero_consume_customer_list)