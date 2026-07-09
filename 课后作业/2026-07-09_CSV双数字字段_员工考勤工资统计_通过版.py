# 员工考勤工资 CSV 双数字字段统计模板
#
# 模板定位：
# 第 1 列：名称字段
# 第 2 列：整数 int 字段
# 第 3 列：金额 float 字段
#
# 输入：input/employee_salary.csv
# 输出：
# 1. output/employee_salary_cleaned.csv
# 2. output/employee_salary_summary.txt
#
# 核心提醒：
# 输入表头顺序 = parts 拆字段顺序 = 有效列表保存顺序 = cleaned csv 写出顺序


# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/employee_salary.csv"
cleaned_file = "D:/python-project/课后作业/output/employee_salary_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/employee_salary_summary.txt"


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
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        # 表头：员工姓名,出勤天数,工资金额
        # parts[0] = 员工姓名
        # parts[1] = 出勤天数，整数 int
        # parts[2] = 工资金额，金额 float
        employee_name = parts[0].strip()
        attendance_days_text = parts[1].strip()
        salary_amount_text = parts[2].strip()

        if employee_name == "":
            invalid_count += 1
        elif not attendance_days_text.isdigit():
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
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("员工考勤工资 CSV 清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总出勤天数：" + str(total_attendance_days) + "\n")
    f.write("总工资金额：" + str(total_salary_amount) + "\n")
    f.write("平均出勤天数：" + str(round(avg_attendance_days, 2)) + "\n")
    f.write("平均工资金额：" + str(round(avg_salary_amount, 2)) + "\n")
    f.write("高工资数量：" + str(len(high_salary_list)) + "\n")
    f.write("普通工资数量：" + str(len(normal_salary_list)) + "\n")
    f.write("零工资数量：" + str(len(zero_salary_list)) + "\n")
