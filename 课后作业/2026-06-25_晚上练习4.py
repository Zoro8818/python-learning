order_records = [
    "张三:88.5",
    "李四:300",
    "王五:",
    " :66",
    "赵六:abc",
    "",
    "钱七:60",
    "孙八:0",
    "周九:450",
    "吴十:72"
]
valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0
high_customer_list = []
normal_customer_list = []
low_customer_list = []

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
            elif amount >= 50:
                normal_customer_list.append(customer)
            else:
                low_customer_list.append(customer)

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    max_customer = valid_customer_list[0]
    max_amount = valid_amount_list[0]

    min_customer = valid_customer_list[0]
    min_amount = valid_amount_list[0]

    for i in range(len(valid_amount_list)):
        if valid_amount_list[i] > max_amount:
            max_amount = valid_amount_list[i]
            max_customer = valid_customer_list[i]

        if valid_amount_list[i] < min_amount:
            min_amount = valid_amount_list[i]
            min_customer = valid_customer_list[i]
else:
    max_customer = ""
    max_amount = 0
    min_customer = ""
    min_amount = 0

print("有效客户名单:", valid_customer_list)
print("无效记录数量:", invalid_count)
print("总金额:", total_amount)
print("最高客户:", max_customer, max_amount)
print("最低客户:", min_customer, min_amount)
print("高/普通/低数量:", len(high_customer_list), len(normal_customer_list), len(low_customer_list))