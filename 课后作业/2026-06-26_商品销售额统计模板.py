# 商品销售额统计模板
# 输入文件：sales.txt
# 输出文件：sales_summary.txt
# 输入格式：商品名:金额, 商品名:金额
# 注意：必须使用英文逗号 "," 和英文冒号 ":"

with open("sales.txt", "r", encoding="utf-8") as f:
    text = f.read()

record_list = text.split(",")

valid_product_list = []
valid_amount_list = []

high_product_list = []
high_amount_list = []
high_total_amount = 0

normal_product_list = []
normal_amount_list = []
normal_total_amount = 0

low_product_list = []
low_amount_list = []
low_total_amount = 0

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
        product = parts[0].strip()
        amount_text = parts[1].strip()

        if product == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_product_list.append(product)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 100:
                high_product_list.append(product)
                high_amount_list.append(amount)
                high_total_amount += amount
            elif amount >= 50:
                normal_product_list.append(product)
                normal_amount_list.append(amount)
                normal_total_amount += amount
            else:
                low_product_list.append(product)
                low_amount_list.append(amount)
                low_total_amount += amount

        else:
            invalid_count += 1

valid_count = len(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count

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
    avg_amount = 0
    max_product = ""
    max_amount = 0
    min_product = ""
    min_amount = 0

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

print("有效商品列表: ", valid_product_list)
print("有效销售额列表: ", valid_amount_list)
print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)
print("总销售额: ", total_amount)
print("平均销售额: ", round(avg_amount, 2))
print("高销售额商品列表: ", high_product_list)
print("高销售额数量: ", len(high_amount_list))
print("高销售额总额: ", high_total_amount)
print("高销售额平均值: ", round(high_avg_amount, 2))
print("普通销售额商品列表: ", normal_product_list)
print("普通销售额数量: ", len(normal_amount_list))
print("普通销售额总额: ", normal_total_amount)
print("普通销售额平均值: ", round(normal_avg_amount, 2))
print("低销售额商品列表: ", low_product_list)
print("低销售额数量: ", len(low_amount_list))
print("低销售额总额: ", low_total_amount)
print("低销售额平均值: ", round(low_avg_amount, 2))
print("最高销售额商品: ", max_product)
print("最高销售额: ", max_amount)
print("最低销售额商品: ", min_product)
print("最低销售额: ", min_amount)

with open("sales_summary.txt" , "w", encoding="utf-8") as f:
    f.write("有效商品列表: " + str(valid_product_list) + "\n")
    f.write("有效销售额列表: " + str(valid_amount_list) + "\n")
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("无效数据数量: " + str(invalid_count) + "\n")
    f.write("总销售额: " + str(total_amount) + "\n")
    f.write("平均销售额: " + str(round(avg_amount, 2)) + "\n")
    f.write("高销售额商品列表: " + str(high_product_list) + "\n")
    f.write("高销售额数量: " + str(len(high_amount_list)) + "\n")
    f.write("高销售额总额: " + str(high_total_amount) + "\n")
    f.write("高销售额平均值: " + str(round(high_avg_amount, 2)) + "\n")
    f.write("普通销售额商品列表: " + str(normal_product_list) + "\n")
    f.write("普通销售额数量: " + str(len(normal_amount_list)) + "\n")
    f.write("普通销售额总额: " + str(normal_total_amount) + "\n")
    f.write("普通销售额平均值: " + str(round(normal_avg_amount, 2)) + "\n")
    f.write("低销售额商品列表: " + str(low_product_list) + "\n")
    f.write("低销售额数量: " + str(len(low_amount_list)) + "\n")
    f.write("低销售额总额: " + str(low_total_amount) + "\n")
    f.write("低销售额平均值: " + str(round(low_avg_amount, 2)) + "\n")
    f.write("最高销售额商品: " + str(max_product) + "\n")
    f.write("最高销售额: " + str(max_amount) + "\n")
    f.write("最低销售额商品: " + str(min_product) + "\n")
    f.write("最低销售额: " + str(min_amount) + "\n")

