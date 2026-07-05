# 1. 路径设置
input_file = "D:/python-project/课后作业/input/name_number_input.txt"
report_file = "D:/python-project/课后作业/output/name_number_report.txt"

# 2. 读取名称:数字 txt 输入
with open(input_file, "r", encoding="utf-8") as f:
    records_text = f.read()

records = records_text.splitlines()

# 3. 准备结果列表和统计变量
valid_name_list = []
valid_number_list = []

invalid_list = []

high_name_list = []
high_number_list = []

middle_name_list = []
middle_number_list = []

low_name_list = []
low_number_list = []

zero_name_list = []
zero_number_list = []

# 总体统计变量
total_number = 0

# 分类统计变量
high_total_number = 0
middle_total_number = 0
low_total_number = 0
zero_total_number = 0

high_avg_number = 0
middle_avg_number = 0
low_avg_number = 0
zero_avg_number = 0

# 4. 清洗、拆分、有效判断和分类
for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_list.append(clean_record)
    elif ":" not in clean_record:
        invalid_list.append(clean_record)
    else:
        parts = clean_record.split(":", 1)
        name = parts[0].strip()
        number_text = parts[1].strip()

        if name == "" or number_text == "":
            invalid_list.append(clean_record)
        elif number_text.replace(".", "", 1).isdigit():
            number = float(number_text)

            valid_name_list.append(name)
            valid_number_list.append(number)
            total_number += number

            if number >= 200:
                high_name_list.append(name)
                high_number_list.append(number)
                high_total_number += number

            elif number >= 100:
                middle_name_list.append(name)
                middle_number_list.append(number)
                middle_total_number += number

            elif number > 0:
                low_name_list.append(name)
                low_number_list.append(number)
                low_total_number += number

            else:
                zero_name_list.append(name)
                zero_number_list.append(number)
                zero_total_number += number

        else:
            invalid_list.append(clean_record)

# 5. 总体统计：平均值、最高值、最低值
valid_count = len(valid_name_list)

if valid_count > 0:
    avg_number = total_number / valid_count

    max_name = valid_name_list[0]
    max_number = valid_number_list[0]

    min_name = valid_name_list[0]
    min_number = valid_number_list[0]

    for i in range(valid_count):
        if valid_number_list[i] > max_number:
            max_name = valid_name_list[i]
            max_number = valid_number_list[i]

        if valid_number_list[i] < min_number:
            min_name = valid_name_list[i]
            min_number = valid_number_list[i]

else:
    avg_number = 0
    max_name = ""
    max_number = 0
    min_name = ""
    min_number = 0

# 6. 分类统计：各分类平均值
if len(high_number_list) > 0:
    high_avg_number = high_total_number / len(high_number_list)
else:
    high_avg_number = 0

if len(middle_number_list) > 0:
    middle_avg_number = middle_total_number / len(middle_number_list)
else:
    middle_avg_number = 0

if len(low_number_list) > 0:
    low_avg_number = low_total_number / len(low_number_list)
else:
    low_avg_number = 0

if len(zero_number_list) > 0:
    zero_avg_number = zero_total_number / len(zero_number_list)
else:
    zero_avg_number = 0

# 7. 写入 txt 统计报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("名称数字清洗统计分类报告\n")
    f.write("=" * 30 + "\n")
    f.write("\n")

    f.write("一、有效与无效记录\n")
    f.write("-" * 30 + "\n")
    f.write("原始记录：" + str(records) + "\n")
    f.write("有效名称列表：" + str(valid_name_list) + "\n")
    f.write("有效数字列表：" + str(valid_number_list) + "\n")
    f.write("无效记录列表：" + str(invalid_list) + "\n")
    f.write("无效记录数量：" + str(len(invalid_list)) + "\n")
    f.write("\n")

    f.write("二、分类结果\n")
    f.write("-" * 30 + "\n")
    f.write("高分类名称列表：" + str(high_name_list) + "\n")
    f.write("高分类数字列表：" + str(high_number_list) + "\n")
    f.write("高分类数量：" + str(len(high_name_list)) + "\n")
    f.write("高分类总和：" + str(high_total_number) + "\n")
    f.write("高分类平均值：" + str(round(high_avg_number, 2)) + "\n")
    f.write("\n")

    f.write("中分类名称列表：" + str(middle_name_list) + "\n")
    f.write("中分类数字列表：" + str(middle_number_list) + "\n")
    f.write("中分类数量：" + str(len(middle_name_list)) + "\n")
    f.write("中分类总和：" + str(middle_total_number) + "\n")
    f.write("中分类平均值：" + str(round(middle_avg_number, 2)) + "\n")
    f.write("\n")

    f.write("低分类名称列表：" + str(low_name_list) + "\n")
    f.write("低分类数字列表：" + str(low_number_list) + "\n")
    f.write("低分类数量：" + str(len(low_name_list)) + "\n")
    f.write("低分类总和：" + str(low_total_number) + "\n")
    f.write("低分类平均值：" + str(round(low_avg_number, 2)) + "\n")
    f.write("\n")

    f.write("零值名称列表：" + str(zero_name_list) + "\n")
    f.write("零值数字列表：" + str(zero_number_list) + "\n")
    f.write("零值数量：" + str(len(zero_name_list)) + "\n")
    f.write("零值总和：" + str(zero_total_number) + "\n")
    f.write("零值平均值：" + str(round(zero_avg_number, 2)) + "\n")
    f.write("\n")

    f.write("三、总体统计\n")
    f.write("-" * 30 + "\n")
    f.write("数字总和：" + str(total_number) + "\n")
    f.write("平均值：" + str(round(avg_number, 2)) + "\n")
    f.write("最高值名称：" + max_name + "\n")
    f.write("最高值：" + str(max_number) + "\n")
    f.write("最低值名称：" + min_name + "\n")
    f.write("最低值：" + str(min_number) + "\n")

print("报告已生成：", report_file)
