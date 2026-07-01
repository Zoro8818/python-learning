stock_text = " 苹果:120, 香蕉:50, , 西瓜:20, 草莓:200, 芒果:0, 错误数据, 梨子:abc, :80, 橙子: "
stock_list = stock_text.split(",")

valid_product_list = []
valid_stock_list = []
invalid_count = 0
total_stock = 0
valid_count = 0
avg_stock = 0

high_stock_product_list = []
middle_stock_product_list = []
low_stock_product_list = []

high_stock_count = 0
middle_stock_count = 0
low_stock_count = 0

for record in stock_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_text_item = parts[1].strip()

        if stock_text_item == "":
            invalid_count += 1
        elif product == "":
            invalid_count += 1
        elif not stock_text_item.replace(".", "", 1).isdigit():
            invalid_count += 1
        else:
            stock = float(stock_text_item)

            valid_product_list.append(product)
            valid_stock_list.append(stock)
            total_stock += stock

            if stock >= 100:
                high_stock_product_list.append(product)
                high_stock_count += 1
            elif stock >= 50:
                middle_stock_product_list.append(product)
                middle_stock_count += 1
            else:
                low_stock_product_list.append(product)
                low_stock_count += 1

valid_count = len(valid_stock_list)

if valid_count > 0:
    avg_stock = total_stock / valid_count

    max_product = valid_product_list[0]
    max_stock = valid_stock_list[0]

    min_product = valid_product_list[0]
    min_stock = valid_stock_list[0]

    for i in range(valid_count):
        if valid_stock_list[i] > max_stock:
            max_product = valid_product_list[i]
            max_stock = valid_stock_list[i]

        if valid_stock_list[i] < min_stock:
            min_product = valid_product_list[i]
            min_stock = valid_stock_list[i]

else:
    avg_stock = 0
    max_product = ""
    max_stock = 0
    min_product = ""
    min_stock = 0

print("原始库存记录列表: ", stock_list)
print("有效商品列表: ", valid_product_list)
print("有效库存列表: ", valid_stock_list)
print("无效记录数量: ", invalid_count)
print("有效记录数量: ", valid_count)
print("库存总数: ", total_stock)
print("平均库存: ", round(avg_stock, 2))
print("最高库存商品: ", max_product)
print("最高库存: ", max_stock)
print("最低库存商品: ", min_product)
print("最低库存: ", min_stock)
print("高库存商品列表: ", high_stock_product_list)
print("高库存商品数量: ", high_stock_count)
print("中库存商品列表: ", middle_stock_product_list)
print("中库存商品数量: ", middle_stock_count)
print("低库存商品列表: ", low_stock_product_list)
print("低库存商品数量: ", low_stock_count)