# 要求：
# 清洗并筛选有效记录。
# 用 record 遍历 products。
# 拆出：product
# stock_text
#
# 判断无效记录：空记录
# 没有冒号
# 商品名为空
# 库存文本为空
# 库存文本不是数字
#
# 合法后：stock = float(stock_text)
# valid_product_list.append(product)
# valid_stocks.append(stock)
#
# 输出：有效商品数量
# 有效商品名单
# 无效记录数量
# 库存总数
# 平均库存
# 最高库存商品名
# 最高库存数量
# 最低库存商品名
# 最低库存数量

products = [
    "苹果: 120",
    "香蕉:80",
    "橙子:",
    " :200",
    "西瓜:abc",
    "",
    "葡萄: 30",
    "芒果:0",
    "梨:150",
    "桃子:60"
]
valid_product_list = []
valid_stocks = []

invalid_count = 0
total_stocks = 0

for record in products:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_text = parts[1].strip()

        if product == "" or stock_text == "":
            invalid_count += 1

        elif stock_text.replace(".", "", 1).isdigit():
            stock = float(stock_text)

            valid_product_list.append(product)
            valid_stocks.append(stock)
            total_stocks += stock

        else:
            invalid_count += 1

if len(valid_stocks) > 0:
    avg_stocks = total_stocks / len(valid_stocks)
    max_stock = valid_stocks[0]
    max_product = valid_product_list[0]

    min_stock = valid_stocks[0]
    min_product = valid_product_list[0]

    for i in range(len(valid_stocks)):
        if valid_stocks[i] > max_stock:
            max_stock = valid_stocks[i]
            max_product = valid_product_list[i]

        if valid_stocks[i] < min_stock:
            min_stock = valid_stocks[i]
            min_product = valid_product_list[i]

else:
    avg_stocks = 0
    max_stock = 0
    max_product = ""
    min_stock = 0
    min_product = ""

print("有效商品数量:", len(valid_stocks))
print("有效商品名单:", valid_product_list)
print("无效记录数量:", invalid_count)
print("库存总数:", total_stocks)
print("平均库存:", round(avg_stocks, 2))
print("最高库存商品名:", max_product)
print("最高库存数量:", max_stock)
print("最低库存商品名:", min_product)
print("最低库存数量:", min_stock)