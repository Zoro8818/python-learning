#1 商品库存清洗统计复盘题
stock_text = "苹果:10, , 香蕉, :20, 梨:, 桃子:abc, 西瓜:100, 葡萄:0, 芒果:35.5"
stock_list = stock_text.split(",")

valid_product_list = []
valid_stock_list = []
invalid_count = 0
total_stock = 0

for record in stock_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_value_text = parts[1].strip()

        if product == "":
            invalid_count += 1
        elif stock_value_text == "":
            invalid_count += 1
        elif not stock_value_text.replace(".", "", 1).isdigit():
            invalid_count += 1
        else:
            stock = float(stock_value_text)
            valid_product_list.append(product)
            valid_stock_list.append(stock)
            total_stock += stock

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

print("有效商品列表：", valid_product_list)
print("有效库存列表：", valid_stock_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("总库存：", total_stock)
print("平均库存：", avg_stock)
print("最高库存商品：", max_product)
print("最高库存：", max_stock)
print("最低库存商品：", min_product)
print("最低库存：", min_stock)
