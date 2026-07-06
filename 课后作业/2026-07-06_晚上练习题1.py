# 商品库存 csv 清洗后导出最小版
# 输入：input/products.csv
# 输出：
# 1. output/products_cleaned.csv
# 2. output/products_summary.txt
#
# 字段：商品名称,库存,分类
#
# 判断规则：
# 1. 商品名称不能为空
# 2. 库存不能为空
# 3. 库存必须是整数数字，用 stock_text.isdigit()
# 4. 分类今天只保留，不做复杂判断
#
# 统计结果：
# 原始记录数量
# 有效记录数量
# 无效记录数量
# 库存总和
# 平均库存

# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/products.csv"
cleaned_file = "D:/python-project/课后作业/output/products_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/products_summary.txt"

# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "商品名称,库存,分类":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_product_list = []
valid_category_list = []
valid_stock_list = []

invalid_count = 0
total_stock = 0


# 第 6 块：循环处理每一条客户记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        product = parts[0].strip()
        stock_text = parts[1].strip()
        category = parts[2].strip()

        if product == "" or stock_text == "":
            invalid_count += 1
        elif stock_text.isdigit():
            stock = int(stock_text)

            valid_product_list.append(product)
            valid_stock_list.append(stock)
            valid_category_list.append(category)
            total_stock += stock
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均金额
raw_count = len(raw_record_list)
valid_count = len(valid_product_list)

if valid_count > 0:
    avg_stock = total_stock / valid_count

else:
    avg_stock = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("商品名称,库存,分类\n")

    for i in range(valid_count):
        f.write(
            valid_product_list[i]
            + ","
            + str(valid_stock_list[i])
            + ","
            + valid_category_list[i]
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("商品库存清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("库存总和：" + str(total_stock) + "\n")
    f.write("平均库存：" + str(round(avg_stock, 2)) + "\n")
