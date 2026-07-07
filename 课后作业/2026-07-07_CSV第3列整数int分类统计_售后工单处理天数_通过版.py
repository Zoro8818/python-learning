# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/after_sales_tickets.csv"
cleaned_file = "D:/python-project/课后作业/output/after_sales_tickets_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/after_sales_tickets_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "工单编号,处理状态,处理天数":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_ticket_id_list = []
valid_ticket_status_list = []
valid_process_days_list = []

invalid_count = 0
total_process_days = 0
fast_process_count = 0
normal_process_count = 0
timeout_process_count = 0


# 第 6 块：循环处理每一条工单记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        ticket_id = parts[0].strip()
        ticket_status = parts[1].strip()
        process_days_text = parts[2].strip()

        if ticket_id == "" or process_days_text == "":
            invalid_count += 1
        elif process_days_text.isdigit():
            process_days = int(process_days_text)

            valid_ticket_id_list.append(ticket_id)
            valid_ticket_status_list.append(ticket_status)
            valid_process_days_list.append(process_days)
            total_process_days += process_days

            if process_days <= 3:
                fast_process_count += 1
            elif process_days <= 7:
                normal_process_count += 1
            else:
                timeout_process_count += 1
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均处理天数
raw_count = len(raw_record_list)
valid_count = len(valid_process_days_list)

if valid_count > 0:
    avg_process_days = total_process_days / valid_count

else:
    avg_process_days = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("工单编号,处理状态,处理天数\n")

    for i in range(valid_count):
        f.write(
            valid_ticket_id_list[i]
            + ","
            + valid_ticket_status_list[i]
            + ","
            + str(valid_process_days_list[i])
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("售后工单处理天数统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总处理天数：" + str(total_process_days) + "\n")
    f.write("平均处理天数：" + str(round(avg_process_days, 2)) + "\n")
    f.write("快速处理数量：" + str(fast_process_count) + "\n")
    f.write("正常处理数量：" + str(normal_process_count) + "\n")
    f.write("超时处理数量：" + str(timeout_process_count) + "\n")
