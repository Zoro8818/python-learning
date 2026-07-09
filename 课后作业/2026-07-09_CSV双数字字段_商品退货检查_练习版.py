# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/returns.csv"
cleaned_file = "D:/python-project/课后作业/output/returns_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/returns_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 第 3 块：按行拆分
lines = csv_text.splitlines()


# 第 4 块：去掉表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "商品名称,退货数量,退款金额":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果列表和统计变量
valid_product_name_list = []
valid_return_qty_list = []
valid_refund_amount_list = []

high_refund_list = []
normal_refund_list = []
zero_refund_list = []

invalid_count = 0

total_return_qty = 0
total_refund_amount = 0


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
        return_qty_text = parts[1].strip()
        refund_amount_text = parts[2].strip()

# 判断和转换

        if product_name == "":
            invalid_count += 1

        elif not return_qty_text.isdigit() :
            invalid_count += 1

        elif not refund_amount_text.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            return_qty = int(return_qty_text)

            refund_amount = float(refund_amount_text)

            valid_product_name_list.append(product_name)

            valid_return_qty_list.append(return_qty)

            valid_refund_amount_list.append(refund_amount)

            total_return_qty += return_qty

            total_refund_amount += refund_amount

            if refund_amount >= 500:
                high_refund_list.append(product_name)
            elif refund_amount > 0:
                normal_refund_list.append(product_name)
            else:
                zero_refund_list.append(product_name)


# 第 7 块：统计数量和平均值
raw_count = len(raw_record_list)

valid_count = len(valid_product_name_list)

if valid_count > 0:
    avg_return_qty = total_return_qty / valid_count
    avg_refund_amount = total_refund_amount / valid_count
else:
    avg_return_qty = 0
    avg_refund_amount = 0


# 第 8 块：写入 cleaned csv
# cleaned csv 写出顺序必须和表头顺序一致
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("商品名称,退货数量,退款金额\n")

    for i in range(valid_count):
        f.write(
            valid_product_name_list[i]
            + ","
            + str(valid_return_qty_list[i])
            + ","
            + str(valid_refund_amount_list[i])
            + "\n"
        )


# 第 9 块：写入 summary txt
# 数字字段位置必须根据具体业务表头重新确认
# 如果数字字段在第 2 列，用 parts[1]
# 如果数字字段在第 3 列，用 parts[2]
# 判断数字、转 int、累加 total、写入数字列表，必须全部对准真正的数字字段
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("CSV 商品退货退款清洗报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总退货数量：" + str(total_return_qty) + "\n")
    f.write("总退款金额: " + str(total_refund_amount) + "\n")
    f.write("平均退货数量：" + str(round(avg_return_qty, 2)) + "\n")
    f.write("平均退款金额：" + str(round(avg_refund_amount, 2)) + "\n")
    f.write("高额退款数量: " + str(len(high_refund_list)) + "\n")
    f.write("普通退款数量: " + str(len(normal_refund_list)) + "\n")
    f.write("零退款数量: " + str(len(zero_refund_list)) + "\n")