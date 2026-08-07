# 物流运输交接时效审核
# 机械输入端：只负责文件路径、读取、去表头空行、结果列表和核心循环入口
# 核心无效判断、有效保存、分类、统计与输出由你完成

input_file = "D:/python-project/课后作业/input/logistics_transport_handover_timeliness_review.csv"
cleaned_file = "D:/python-project/课后作业/output/logistics_transport_handover_timeliness_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/logistics_transport_handover_timeliness_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "运单编号,发运状态,交接状态,计划时效小时,实际运输小时":
        raw_record_list.append(clean_line)


# 有效、无效结果
valid_record_list = []           # 有效记录列表
invalid_record_list = []         # 无效记录列表
invalid_reason_list = []         # 无效原因列表


# 有效记录分类
timeliness_review_list = []      # 运输时效复核运单列表
rejection_handover_list = []     # 拒收交接处理运单列表
waiting_dispatch_list = []       # 等待发运运单列表
transport_follow_up_list = []    # 运输跟进运单列表
completed_handover_list = []     # 完成交接运单列表


# 核心处理循环
for raw_record in raw_record_list:

    parts = raw_record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误，原始记录：" + raw_record)
        continue

    waybill_number = parts[0].strip()
    dispatch_status = parts[1].strip()
    handover_status = parts[2].strip()
    planned_hours_text = parts[3].strip()
    actual_hours_text = parts[4].strip()

    if (
        waybill_number == ""
        or dispatch_status == ""
        or handover_status == ""
        or planned_hours_text == ""
        or actual_hours_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        dispatch_status != "未发运"
        and dispatch_status != "已发运"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("发运状态不合法, 原始记录: " + raw_record)
        continue

    if (
        handover_status != "未签收"
        and handover_status != "已签收"
        and handover_status != "拒收"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("交接状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not planned_hours_text.removeprefix("-").isdigit()
        or not actual_hours_text.removeprefix("-").isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("计划时效小时或实际运输小时不是有效数字, 原始记录: " + raw_record)
        continue

    planned_hours = int(planned_hours_text)
    actual_hours = int(actual_hours_text)

    if (
        planned_hours < 4
        or planned_hours > 72
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("计划时效小时必须是4—72 的整数, 原始记录: " + raw_record)
        continue

    if (
        actual_hours < 0
        or actual_hours > 120
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际运输小时必须是0—120 的整数, 原始记录: " + raw_record)
        continue

    if dispatch_status == "未发运" and handover_status != "未签收":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态组合不合法, 原始记录: " + raw_record)
        continue

    if dispatch_status == "未发运" and actual_hours != 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未发运实际运输小时必须等于 0, 原始记录: " + raw_record)
        continue

    if dispatch_status == "已发运" and actual_hours <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已发运实际运输小时必须大于 0,原始记录: " + raw_record)
        continue

    clean_record = (
        waybill_number
        + ","
        + dispatch_status
        + ","
        + handover_status
        + ","
        + str(planned_hours)
        + ","
        + str(actual_hours)
    )

    valid_record_list.append(clean_record)

    if actual_hours > planned_hours:
        timeliness_review_list.append(waybill_number)
    elif dispatch_status == "已发运" and handover_status == "拒收":
        rejection_handover_list.append(waybill_number)
    elif dispatch_status == "未发运" and handover_status == "未签收":
        waiting_dispatch_list.append(waybill_number)
    elif dispatch_status == "已发运" and handover_status == "未签收":
        transport_follow_up_list.append(waybill_number)
    else:
        completed_handover_list.append(waybill_number)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

timeliness_review_count = len(timeliness_review_list)
rejection_handover_count = len(rejection_handover_list)
waiting_dispatch_count = len(waiting_dispatch_list)
transport_follow_up_count = len(transport_follow_up_list)
completed_handover_count = len(completed_handover_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "当前审核结果仅供参考，需修正后重新审核"
elif timeliness_review_count > 0:
    review_conclusion = "存在超时运单，需要优先复核"
elif rejection_handover_count > 0:
    review_conclusion = "存在拒收运单，需要跟进交接"
elif waiting_dispatch_count > 0 or transport_follow_up_count > 0:
    review_conclusion = "仍有运单未完成交接"
else:
    review_conclusion = "运单均已按时完成交接"

# 写入清洗后的有效 CSV 文件
with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write("运单编号,发运状态,交接状态,计划时效小时,实际运输小时\n")

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# 写入 TXT 审核报告
with open(report_file, "w", encoding="utf-8") as file:
    file.write("物流运输交接时效审核报告\n")
    file.write("========================================\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")
    file.write("\n")

    file.write("运输时效复核数量: " + str(timeliness_review_count) + "\n")
    file.write("拒收交接处理数量: " + str(rejection_handover_count) + "\n")
    file.write("等待发运数量: " + str(waiting_dispatch_count) + "\n")
    file.write("运输跟进数量: " + str(transport_follow_up_count) + "\n")
    file.write("完成交接数量: " + str(completed_handover_count) + "\n")
    file.write("\n")

    file.write("运输时效复核运单: " + str(timeliness_review_list) + "\n")
    file.write("拒收交接处理运单: " + str(rejection_handover_list) + "\n")
    file.write("等待发运运单: " + str(waiting_dispatch_list) + "\n")
    file.write("运输跟进运单: " + str(transport_follow_up_list) + "\n")
    file.write("完成交接运单: " + str(completed_handover_list) + "\n")
    file.write("\n")

    file.write("无效记录及原因:\n")

    for invalid_reason in invalid_reason_list:
        file.write(invalid_reason + "\n")

    file.write("\n")
    file.write("最终审核结论:\n")
    file.write(review_conclusion + "\n")


# 控制台输出审核报告
print("物流运输交接时效审核报告")
print("========================================")

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("运输时效复核数量:", timeliness_review_count)
print("拒收交接处理数量:", rejection_handover_count)
print("等待发运数量:", waiting_dispatch_count)
print("运输跟进数量:", transport_follow_up_count)
print("完成交接数量:", completed_handover_count)
print()

print("运输时效复核运单:", timeliness_review_list)
print("拒收交接处理运单:", rejection_handover_list)
print("等待发运运单:", waiting_dispatch_list)
print("运输跟进运单:", transport_follow_up_list)
print("完成交接运单:", completed_handover_list)
print()

print("无效记录及原因:")

for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()
print("最终审核结论:")
print(review_conclusion)