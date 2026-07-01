records = [
    "张三:1200.5",
    "李四:860",
    "王五:2380",
    "",
    "赵六:450",
    "钱七:abc",
    "孙八:300.5"
]

customers = []
amounts = []
invalid_count = 0
total_amount = 0

for record in records:
    record = record.strip()

    if record == "":
        invalid_count += 1
        continue

    if ":" not in record:
        invalid_count += 1
        continue

    parts = record.split(":")
    customer = parts[0].strip()
    amount_text = parts[1].strip()

    if customer == "":
        invalid_count += 1
        continue

    if not amount_text.replace(".", "", 1).isdigit():
        invalid_count += 1
        continue

    amount = float(amount_text)
    customers.append(customer)
    amounts.append(amount)
    total_amount += amount

valid_count = len(amounts)

if valid_count > 0:
    avg_amount = total_amount / valid_count

    max_amount = amounts[0]
    max_customer = customers[0]

    min_amount = amounts[0]
    min_customer = customers[0]

    for i in range(len(amounts)):
        if amounts[i] > max_amount:
            max_amount = amounts[i]
            max_customer = customers[i]

        if amounts[i] < min_amount:
            min_amount = amounts[i]
            min_customer = customers[i]
else:
    avg_amount = 0
    max_amount = 0
    max_customer = ""
    min_amount = 0
    min_customer = ""

print("有效客户列表: ", customers)
print("有效金额列表: ", amounts)
print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高客户: ", max_customer)
print("最高金额: ", max_amount)
print("最低客户: ", min_customer)
print("最低金额: ", min_amount)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("无效数据数量: " + str(invalid_count) + "\n")
    f.write("总金额: " + str(total_amount) + "\n")
    f.write("平均金额: " + str(round(avg_amount, 2)) + "\n")
    f.write("最高客户: " + max_customer + "\n")
    f.write("最高金额: " + str(max_amount) + "\n")
    f.write("最低客户: " + min_customer + "\n")
    f.write("最低金额: " + str(min_amount) + "\n")



