# 有效商品数量
# 有效商品名单
# 有效销售额列表
# 无效记录数量
# 总销售额
# 平均销售额，保留 2 位小数
# 最高销售额商品
# 最高销售额
# 最低销售额商品
# 最低销售额

sales_records = [
    "苹果: 120.5",
    "香蕉:80",
    "橙子:",
    " :66",
    "牛奶:abc",
    "",
    "面包: 35.5",
    "鸡蛋:0",
    "大米:300",
    "酸奶: 18.8"
]

valid_product_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0

for record in sales_records:
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

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

    max_amount = valid_amount_list[0]
    max_product = valid_product_list[0]

    min_amount = valid_amount_list[0]
    min_product = valid_product_list[0]

    for i in range(len(valid_amount_list)):
        if valid_amount_list[i] > max_amount:
            max_amount = valid_amount_list[i]
            max_product = valid_product_list[i]

        if valid_amount_list[i] < min_amount:
            min_amount = valid_amount_list[i]
            min_product = valid_product_list[i]

else:
    avg_amount = 0
    max_amount = 0
    max_product = ""
    min_amount = 0
    min_product = ""

print("有效商品数量:", len(valid_product_list))
print("有效商品名单:", valid_product_list)
print("有效销售额列表:", valid_amount_list)
print("无效记录数量:", invalid_count)
print("总销售额:", total_amount)
print("平均销售额:", round(avg_amount, 2))
print("最高销售额商品:", max_product)
print("最高销售额:", max_amount)
print("最低销售额商品:", min_product)
print("最低销售额:", min_amount)
