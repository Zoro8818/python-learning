with open("orders.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

record_list = text.split(",")
print(record_list)

valid_customer_list = []
valid_amounts_list = []
invalid_count = 0
total_amount = 0

for record in record_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amounts_text = parts[1].strip()

        if customer == "" or amounts_text == "":
            invalid_count += 1
        elif amounts_text.replace(".", "", 1).isdigit():
            amount = float(amounts_text)

            valid_customer_list.append(customer)
            valid_amounts_list.append(amount)
            total_amount += amount

        else:
            invalid_count += 1

valid_count = len(valid_amounts_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count

    max_amount = valid_amounts_list[0]
    max_customer = valid_customer_list[0]

    min_amount = valid_amounts_list[0]
    min_customer = valid_customer_list[0]

    for i in range(valid_count):
        if valid_amounts_list[i] > max_amount:
            max_amount = valid_amounts_list[i]
            max_customer = valid_customer_list[i]

        if valid_amounts_list[i] < min_amount:
            min_amount = valid_amounts_list[i]
            min_customer = valid_customer_list[i]

else:
    avg_amount = 0
    max_amount = 0
    max_customer = ""
    min_amount = 0
    min_customer = ""

print("有效客户列表: ", valid_customer_list)
print("有效客户数量: ", valid_count)
print("有效客户金额: ", valid_amounts_list)
print("无效记录数据: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高客户: ", max_customer)
print("最高金额: ", max_amount)
print("最低客户: ", min_customer)
print("最低金额: ", min_amount)

with open("orders_summary.txt", "w", encoding="utf-8") as f:
    f.write("有效客户列表: " + str(valid_customer_list) + "\n")
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("有效客户金额: " + str(valid_amounts_list) + "\n")
    f.write("无效记录数据: " + str(invalid_count) + "\n")
    f.write("总金额: " + str(total_amount) + "\n")
    f.write("平均金额: " + str(round(avg_amount, 2)) + "\n")
    f.write("最高客户: " + max_customer + "\n")
    f.write("最高金额: " + str(max_amount) + "\n")
    f.write("最低客户: " + min_customer + "\n")
    f.write("最低金额: "+ str(min_amount) + "\n")
