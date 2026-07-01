#1
text = "苹果:120, 香蕉:45, 梨:80, 桃子:30"

clean_record_list = []

record_list = text.split(",")

for record in record_list:
    clean_record = record.strip()
    clean_record_list.append(clean_record)

print(clean_record_list)

#2
valid_product_list = ["苹果", "香蕉", "梨", "桃子"]
valid_amount_list = [120.0, 45.0, 80.0, 30.0]

valid_count = len(valid_amount_list)
total_amount = sum(valid_amount_list)

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

print("有效数据数量: ", valid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高商品: ", max_product)
print("最高金额: ", max_amount)
print("最低商品: ", min_product)
print("最低金额: ", min_amount)


