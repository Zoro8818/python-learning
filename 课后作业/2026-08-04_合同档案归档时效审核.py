input_file = "D:/python-project/课后作业/input/contract_archive_timeliness_review.csv"
cleaned_file = "D:/python-project/课后作业/output/contract_archive_timeliness_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/contract_archive_timeliness_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "合同档案编号,合同结案状态,归档状态,实际归档处理天数":
        raw_record_list.append(clean_line)

# 有效、无效结果
valid_record_list = []
invalid_record_list = []
invalid_reason_list = []

# 有效记录分类：列表中保存合同档案编号
overdue_archive_review_list = []       # 超期归档复核
waiting_contract_closure_list = []      # 等待合同结案
waiting_archive_list = []               # 等待归档
archive_correction_list = []            # 归档补正
archive_completed_list = []             # 归档完成

for raw_record in raw_record_list:

    parts = raw_record.split(",")

    if len(parts) != 4:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误，原始记录：" + raw_record)
        continue

    contract_archive_number = parts[0].strip()
    contract_closure_status = parts[1].strip()
    archive_status = parts[2].strip()
    actual_archive_processing_days_text = parts[3].strip()

    if (
        contract_archive_number == ""
        or contract_closure_status == ""
        or archive_status == ""
        or actual_archive_processing_days_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        contract_closure_status != "未结案"
        and contract_closure_status != "已结案"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("合同结案状态不合法, 原始记录: " + raw_record)
        continue

    if (
        archive_status != "未归档"
        and archive_status != "已归档"
        and archive_status != "退回补正"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("归档状态不合法, 原始记录: " + raw_record)
        continue

    if not actual_archive_processing_days_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际归档处理天数不合法, 原始记录: " + raw_record)
        continue

    actual_archive_processing_days = int(actual_archive_processing_days_text)

    if actual_archive_processing_days < 0 or actual_archive_processing_days > 90:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际归档处理天数必须是0—90 的整数, 原始记录: " + raw_record)
        continue

    if (
        contract_closure_status == "未结案"
        and archive_status != "未归档"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("组合状态不合法, 原始记录: " + raw_record)
        continue

    if (
        archive_status == "未归档"
        and actual_archive_processing_days != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("归档状态为未归档时, 处理天数必须是0, 原始记录: " + raw_record)
        continue

    if(
        (
            archive_status == "已归档"
            or archive_status == "退回补正"
        )
        and actual_archive_processing_days <= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("归档状态为已归档或退回补正时, 处理天数必须大于 0, 原始记录: " + raw_record)
        continue

    clean_record = (
        contract_archive_number
        + ","
        + contract_closure_status
        + ","
        + archive_status
        + ","
        + str(actual_archive_processing_days)
    )

    valid_record_list.append(clean_record)

    if actual_archive_processing_days > 30:
        overdue_archive_review_list.append(contract_archive_number)
    elif (
        contract_closure_status == "未结案"
        and archive_status == "未归档"
    ):
        waiting_contract_closure_list.append(contract_archive_number)
    elif (
        contract_closure_status == "已结案"
        and archive_status == "未归档"
    ):
        waiting_archive_list.append(contract_archive_number)
    elif (
        contract_closure_status == "已结案"
        and archive_status == "退回补正"
    ):
        archive_correction_list.append(contract_archive_number)
    else:
        archive_completed_list.append(contract_archive_number)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

overdue_archive_review_count = len(overdue_archive_review_list)
waiting_contract_closure_count = len(waiting_contract_closure_list)
waiting_archive_count = len(waiting_archive_list)
archive_correction_count = len(archive_correction_list)
archive_completed_count = len(archive_completed_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "当前审核结果仅供参考，需修正后重新审核"
elif overdue_archive_review_count > 0:
    review_conclusion = "存在超期归档合同，需要优先复核"
elif archive_correction_count > 0:
    review_conclusion = "存在退回档案，需要补正后重新归档"
elif waiting_contract_closure_count > 0 or waiting_archive_count > 0:
    review_conclusion = "仍有合同档案未完成归档"
else:
    review_conclusion = "合同档案均已按时完成归档"

# 写入清洗后的有效 CSV
with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write("合同档案编号,合同结案状态,归档状态,实际归档处理天数\n")

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# 写入 TXT 审核报告
with open(report_file, "w", encoding="utf-8") as file:
    file.write("合同档案归档时效审核报告\n")
    file.write("=" * 40 + "\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")
    file.write("\n")

    file.write("超期归档复核数量: " + str(overdue_archive_review_count) + "\n")
    file.write("等待合同结案数量: " + str(waiting_contract_closure_count) + "\n")
    file.write("等待归档数量: " + str(waiting_archive_count) + "\n")
    file.write("归档补正数量: " + str(archive_correction_count) + "\n")
    file.write("归档完成数量: " + str(archive_completed_count) + "\n")
    file.write("\n")

    file.write("超期归档复核合同档案: " + str(overdue_archive_review_list) + "\n")
    file.write("等待合同结案合同档案: " + str(waiting_contract_closure_list) + "\n")
    file.write("等待归档合同档案: " + str(waiting_archive_list) + "\n")
    file.write("归档补正合同档案: " + str(archive_correction_list) + "\n")
    file.write("归档完成合同档案: " + str(archive_completed_list) + "\n")
    file.write("\n")

    file.write("无效记录原因:\n")

    if invalid_record_count == 0:
        file.write("无\n")
    else:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")

    file.write("\n")
    file.write("最终审核结论:\n")
    file.write(review_conclusion + "\n")


# 控制台输出
print("合同档案归档时效审核报告")
print("=" * 40)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("超期归档复核数量:", overdue_archive_review_count)
print("等待合同结案数量:", waiting_contract_closure_count)
print("等待归档数量:", waiting_archive_count)
print("归档补正数量:", archive_correction_count)
print("归档完成数量:", archive_completed_count)
print()

print("超期归档复核合同档案:", overdue_archive_review_list)
print("等待合同结案合同档案:", waiting_contract_closure_list)
print("等待归档合同档案:", waiting_archive_list)
print("归档补正合同档案:", archive_correction_list)
print("归档完成合同档案:", archive_completed_list)
print()

print("无效记录原因:")

if invalid_record_count == 0:
    print("无")
else:
    for invalid_reason in invalid_reason_list:
        print(invalid_reason)

print()
print("最终审核结论:")
print(review_conclusion)

print()
print("清洗后的有效数据已写入:", cleaned_file)
print("审核报告已写入:", report_file)