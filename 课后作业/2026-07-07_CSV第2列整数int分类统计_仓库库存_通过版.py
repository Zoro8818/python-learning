# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/warehouse_stock.csv"
cleaned_file = "D:/python-project/课后作业/output/warehouse_stock_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/warehouse_stock_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 第 3 块：按行拆分
lines = csv_text.splitlines()


# 第 4 块：去掉表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "商品名称,库存数量,仓库位置":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果列表和统计变量
valid_product_list = []
valid_stock_list = []
valid_warehouse_location_list = []

invalid_count = 0
total_stock = 0
high_stock_count = 0
normal_stock_count = 0
zero_stock_count = 0


# 第 6 块：循环处理每一条记录
# 输入表头顺序 = parts 拆字段顺序 = 有效列表保存顺序 = cleaned csv 写出顺序
# 示例表头：字段1,数字字段,字段3
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        # field_1 = parts[0].strip()
        # number_text = parts[1].strip()
        # field_3 = parts[2].strip()
        product_name = parts[0].strip()
        stock_text = parts[1].strip()
        warehouse_location = parts[2].strip()

        if product_name == "" or stock_text == "":
            invalid_count += 1
        elif stock_text.isdigit():
            stock = int(stock_text)

            valid_product_list.append(product_name)
            valid_stock_list.append(stock)
            valid_warehouse_location_list.append(warehouse_location)
            total_stock += stock

            if stock >= 100:
                high_stock_count += 1
            elif stock > 0:
                normal_stock_count += 1
            else:
                zero_stock_count += 1

        else:
            invalid_count += 1


# 第 7 块：统计数量和平均值
raw_count = len(raw_record_list)
valid_count = len(valid_stock_list)

if valid_count > 0:
    avg_stock = total_stock / valid_count
else:
    avg_stock = 0


# 第 8 块：写入 cleaned csv
# cleaned csv 写出顺序必须和表头顺序一致
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("商品名称,库存数量,仓库位置\n")

    for i in range(valid_count):
        f.write(
            valid_product_list[i]
            + ","
            + str(valid_stock_list[i])
            + ","
            + valid_warehouse_location_list[i]
            + "\n"
        )


# 第 9 块：写入 summary txt
# 数字字段位置必须根据具体业务表头重新确认
# 如果数字字段在第 2 列，用 parts[1]
# 如果数字字段在第 3 列，用 parts[2]
# 判断数字、转 int、累加 total、写入数字列表，必须全部对准真正的数字字段
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("CSV 清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("数字总和：" + str(total_stock) + "\n")
    f.write("平均数值：" + str(round(avg_stock, 2)) + "\n")
    f.write("高库存数量：" + str(high_stock_count) + "\n")
    f.write("普通库存数量：" + str(normal_stock_count) + "\n")
    f.write("零库存数量：" + str(zero_stock_count) + "\n")
