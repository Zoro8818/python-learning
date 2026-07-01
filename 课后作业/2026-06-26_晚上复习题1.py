with open("sales.txt", "r", encoding="utf-8") as f:
    text = f.read()

record_list = text.split(",")

print(text)
print(record_list)
print("记录数量: ", len(record_list))

clean_record_list = []

for record in record_list:
    clean_record = record.strip()
    clean_record_list.append(clean_record)

print(clean_record_list)

valid_product_list = []
valid_amount_list = []
invalid_count = 0

for record in clean_record_list:
    if record == "":
        invalid_count += 1
    elif ":" not in record:
        invalid_count += 1
    else:
        parts = record.split(":", 1)
        product = parts[0].strip()
        amount_text = parts[1].strip()

        if product == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)
            valid_product_list.append(product)
            valid_amount_list.append(amount)
        else:
            invalid_count += 1

print(valid_product_list)
print(valid_amount_list)
print(invalid_count)

valid_product_list = ["苹果", "香蕉", "梨", "桃子", "芒果"]
valid_amount_list = [120.0, 45.0, 80.0, 30.0, 200.0]

valid_count = len(valid_amount_list)

if valid_count > 0:
    max_product = valid_product_list[0]
    max_amount = valid_amount_list[0]

    min_product = valid_product_list[0]
    min_amount = valid_amount_list[0]

    for i in range(valid_count):
        if valid_amount_list[i] > max_amount:
            max_product = valid_product_list[i]
            max_amount = valid_amount_list[i]

        if valid_amount_list[i] < min_amount:
            min_product = valid_product_list[i]
            min_amount = valid_amount_list[i]

else:
    max_product = ""
    max_amount = 0
    min_product = ""
    min_amount = 0

print("最高商品: ", max_product)
print("最高金额: ", max_amount)
print("最低商品: ", min_product)
print("最低金额: ", min_amount)

print("----------------------------------------")

#
with open("sales.txt", "r", encoding="utf-8") as f:
    text = f.read()

record_list = text.split(",")


valid_product_list = []
valid_amount_list = []
invalid_count = 0

for record in record_list:
    record = record.strip()

    if record == "":
        invalid_count += 1
    elif ":" not in record:
        invalid_count += 1
    else:
        parts = record.split(":", 1)
        product = parts[0].strip()
        amount_text = parts[1].strip()

        if product == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_product_list.append(product)
            valid_amount_list.append(amount)

        else:
            invalid_count += 1


valid_count = len(valid_amount_list)
total_amount = sum(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count
else:
    avg_amount = 0

with open("sales_summary.txt", "w", encoding="utf-8") as f:
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("无效数据数量: " + str(invalid_count) + "\n")
    f.write("总销售额: " + str(total_amount) + "\n")
    f.write("平均销售额: " + str(round(avg_amount, 2)) + "\n")