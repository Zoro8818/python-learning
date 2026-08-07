input_file = "D:/python-project/课后作业/input/after_sales_repair_work_order_close_review.csv"
cleaned_file = "D:/python-project/课后作业/output/after_sales_repair_work_order_close_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/after_sales_repair_work_order_close_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "工单编号,维修状态,验证状态,实际维修小时,服务时限小时":
        raw_record_list.append(clean_line)


# 有效、无效结果
valid_record_list = []
invalid_record_list = []
invalid_reason_list = []


# 有效记录分类
overtime_review_list = []            # 超时维修复核
waiting_repair_list = []             # 等待维修
rework_list = []                     # 返修处理
waiting_verification_list = []       # 等待验证
closable_list = []                   # 可关单


for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    work_order_id = parts[0].strip()
    repair_status = parts[1].strip()
    verification_status = parts[2].strip()
    actual_repair_hours_text = parts[3].strip()
    service_limit_hours_text = parts[4].strip()

    if (
        work_order_id == ""
        or repair_status == ""
        or verification_status == ""
        or actual_repair_hours_text == ""
        or service_limit_hours_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        repair_status != "未修复"
        and repair_status != "已修复"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("维修状态不合法, 原始记录: " + raw_record)
        continue

    if (
        verification_status != "待验证"
        and verification_status != "通过"
        and verification_status != "不通过"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("验证状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not actual_repair_hours_text.removeprefix("-").isdigit()
        or not service_limit_hours_text.removeprefix("-").isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际维修小时或服务时限小时不是整数, 原始记录: " + raw_record)
        continue

    actual_repair_hours = int(actual_repair_hours_text)
    service_limit_hours = int(service_limit_hours_text)

    if actual_repair_hours < 0 or actual_repair_hours > 720:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际维修小时必须是0—720 的整数, 原始记录: " + raw_record)
        continue

    if service_limit_hours < 4 or service_limit_hours > 72:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("服务时限小时必须是4—72 的整数, 原始记录: " + raw_record)
        continue

    if (
        repair_status == "未修复"
        and verification_status != "待验证"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态组合不合理, 原始记录: " + raw_record)
        continue

    if (
        repair_status == "未修复"
        and actual_repair_hours != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态与数字关系不合理, 原始记录: " + raw_record)
        continue

    if (
        repair_status == "已修复"
        and actual_repair_hours <= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态与数字关系不合理, 原始记录: " + raw_record)
        continue

    clean_record = (
        work_order_id
        + ","
        + repair_status
        + ","
        + verification_status
        + ","
        + str(actual_repair_hours)
        + ","
        + str(service_limit_hours)
    )

    valid_record_list.append(clean_record)

    if actual_repair_hours > service_limit_hours:
        overtime_review_list.append(work_order_id)
    elif repair_status == "未修复" and verification_status == "待验证":
        waiting_repair_list.append(work_order_id)
    elif repair_status == "已修复" and verification_status == "不通过":
        rework_list.append(work_order_id)
    elif repair_status == "已修复" and verification_status == "待验证":
        waiting_verification_list.append(work_order_id)
    else:
        closable_list.append(work_order_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

overtime_review_count = len(overtime_review_list)
waiting_repair_count = len(waiting_repair_list)
rework_count = len(rework_list)
waiting_verification_count = len(waiting_verification_list)
closable_count = len(closable_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "存在无效数据，当前关单审核结果仅供参考，需要修正后重新审核"
elif overtime_review_count > 0:
    review_conclusion = "存在超时维修工单，需要优先复核"
elif rework_count > 0:
    review_conclusion = "存在验证不通过工单，需要安排返修"
elif waiting_repair_count > 0:
    review_conclusion = "存在未修复工单，需要继续维修"
elif waiting_verification_count > 0:
    review_conclusion = "存在已修复待验证工单，需要完成验证"
else:
    review_conclusion = "所有工单均已通过验证，可以关单"

# ============================================================
# 控制台输出
# ============================================================

print("售后维修工单关单审核报告")
print("=" * 32)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)

print()

print("超时维修复核数量:", overtime_review_count)
print("等待维修数量:", waiting_repair_count)
print("返修处理数量:", rework_count)
print("等待验证数量:", waiting_verification_count)
print("可关单数量:", closable_count)

print()

print("超时维修复核工单:", overtime_review_list)
print("等待维修工单:", waiting_repair_list)
print("返修处理工单:", rework_list)
print("等待验证工单:", waiting_verification_list)
print("可关单工单:", closable_list)

print()

print("无效记录:")

if invalid_record_count > 0:
    for invalid_reason in invalid_reason_list:
        print(invalid_reason)
else:
    print("无")

print()

print("最终结论:")
print(review_conclusion)


# ============================================================
# cleaned CSV 输出
# ============================================================

with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write("工单编号,维修状态,验证状态,实际维修小时,服务时限小时\n")

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# ============================================================
# TXT 报告输出
# ============================================================

with open(report_file, "w", encoding="utf-8") as file:
    file.write("售后维修工单关单审核报告\n")
    file.write("=" * 32 + "\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")

    file.write("\n")

    file.write("超时维修复核数量: " + str(overtime_review_count) + "\n")
    file.write("等待维修数量: " + str(waiting_repair_count) + "\n")
    file.write("返修处理数量: " + str(rework_count) + "\n")
    file.write("等待验证数量: " + str(waiting_verification_count) + "\n")
    file.write("可关单数量: " + str(closable_count) + "\n")

    file.write("\n")

    file.write("超时维修复核工单: " + str(overtime_review_list) + "\n")
    file.write("等待维修工单: " + str(waiting_repair_list) + "\n")
    file.write("返修处理工单: " + str(rework_list) + "\n")
    file.write("等待验证工单: " + str(waiting_verification_list) + "\n")
    file.write("可关单工单: " + str(closable_list) + "\n")

    file.write("\n")

    file.write("无效记录:\n")

    if invalid_record_count > 0:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")
    else:
        file.write("无\n")

    file.write("\n")

    file.write("最终结论:\n")
    file.write(review_conclusion + "\n")