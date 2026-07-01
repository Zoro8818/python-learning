valid_product_list = ["苹果", "香蕉", "大米", "鸡蛋"]
valid_amount_list = [120.5, 80.0, 300.0, 0.0]

total_amount = 500.5

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

    max_product = valid_product_list[0]
    max_amount = valid_amount_list[0]

    min_product = valid_product_list[0]
    min_amount = valid_amount_list[0]

    for i in range(len(valid_amount_list)):
        if valid_amount_list[i] > max_amount:
            max_amount = valid_amount_list[i]
            max_product = valid_product_list[i]

        if valid_amount_list[i] < min_amount:
            min_amount = valid_amount_list[i]
            min_product = valid_product_list[i]
else:
    avg_amount = 0
    max_product = ""
    max_amount = 0
    min_product = ""
    min_amount = 0

normal_amount_list = []
normal_total_amount = 0

if len(normal_amount_list) > 0:
    normal_avg_amount = normal_total_amount / len(normal_amount_list)
else:
    normal_avg_amount = 0

print("平均销售额:", round(avg_amount, 2))
print("最高销售额商品:", max_product)
print("最高销售额:", max_amount)
print("最低销售额商品:", min_product)
print("最低销售额:", min_amount)
print("普通销售额平均金额:", round(normal_avg_amount, 2))