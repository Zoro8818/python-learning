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

    if clean_line != "" and clean_line != "员工姓名,出勤天数,工资金额":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果列表和统计变量
valid_employee_name_list = []
valid_attendance_days_list = []
valid_salary_amount_list = []

high_salary_list = []
normal_salary_list = []
zero_salary_list = []

invalid_count = 0

total_attendance_days = 0
total_salary_amount = 0


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
        employee_name = parts[0].strip()
        attendance_days_text = parts[1].strip()
        salary_amount_text = parts[2].strip()

# 判断和转换

        if employee_name == "":
            invalid_count += 1

        elif not attendance_days_text.isdigit() :
            invalid_count += 1

        elif not salary_amount_text.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            attendance_days = int(attendance_days_text)

            salary_amount = float(salary_amount_text)

            valid_employee_name_list.append(employee_name)

            valid_attendance_days_list.append(attendance_days)

            valid_salary_amount_list.append(salary_amount)

            total_attendance_days += attendance_days

            total_salary_amount += salary_amount

            if salary_amount >= 6000:
                high_salary_list.append(employee_name)
            elif salary_amount > 0:
                normal_salary_list.append(employee_name)
            else:
                zero_salary_list.append(employee_name)


# 第 7 块：统计数量和平均值
raw_count = len(raw_record_list)

valid_count = len(valid_employee_name_list)

if valid_count > 0:
    avg_attendance_days = total_attendance_days / valid_count
    avg_salary_amount = total_salary_amount / valid_count
else:
    avg_attendance_days = 0
    avg_salary_amount = 0


# 第 8 块：写入 cleaned csv
# cleaned csv 写出顺序必须和表头顺序一致
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("员工姓名,出勤天数,工资金额\n")

    for i in range(valid_count):
        f.write(
            valid_employee_name_list[i]
            + ","
            + str(valid_attendance_days_list[i])
            + ","
            + str(valid_salary_amount_list[i])
            + "\n"
        )


# 第 9 块：写入 summary txt
# 数字字段位置必须根据具体业务表头重新确认
# 如果数字字段在第 2 列，用 parts[1]
# 如果数字字段在第 3 列，用 parts[2]
# 判断数字、转 int、累加 total、写入数字列表，必须全部对准真正的数字字段
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("CSV 员工考勤工资清理统计\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总出勤天数：" + str(total_attendance_days) + "\n")
    f.write("总工资金额: " + str(total_salary_amount) + "\n")
    f.write("平均出勤天数：" + str(round(avg_attendance_days, 2)) + "\n")
    f.write("平均工资金额：" + str(round(avg_salary_amount, 2)) + "\n")
    f.write("高工资数量: " + str(len(high_salary_list)) + "\n")
    f.write("普通工资数量: " + str(len(normal_salary_list)) + "\n")
    f.write("零工资数量: " + str(len(zero_salary_list)) + "\n")