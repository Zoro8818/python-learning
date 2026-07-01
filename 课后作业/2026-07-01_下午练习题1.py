consume_text = " 张三:1500, 李四:0, 王五:300, , 赵六:abc, 钱七:800, 错误数据, :200, 孙八: "

consume_list = consume_text.split(",")

valid_customer_list = []
valid_amount_list = []
valid_count = 0

for record in consume_list:
    clean_record = record.strip()

    if clean_record == "":
        continue
    elif ":" not in clean_record:
        continue
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text_item = parts[1].strip()
        if amount_text_item == "" or customer == "":
            continue
        elif amount_text_item.replace(".", "", 1).isdigit():
            amount = float(amount_text_item)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
        else:
            continue

valid_count = len(valid_amount_list)

if valid_count > 0:
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
    max_customer = ""
    max_amount = 0
    min_customer = ""
    min_amount = 0

print("最高消费会员: ", max_customer)
print("最高消费金额: ", max_amount)
print("最低消费会员: ", min_customer)
print("最低消费金额: ", min_amount)