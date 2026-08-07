# 1. 文件路径
input_file = "D:/python-project/课后作业/input/laboratory_equipment_calibration.csv"
cleaned_file = "D:/python-project/课后作业/output/laboratory_equipment_calibration_cleaned.csv"
report_file = "D:/python-project/课后作业/output/laboratory_equipment_calibration_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

line_list = csv_text.splitlines()


# 3. 去除表头和空行
raw_record_list = []

for line in line_list:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "设备编号,使用状态,校准状态,剩余天数,校准费用":
        raw_record_list.append(clean_line)


# 4. 有效字段列表
equipment_id_list = []
usage_status_list = []
calibration_status_list = []
remaining_days_list = []
calibration_cost_list = []


# 5. 有效、无效记录
cleaned_record_list = []
invalid_record_list = []
invalid_reason_list = []


# 6. 业务分类列表
shutdown_risk_equipment_list = []              # 停用风险设备列表
priority_calibration_equipment_list = []       # 优先校准设备列表
stopped_pending_calibration_equipment_list = []  # 停用待校准设备列表
normal_equipment_list = []                     # 正常设备列表


# 7. 合计变量
total_calibration_cost = 0.0

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    equipment_id = parts[0].strip()
    usage_status = parts[1].strip()
    calibration_status = parts[2].strip()
    remaining_days_text = parts[3].strip()
    calibration_cost_text = parts[4].strip()

    if (
        equipment_id == ""
        or usage_status == ""
        or calibration_status == ""
        or remaining_days_text == ""
        or calibration_cost_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if usage_status != "使用中" and usage_status != "停用":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("使用状态不合法, 原始记录: " + raw_record)
        continue

    if (
        calibration_status != "有效"
        and calibration_status != "即将到期"
        and calibration_status != "已过期"
        and calibration_status != "未送检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("校准状态不合法, 原始记录: " + raw_record)
        continue

    if not remaining_days_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("剩余天数不是整数, 原始记录: " + raw_record)
        continue

    remaining_days = int(remaining_days_text)

    if not calibration_cost_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("校准费用不是数字, 原始记录: " + raw_record)
        continue

    calibration_cost = float(calibration_cost_text)

    if calibration_cost < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("校准费用小于0, 原始记录: " + raw_record)
        continue

    if (
        calibration_status == "有效"
        and remaining_days <= 30
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("有效状态的剩余天数必须大于30, 原始记录: " + raw_record)
        continue

    if (
        calibration_status == "即将到期"
        and (remaining_days < 0 or remaining_days > 30)
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("即将到期的剩余天数必须在0到30之间, 原始记录: " + raw_record)
        continue

    if (
        calibration_status == "已过期"
        and remaining_days >= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已过期的剩余天数必须小于0, 原始记录: " + raw_record)
        continue

    if (
        calibration_status == "未送检"
        and remaining_days != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未送检的剩余天数必须等于0, 原始记录: " + raw_record)
        continue

    equipment_id_list.append(equipment_id)
    usage_status_list.append(usage_status)
    calibration_status_list.append(calibration_status)
    remaining_days_list.append(remaining_days)
    calibration_cost_list.append(calibration_cost)

    cleaned_record_list.append(
        equipment_id
        + ","
        + usage_status
        + ","
        + calibration_status
        + ","
        + str(remaining_days)
        + ","
        + str(calibration_cost)
    )

    total_calibration_cost += calibration_cost

    if (
        usage_status == "使用中"
        and (calibration_status == "已过期" or calibration_status == "未送检")
    ):
        shutdown_risk_equipment_list.append(equipment_id)

    elif (
        usage_status == "使用中"
        and calibration_status == "即将到期"
    ):
        priority_calibration_equipment_list.append(equipment_id)

    elif (
        usage_status == "停用"
        and (calibration_status == "已过期" or calibration_status == "未送检" or calibration_status == "即将到期")
    ):
        stopped_pending_calibration_equipment_list.append(equipment_id)

    elif (
        (usage_status == "使用中" or usage_status == "停用")
        and calibration_status == "有效"
    ):
        normal_equipment_list.append(equipment_id)

raw_count = len(raw_record_list)
valid_count = len(cleaned_record_list)
invalid_count = len(invalid_record_list)

shutdown_risk_count = len(shutdown_risk_equipment_list)
priority_calibration_count = len(priority_calibration_equipment_list)
stopped_pending_calibration_count = len(stopped_pending_calibration_equipment_list)
normal_equipment_count = len(normal_equipment_list)

final_conclusion = ""

if invalid_count > 0:
    final_conclusion = "数据需要人工更正，统计结论不完整"
elif shutdown_risk_count > 0:
    final_conclusion = "存在使用中但校准失效设备，立即停用处理"
elif priority_calibration_count > 0:
    final_conclusion = "存在即将到期设备，安排优先校准"
elif stopped_pending_calibration_count > 0:
    final_conclusion = "停用设备存在校准待处理事项"
else:
    final_conclusion = "全部设备校准状态正常"

# 8. 控制台输出
print("实验室设备校准风险检查报告")
print("============================")
print("原始记录数量:", raw_count)
print("有效记录数量:", valid_count)
print("无效记录数量:", invalid_count)
print()

print("停用风险设备数量:", shutdown_risk_count)
print("优先校准设备数量:", priority_calibration_count)
print("停用待校准设备数量:", stopped_pending_calibration_count)
print("正常设备数量:", normal_equipment_count)
print()

print("有效校准费用合计:", total_calibration_cost)
print()

print("停用风险设备:", shutdown_risk_equipment_list)
print("优先校准设备:", priority_calibration_equipment_list)
print("停用待校准设备:", stopped_pending_calibration_equipment_list)
print("正常设备:", normal_equipment_list)
print()

print("无效记录:")
for invalid_record in invalid_record_list:
    print(invalid_record)

print()
print("无效原因:")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()
print("最终结论:", final_conclusion)

# 9. 输出 cleaned CSV
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("设备编号,使用状态,校准状态,剩余天数,校准费用\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")

# 10. 输出 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("实验室设备校准风险检查报告\n")
    f.write("============================\n")
    f.write("原始记录数量: " + str(raw_count) + "\n")
    f.write("有效记录数量: " + str(valid_count) + "\n")
    f.write("无效记录数量: " + str(invalid_count) + "\n")
    f.write("\n")

    f.write("停用风险设备数量: " + str(shutdown_risk_count) + "\n")
    f.write("优先校准设备数量: " + str(priority_calibration_count) + "\n")
    f.write("停用待校准设备数量: " + str(stopped_pending_calibration_count) + "\n")
    f.write("正常设备数量: " + str(normal_equipment_count) + "\n")
    f.write("\n")

    f.write("有效校准费用合计: " + str(total_calibration_cost) + "\n")
    f.write("\n")

    f.write("停用风险设备:\n")
    for equipment_id in shutdown_risk_equipment_list:
        f.write(equipment_id + "\n")

    f.write("\n")
    f.write("优先校准设备:\n")
    for equipment_id in priority_calibration_equipment_list:
        f.write(equipment_id + "\n")

    f.write("\n")
    f.write("停用待校准设备:\n")
    for equipment_id in stopped_pending_calibration_equipment_list:
        f.write(equipment_id + "\n")

    f.write("\n")
    f.write("正常设备:\n")
    for equipment_id in normal_equipment_list:
        f.write(equipment_id + "\n")

    f.write("\n")
    f.write("无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n")
    f.write("无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n")
    f.write("最终结论: " + final_conclusion + "\n")