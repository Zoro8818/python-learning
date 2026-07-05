# 1. 原始数据
records = [
    "小王:260",
    "小李:80",
    " :100",
    "小张:",
    "小周:0",
    "小吴:abc",
    "小赵:600"
]

# 2. 准备结果列表和统计变量
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

# 3. 清洗、拆分、有效判断和分类
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

# 4. 总体统计：平均值、最高值、最低值
valid_count = len(valid_number_list)

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

# 5. 分类统计：各分类平均值
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

# 6. 输出结果
print("原始记录：", records)
print("有效名称列表：", valid_name_list)
print("有效数字列表：", valid_number_list)

print("无效记录列表：", invalid_list)
print("无效记录数量：", len(invalid_list))

print("高分类名称列表：", high_name_list)
print("高分类数字列表：", high_number_list)
print("高分类数量：", len(high_name_list))
print("高分类总和：", high_total_number)
print("高分类平均值：", round(high_avg_number, 2))

print("中分类名称列表：", middle_name_list)
print("中分类数字列表：", middle_number_list)
print("中分类数量：", len(middle_name_list))
print("中分类总和：", middle_total_number)
print("中分类平均值：", round(middle_avg_number, 2))

print("低分类名称列表：", low_name_list)
print("低分类数字列表：", low_number_list)
print("低分类数量：", len(low_name_list))
print("低分类总和：", low_total_number)
print("低分类平均值：", round(low_avg_number, 2))

print("零值名称列表：", zero_name_list)
print("零值数字列表：", zero_number_list)
print("零值数量：", len(zero_name_list))
print("零值总和：", zero_total_number)
print("零值平均值：", round(zero_avg_number, 2))

print("数字总和：", total_number)
print("平均值：", round(avg_number, 2))

print("最高值名称：", max_name)
print("最高值：", max_number)

print("最低值名称：", min_name)
print("最低值：", min_number)
