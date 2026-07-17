raw_record_list = [
    "张敏,8,8",
    "李强,7.5,8",
    "王芳,9,8",
    "赵雷,8",
    "陈静,,7",
    "周伟,abc,8",
    "刘洋,8,xyz"
]

employee_name_list = []            # 有效员工姓名列表
planned_hours_list = []            # 有效计划工时列表
actual_hours_list = []             # 有效实际工时列表
hours_difference_list = []         # 工时差异列表

invalid_record_list = []
invalid_reason_list = []

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
            not planned_hours_text.replace(",", "", 1).isdigit()
            or not actual_hours_text.replace(",", "", 1).isdigit()
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

            

