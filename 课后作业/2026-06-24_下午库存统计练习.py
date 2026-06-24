# 要求：
# 遍历 products
# 清洗整条记录
# 空记录算无效
# 用 split(":", 1) 拆成 product 和 stock_text
# 左右字段都要 strip()
# 商品名为空，算无效
# 库存文本为空，算无效
# 库存文本必须先判断是不是合法数字，再 float() 转换
# 有效库存保存到 valid_stocks
# 无效记录数量用 invalid_count 统计
# 对有效库存分类：stock >= 100：高库存
# stock >= 50：中库存
# else：低库存

# 输出：有效商品数量
# 无效记录数量
# 库存总数
# 平均库存
# 高 / 中 / 低 库存商品数量
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
valid_stocks = []

valid_stocks_count = 0
invalid_stocks_count = 0
big_count = 0
medium_count = 0
small_count = 0
total_stocks = 0

for record in products:
    clean_record = record.strip()

    if clean_record == "":
        invalid_stocks_count += 1

    elif ":" not in clean_record:
        invalid_stocks_count += 1

    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_text = parts[1].strip()

        if product == "" or stock_text == "":
            invalid_stocks_count += 1

        elif stock_text.replace(".", "", 1).isdigit():
            stock = float(stock_text)

            valid_stocks.append(stock)
            valid_stocks_count += 1
            total_stocks += stock

            if stock >= 100:
                big_count += 1
            elif stock >= 50:
                medium_count += 1
            else:
                small_count += 1

        else:
            invalid_stocks_count += 1

if len(valid_stocks) > 0:
    avg_stocks = total_stocks / len(valid_stocks)
else:
    avg_stocks = 0

print("有效商品数量:", valid_stocks_count)
print("无效记录数量:", invalid_stocks_count)
print("库存总数:", total_stocks)
print("平均库存:", round(avg_stocks, 2))
print("高库存商品数量:", big_count)
print("中库存商品数量:", medium_count)
print("低库存商品数量:", small_count)