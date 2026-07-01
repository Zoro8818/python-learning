valid_product_list = ["苹果", "香蕉", "大米", "鸡蛋"]
valid_amount_list = [120.5, 80.0, 300.0, 0.0]

if len(valid_amount_list) > 0:
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
    max_amount = 0
    max_product = ""
    min_amount = 0
    min_product = ""

print("最高销售额商品:", max_product)
print("最高销售额:", max_amount)
print("最低销售额商品:", min_product)
print("最低销售额:", min_amount)