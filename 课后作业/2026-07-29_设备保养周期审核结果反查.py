input_file = "D:/python-project/课后作业/input/equipment_maintenance_cycle_review.csv"
cleaned_file = "D:/python-project/课后作业/output/equipment_maintenance_cycle_review_20260729_cleaned.csv"
report_file = "D:/python-project/课后作业/output/equipment_maintenance_cycle_review_20260729_report.txt"


with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()


lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "设备编号,使用状态,保养状态,已运行小时,保养周期小时"
    ):
        raw_record_list.append(clean_line)


# 有效、无效结果
valid_record_list = []          # 有效记录列表
invalid_record_list = []        # 无效记录列表
invalid_reason_list = []        # 无效原因列表


# 有效记录分类
overdue_maintenance_list = []          # 超周期停机保养列表
due_stop_maintenance_list = []         # 到期停机保养列表
due_arrange_maintenance_list = []      # 到期安排保养列表
post_maintenance_running_list = []     # 保养后投入运行列表
post_maintenance_standby_list = []     # 保养后备用列表
continue_running_list = []             # 继续运行列表
standby_storage_list = []              # 备用停放列表


for raw_record in raw_record_list:
    parts = raw_record.split(",")

    # 从这里开始写核心判断代码
    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    equipment_id = parts[0].strip()  # 设备编号
    usage_status = parts[1].strip()  # 使用状态
    maintenance_status = parts[2].strip()  # 保养状态
    running_hours_text = parts[3].strip()  # 已运行小时文本
    maintenance_cycle_hours_text = parts[4].strip()  # 保养周期小时文本

    if (
        equipment_id == ""
        or usage_status == ""
        or maintenance_status == ""
        or running_hours_text == ""
        or maintenance_cycle_hours_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if usage_status != "在用" and usage_status != "停机":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("使用状态不合法, 原始记录: " + raw_record)
        continue

    if (
        maintenance_status != "未到期"
        and maintenance_status != "待保养"
        and maintenance_status != "已保养"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("保养状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not running_hours_text.removeprefix("-").isdigit()
        or not maintenance_cycle_hours_text.removeprefix("-").isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已运行小时或保养周期小时不是整数, 原始记录: " + raw_record)
        continue

    running_hours = int(running_hours_text)
    maintenance_cycle_hours = int(maintenance_cycle_hours_text)

    if running_hours < 0 or running_hours > 2000:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已运行小时必须是0—2000 的整数, 原始记录: " + raw_record)
        continue

    if maintenance_cycle_hours <100 or maintenance_cycle_hours > 1000:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("保养周期小时必须是100—1000 的整数, 原始记录: " + raw_record)
        continue

    if maintenance_status == "未到期" and running_hours >= maintenance_cycle_hours:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("保养状态与数字关系不合理, 原始记录: " + raw_record)
        continue

    if maintenance_status == "待保养" and running_hours < maintenance_cycle_hours:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("保养状态与数字关系不合理, 原始记录: " + raw_record)
        continue

    if maintenance_status == "已保养" and running_hours != 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("保养状态与数字关系不合理, 原始记录: " + raw_record)
        continue

    clean_record = (
            equipment_id + ","
            + usage_status + ","
            + maintenance_status + ","
            + str(running_hours) + ","
            + str(maintenance_cycle_hours)
    )

    valid_record_list.append(clean_record)

    if running_hours > maintenance_cycle_hours:
        overdue_maintenance_list.append(equipment_id)
    elif running_hours == maintenance_cycle_hours and usage_status == "在用":
        due_stop_maintenance_list.append(equipment_id)
    elif running_hours == maintenance_cycle_hours and usage_status == "停机":
        due_arrange_maintenance_list.append(equipment_id)
    elif maintenance_status == "已保养" and usage_status == "在用":
        post_maintenance_running_list.append(equipment_id)
    elif maintenance_status == "已保养" and usage_status == "停机":
        post_maintenance_standby_list.append(equipment_id)
    elif maintenance_status == "未到期" and usage_status == "在用":
        continue_running_list.append(equipment_id)
    else:
        standby_storage_list.append(equipment_id)

# 数量统计
raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

overdue_maintenance_count = len(overdue_maintenance_list)
due_stop_maintenance_count = len(due_stop_maintenance_list)
due_arrange_maintenance_count = len(due_arrange_maintenance_list)
post_maintenance_running_count = len(post_maintenance_running_list)
post_maintenance_standby_count = len(post_maintenance_standby_list)
continue_running_count = len(continue_running_list)
standby_storage_count = len(standby_storage_list)


# 整批业务结论
if invalid_record_count > 0:
    business_conclusion = (
        "存在无效数据，当前审核结果仅供参考，需要修正后重新审核"
    )

elif overdue_maintenance_count > 0:
    business_conclusion = (
        "存在超周期设备，需要优先停机并安排保养"
    )

elif due_stop_maintenance_count > 0 or due_arrange_maintenance_count > 0:
    business_conclusion = (
        "存在已到保养周期的设备，需要及时安排保养"
    )

else:
    business_conclusion = (
        "当前设备保养周期审核未发现到期或超周期风险"
    )


# 控制台输出
print("设备保养周期审核报告")
print("=" * 30)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)

print()

print("超周期停机保养数量:", overdue_maintenance_count)
print("到期停机保养数量:", due_stop_maintenance_count)
print("到期安排保养数量:", due_arrange_maintenance_count)
print("保养后投入运行数量:", post_maintenance_running_count)
print("保养后备用数量:", post_maintenance_standby_count)
print("继续运行数量:", continue_running_count)
print("备用停放数量:", standby_storage_count)

print()

print("超周期停机保养设备:", overdue_maintenance_list)
print("到期停机保养设备:", due_stop_maintenance_list)
print("到期安排保养设备:", due_arrange_maintenance_list)
print("保养后投入运行设备:", post_maintenance_running_list)
print("保养后备用设备:", post_maintenance_standby_list)
print("继续运行设备:", continue_running_list)
print("备用停放设备:", standby_storage_list)

print()

print("无效记录:")

for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()
print("业务结论:", business_conclusion)


# 输出清洗后的 CSV 文件
with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write(
        "设备编号,使用状态,保养状态,已运行小时,保养周期小时\n"
    )

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# 输出 TXT 审核报告
with open(report_file, "w", encoding="utf-8") as file:
    file.write("设备保养周期审核报告\n")
    file.write("=" * 30 + "\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")

    file.write("\n")

    file.write(
        "超周期停机保养数量: "
        + str(overdue_maintenance_count)
        + "\n"
    )
    file.write(
        "到期停机保养数量: "
        + str(due_stop_maintenance_count)
        + "\n"
    )
    file.write(
        "到期安排保养数量: "
        + str(due_arrange_maintenance_count)
        + "\n"
    )
    file.write(
        "保养后投入运行数量: "
        + str(post_maintenance_running_count)
        + "\n"
    )
    file.write(
        "保养后备用数量: "
        + str(post_maintenance_standby_count)
        + "\n"
    )
    file.write(
        "继续运行数量: "
        + str(continue_running_count)
        + "\n"
    )
    file.write(
        "备用停放数量: "
        + str(standby_storage_count)
        + "\n"
    )

    file.write("\n")

    file.write(
        "超周期停机保养设备: "
        + str(overdue_maintenance_list)
        + "\n"
    )
    file.write(
        "到期停机保养设备: "
        + str(due_stop_maintenance_list)
        + "\n"
    )
    file.write(
        "到期安排保养设备: "
        + str(due_arrange_maintenance_list)
        + "\n"
    )
    file.write(
        "保养后投入运行设备: "
        + str(post_maintenance_running_list)
        + "\n"
    )
    file.write(
        "保养后备用设备: "
        + str(post_maintenance_standby_list)
        + "\n"
    )
    file.write(
        "继续运行设备: "
        + str(continue_running_list)
        + "\n"
    )
    file.write(
        "备用停放设备: "
        + str(standby_storage_list)
        + "\n"
    )

    file.write("\n")
    file.write("无效记录:\n")

    for invalid_reason in invalid_reason_list:
        file.write(invalid_reason + "\n")

    file.write("\n")
    file.write("业务结论: " + business_conclusion + "\n")

