product_records = [
    "鼠标:120",
    "键盘:45",
    "显示器:8",
    "耳机:0",
    " :30",
    "音箱:",
    "摄像头:abc",
    "硬盘:300"
]

valid_product_list = []
valid_stock_list = []

invalid_list = []

high_stock_product_list = []
middle_stock_product_list = []
low_stock_product_list = []
zero_stock_product_list = []
total_stock = 0

for record in product_records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_list.append(clean_record)
    elif ":" not in clean_record:
        invalid_list.append(clean_record)
    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_text = parts[1].strip()

        if product == "" or stock_text == "":
            invalid_list.append(clean_record)
        elif stock_text.replace(".", "", 1).isdigit():
            stock = int(stock_text)

            valid_product_list.append(product)
            valid_stock_list.append(stock)
            total_stock += stock

            if stock >= 100:
                high_stock_product_list.append(product)
            elif stock >= 50:
                middle_stock_product_list.append(product)
            elif stock > 0:
                low_stock_product_list.append(product)
            else:
                zero_stock_product_list.append(product)

        else:
            invalid_list.append(clean_record)

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

print("原始商品记录：", product_records)
print("有效商品列表：", valid_product_list)
print("有效库存列表：", valid_stock_list)
print("无效记录列表：", invalid_list)
print("无效记录数量：", len(invalid_list))

print("高库存商品列表：", high_stock_product_list)
print("高库存数量：", len(high_stock_product_list))

print("中库存商品列表：", middle_stock_product_list)
print("中库存数量：", len(middle_stock_product_list))

print("低库存商品列表：", low_stock_product_list)
print("低库存数量：", len(low_stock_product_list))

print("零库存商品列表：", zero_stock_product_list)
print("零库存数量：", len(zero_stock_product_list))

print("总库存：", total_stock)
print("平均库存：", round(avg_stock, 2))
print("最高库存商品：", max_product)
print("最高库存：", max_stock)
print("最低库存商品：", min_product)
print("最低库存：", min_stock)

