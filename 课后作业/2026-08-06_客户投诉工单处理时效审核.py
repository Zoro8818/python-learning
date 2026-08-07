input_file = "D:/python-project/课后作业/input/complaint_work_order_response_review.csv"
cleaned_file = "D:/python-project/课后作业/output/complaint_work_order_response_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/complaint_work_order_response_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    raw_record = line.strip()

    if (
        raw_record != ""
        and raw_record != "投诉工单号,受理状态,处理结果,首次响应小时"
    ):
        raw_record_list.append(raw_record)

# 有效、无效结果
valid_record_list = []
invalid_record_list = []
invalid_reason_list = []

# 有效记录分类
first_response_timeout_review_list = []       # 首次响应超时复核列表
waiting_complaint_acceptance_list = []        # 等待投诉受理列表
waiting_complaint_processing_list = []        # 等待投诉处理列表
complaint_rejection_follow_up_list = []       # 投诉驳回跟进列表
complaint_processing_completed_list = []      # 投诉处理完成列表

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 4:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录：" + raw_record)
        continue

    complaint_work_order_number = parts[0].strip()
    acceptance_status = parts[1].strip()
    processing_result = parts[2].strip()
    first_response_hours_text = parts[3].strip()

    if (
        complaint_work_order_number == ""
        or acceptance_status == ""
        or processing_result == ""
        or first_response_hours_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        acceptance_status != "未受理"
        and acceptance_status != "已受理"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("受理状态不合法, 原始记录: " + raw_record)
        continue

    if (
        processing_result != "待处理"
        and processing_result != "已解决"
        and processing_result != "驳回"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("处理结果不合法, 原始记录: " + raw_record)
        continue

    if not first_response_hours_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("首次响应小时不是有效整数, 原始记录: " + raw_record)
        continue

    first_response_hours = int(first_response_hours_text)

    if (
        first_response_hours < 0
        or first_response_hours > 72
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("首次响应小时必须是0—72 的整数, 原始记录: " + raw_record)
        continue

    if (
        acceptance_status == "未受理"
        and processing_result != "待处理"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("组合状态无效, 原始记录: " + raw_record)
        continue

    if (
        acceptance_status == "未受理"
        and first_response_hours != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未受理时首次响应小时必须等于 0, 原始记录: " + raw_record)
        continue

    if (
        acceptance_status == "已受理"
        and first_response_hours <= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已受理时首次响应小时必须大于 0, 原始记录: " + raw_record)
        continue

    clean_record = (
        complaint_work_order_number
        + ","
        + acceptance_status
        + ","
        + processing_result
        + ","
        + str(first_response_hours)
    )

    valid_record_list.append(clean_record)

    if first_response_hours > 24:
        first_response_timeout_review_list.append(complaint_work_order_number)
    elif (
        acceptance_status == "未受理"
        and processing_result == "待处理"
    ):
        waiting_complaint_acceptance_list.append(complaint_work_order_number)
    elif (
        acceptance_status == "已受理"
        and processing_result == "待处理"
    ):
        waiting_complaint_processing_list.append(complaint_work_order_number)
    elif (
        acceptance_status == "已受理"
        and processing_result == "驳回"
    ):
        complaint_rejection_follow_up_list.append(complaint_work_order_number)
    else:
        complaint_processing_completed_list.append(complaint_work_order_number)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

first_response_timeout_review_count = len(first_response_timeout_review_list)
waiting_complaint_acceptance_count = len(waiting_complaint_acceptance_list)
waiting_complaint_processing_count = len(waiting_complaint_processing_list)
complaint_rejection_follow_up_count = len(complaint_rejection_follow_up_list)
complaint_processing_completed_count = len(complaint_processing_completed_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "当前审核结果仅供参考，需修正后重新审核"
elif first_response_timeout_review_count > 0:
    review_conclusion = "存在响应超时工单，需要优先复核"
elif complaint_rejection_follow_up_count > 0:
    review_conclusion = "存在被驳回投诉，需要继续跟进"
elif waiting_complaint_acceptance_count > 0 or waiting_complaint_processing_count > 0:
    review_conclusion = "仍有投诉工单未完成处理"
else:
    review_conclusion = "投诉工单均已完成处理"

print("客户投诉工单处理时效审核报告")
print("=" * 40)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)

print()

print("首次响应超时复核数量:", first_response_timeout_review_count)
print("等待投诉受理数量:", waiting_complaint_acceptance_count)
print("等待投诉处理数量:", waiting_complaint_processing_count)
print("投诉驳回跟进数量:", complaint_rejection_follow_up_count)
print("投诉处理完成数量:", complaint_processing_completed_count)

print()

print("首次响应超时复核工单:", first_response_timeout_review_list)
print("等待投诉受理工单:", waiting_complaint_acceptance_list)
print("等待投诉处理工单:", waiting_complaint_processing_list)
print("投诉驳回跟进工单:", complaint_rejection_follow_up_list)
print("投诉处理完成工单:", complaint_processing_completed_list)

print()

print("无效记录:")
for invalid_record in invalid_record_list:
    print(invalid_record)

print()

print("无效原因:")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()

print("最终审核结论:")
print(review_conclusion)

with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write("投诉工单号,受理状态,处理结果,首次响应小时\n")

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")

with open(report_file, "w", encoding="utf-8") as file:
    file.write("客户投诉工单处理时效审核报告\n")
    file.write("=" * 40 + "\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")

    file.write("\n")

    file.write(
        "首次响应超时复核数量: "
        + str(first_response_timeout_review_count)
        + "\n"
    )
    file.write(
        "等待投诉受理数量: "
        + str(waiting_complaint_acceptance_count)
        + "\n"
    )
    file.write(
        "等待投诉处理数量: "
        + str(waiting_complaint_processing_count)
        + "\n"
    )
    file.write(
        "投诉驳回跟进数量: "
        + str(complaint_rejection_follow_up_count)
        + "\n"
    )
    file.write(
        "投诉处理完成数量: "
        + str(complaint_processing_completed_count)
        + "\n"
    )

    file.write("\n")

    file.write(
        "首次响应超时复核工单: "
        + str(first_response_timeout_review_list)
        + "\n"
    )
    file.write(
        "等待投诉受理工单: "
        + str(waiting_complaint_acceptance_list)
        + "\n"
    )
    file.write(
        "等待投诉处理工单: "
        + str(waiting_complaint_processing_list)
        + "\n"
    )
    file.write(
        "投诉驳回跟进工单: "
        + str(complaint_rejection_follow_up_list)
        + "\n"
    )
    file.write(
        "投诉处理完成工单: "
        + str(complaint_processing_completed_list)
        + "\n"
    )

    file.write("\n")

    file.write("无效记录:\n")

    for invalid_record in invalid_record_list:
        file.write(invalid_record + "\n")

    file.write("\n")

    file.write("无效原因:\n")

    for invalid_reason in invalid_reason_list:
        file.write(invalid_reason + "\n")

    file.write("\n")

    file.write("最终审核结论:\n")
    file.write(review_conclusion + "\n")