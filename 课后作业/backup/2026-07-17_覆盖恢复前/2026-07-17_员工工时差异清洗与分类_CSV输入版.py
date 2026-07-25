input_file_path = r"D:\python-project\课后作业\input\employee_hours.csv"
cleaned_file_path = r"D:\python-project\课后作业\output\employee_hours_cleaned.csv"
report_file_path = r"D:\python-project\课后作业\output\employee_hours_report.txt"

raw_record_list = []

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "员工姓名,计划工时,实际工时":
        raw_record_list.append(clean_line)

employee_name_list = []            # 有效员工姓名列表
planned_hours_list = []            # 有效计划工时列表
actual_hours_list = []             # 有效实际工时列表
hours_difference_list = []         # 工时差异列表

invalid_record_list = []
invalid_reason_list = []
cleaned_record_list = []

overtime_employee_list = []        # 超出计划工时员工列表
on_plan_employee_list = []         # 按计划完成员工列表
under_hours_employee_list = []     # 未达到计划工时员工列表

total_planned_hours = 0
total_actual_hours = 0
total_hours_difference = 0

highest_hours_difference = 0
highest_difference_employee = ""

lowest_hours_difference = 0
lowest_difference_employee = ""

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录：" + record)

    else:
        employee_name = parts[0].strip()
        planned_hours_text = parts[1].strip()
        actual_hours_text = parts[2].strip()

        if (
            employee_name == ""
            or planned_hours_text == ""
            or actual_hours_text == ""
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("字段为空，原始记录：" + record)

        elif (
            not planned_hours_text.replace(".", "", 1).isdigit()
            or not actual_hours_text.replace(".", "", 1).isdigit()
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("工时不是数字，原始记录：" + record)

        else:
            planned_hours = float(planned_hours_text)
            actual_hours = float(actual_hours_text)
            hours_difference = actual_hours - planned_hours

            employee_name_list.append(employee_name)
            planned_hours_list.append(planned_hours)
            actual_hours_list.append(actual_hours)
            hours_difference_list.append(hours_difference)

            if len(hours_difference_list) == 1:
                highest_hours_difference = hours_difference
                highest_difference_employee = employee_name

                lowest_hours_difference = hours_difference
                lowest_difference_employee = employee_name

            else:
                if hours_difference > highest_hours_difference:
                    highest_hours_difference = hours_difference
                    highest_difference_employee = employee_name

                if hours_difference < lowest_hours_difference:
                    lowest_hours_difference = hours_difference
                    lowest_difference_employee = employee_name

            total_planned_hours += planned_hours
            total_actual_hours += actual_hours
            total_hours_difference += hours_difference

            cleaned_record_list.append(
                employee_name
                + ","
                + str(planned_hours)
                + ","
                + str(actual_hours)
                + ","
                + str(hours_difference)
            )
            if hours_difference > 0:
                overtime_employee_list.append(employee_name)
            elif hours_difference == 0:
                on_plan_employee_list.append(employee_name)
            else:
                under_hours_employee_list.append(employee_name)

print("原始记录数量：", len(raw_record_list))
print("有效记录数量：", len(employee_name_list))
print("无效记录数量：", len(invalid_record_list))

print("\n无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print("\n无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print("\n超出计划工时员工：", overtime_employee_list)
print("按计划完成员工：", on_plan_employee_list)
print("未达到计划工时员工：", under_hours_employee_list)

print("\n计划工时合计：", total_planned_hours)
print("实际工时合计：", total_actual_hours)
print("工时差异合计：", total_hours_difference)

print("\n清洗后的有效记录：")
for cleaned_record in cleaned_record_list:
    print(cleaned_record)

if len(employee_name_list) == 0:
    print("\n没有有效数据，无法计算最大和最小工时差异")

else:
    print("\n最大工时差异员工：", highest_difference_employee)
    print("最大工时差异：", highest_hours_difference)

    print("最小工时差异员工：", lowest_difference_employee)
    print("最小工时差异：", lowest_hours_difference)