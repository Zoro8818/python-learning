# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/example.csv"
cleaned_file = "D:/python-project/课后作业/output/example_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/example_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 第 3 块：按行拆分
lines = csv_text.splitlines()


# 第 4 块：去掉表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "字段1,数字字段,字段3":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果列表和统计变量
valid_field_1_list = []
valid_number_list = []
valid_field_3_list = []

invalid_count = 0
total_number = 0


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
        field_1 = parts[0].strip()
        number_text = parts[1].strip()
        field_3 = parts[2].strip()

        if field_1 == "" or number_text == "":
            invalid_count += 1
        elif number_text.isdigit():
            number = int(number_text)

            valid_field_1_list.append(field_1)
            valid_number_list.append(number)
            valid_field_3_list.append(field_3)
            total_number += number
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均值
raw_count = len(raw_record_list)
valid_count = len(valid_field_1_list)

if valid_count > 0:
    avg_number = total_number / valid_count
else:
    avg_number = 0


# 第 8 块：写入 cleaned csv
# cleaned csv 写出顺序必须和表头顺序一致
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("字段1,数字字段,字段3\n")

    for i in range(valid_count):
        f.write(
            valid_field_1_list[i]
            + ","
            + str(valid_number_list[i])
            + ","
            + valid_field_3_list[i]
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
    f.write("数字总和：" + str(total_number) + "\n")
    f.write("平均数值：" + str(round(avg_number, 2)) + "\n")
