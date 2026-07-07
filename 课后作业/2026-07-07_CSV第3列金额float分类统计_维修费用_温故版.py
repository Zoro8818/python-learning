# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/repair_cost.csv"
cleaned_file = "D:/python-project/课后作业/output/repair_cost_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/repair_cost_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "维修项目,维修状态,维修费用":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_repair_item_list = []
valid_repair_status_list = []
valid_repair_cost_list = []

invalid_count = 0
total_repair_cost = 0
high_repair_cost_count = 0
normal_repair_cost_count = 0
zero_repair_cost_count = 0


# 第 6 块：循环处理每一条维修记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        repair_item = parts[0].strip()
        repair_status = parts[1].strip()
        repair_cost_text = parts[2].strip()

        if repair_item == "" or repair_cost_text == "":
            invalid_count += 1
        elif repair_cost_text.replace(".", "", 1).isdigit():
            repair_cost = float(repair_cost_text)

            valid_repair_item_list.append(repair_item)
            valid_repair_status_list.append(repair_status)
            valid_repair_cost_list.append(repair_cost)
            total_repair_cost += repair_cost

            if repair_cost >= 1000:
                high_repair_cost_count += 1
            elif repair_cost > 0:
                normal_repair_cost_count += 1
            else:
                zero_repair_cost_count += 1
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均金额
raw_count = len(raw_record_list)
valid_count = len(valid_repair_cost_list)

if valid_count > 0:
    avg_repair_cost = total_repair_cost / valid_count

else:
    avg_repair_cost = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("维修项目,维修状态,维修费用\n")

    for i in range(valid_count):
        f.write(
            valid_repair_item_list[i]
            + ","
            + valid_repair_status_list[i]
            + ","
            + str(valid_repair_cost_list[i])
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("维修费用清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总维修费用：" + str(total_repair_cost) + "\n")
    f.write("平均维修费用：" + str(round(avg_repair_cost, 2)) + "\n")
    f.write("高维修费用数量: " + str(high_repair_cost_count) + "\n")
    f.write("普通维修费用数量: " + str(normal_repair_cost_count) + "\n")
    f.write("零维修费用数量: " + str(zero_repair_cost_count) + "\n")
