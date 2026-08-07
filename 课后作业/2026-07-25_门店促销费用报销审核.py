# 1. 文件路径
input_file = "D:/python-project/课后作业/input/store_promotion_expense_claims.csv"
cleaned_file = "D:/python-project/课后作业/output/store_promotion_expense_claims_cleaned.csv"
report_file = "D:/python-project/课后作业/output/store_promotion_expense_claims_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 3. 按行拆分
lines = csv_text.splitlines()


# 4. 去掉表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "报销单号,活动状态,发票状态,预算金额,报销申请金额"
    ):
        raw_record_list.append(clean_line)


# 5. 有效字段列表
valid_reimbursement_id_list = []
valid_activity_status_list = []
valid_invoice_status_list = []
valid_budget_amount_list = []
valid_requested_amount_list = []


# 6. 有效完整记录
cleaned_record_list = []


# 7. 无效记录和原因
invalid_record_list = []
invalid_reason_list = []


# 8. 业务分类列表
waiting_activity_end_list = []          #待活动结束报销单列表
missing_invoice_list = []               #凭证缺失报销单列表
pending_invoice_list = []               #待补凭证报销单列表
over_budget_review_list = []            #超预算复核报销单列表
reimbursable_list = []                  #可报销报销单列表


# 9. 金额合计
total_budget_amount = 0
total_requested_amount = 0


# 10. 逐条处理记录
for raw_record in raw_record_list:
    parts = raw_record.split(",")

    # 从这里开始编写核心无效判断
    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    reimbursement_id = parts[0].strip()
    activity_status = parts[1].strip()
    invoice_status = parts[2].strip()
    budget_amount_text = parts[3].strip()
    requested_amount_text = parts[4].strip()

    if (
        reimbursement_id == ""
        or activity_status == ""
        or invoice_status == ""
        or budget_amount_text == ""
        or requested_amount_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        activity_status != "已结束"
        and activity_status != "未结束"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("活动状态不合法, 原始记录: " + raw_record)
        continue

    if (
        invoice_status != "齐全"
        and invoice_status != "待补"
        and invoice_status != "缺失"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("发票状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not budget_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
        or not requested_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("预算金额或报销申请金额不是合法数字, 原始记录: " + raw_record)
        continue

    budget_amount = float(budget_amount_text)
    requested_amount = float(requested_amount_text)

    if (
        budget_amount <= 0
        or requested_amount <= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("预算金额或报销申请金额必须大于 0, 原始记录: " + raw_record)
        continue

    if (
        activity_status == "未结束"
        and invoice_status == "齐全"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    if (
        activity_status == "未结束"
        and invoice_status == "缺失"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    valid_reimbursement_id_list.append(reimbursement_id)
    valid_activity_status_list.append(activity_status)
    valid_invoice_status_list.append(invoice_status)
    valid_budget_amount_list.append(budget_amount)
    valid_requested_amount_list.append(requested_amount)

    total_budget_amount += budget_amount
    total_requested_amount += requested_amount

    cleaned_record_list.append(
        reimbursement_id
        + ","
        + activity_status
        + ","
        + invoice_status
        + ","
        + str(budget_amount)
        + ","
        + str(requested_amount)
    )

    if (
        activity_status == "未结束"
        and invoice_status == "待补"
    ):
        waiting_activity_end_list.append(reimbursement_id)
    elif (
        activity_status == "已结束"
        and invoice_status == "缺失"
    ):
        missing_invoice_list.append(reimbursement_id)
    elif (
        activity_status == "已结束"
        and invoice_status == "待补"
    ):
        pending_invoice_list.append(reimbursement_id)
    elif (
        activity_status == "已结束"
        and invoice_status == "齐全"
        and requested_amount > budget_amount
    ):
        over_budget_review_list.append(reimbursement_id)
    elif (
        activity_status == "已结束"
        and invoice_status == "齐全"
        and requested_amount <= budget_amount
    ):
        reimbursable_list.append(reimbursement_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)

waiting_activity_end_count = len(waiting_activity_end_list)
missing_invoice_count = len(missing_invoice_list)
pending_invoice_count = len(pending_invoice_list)
over_budget_review_count = len(over_budget_review_list)
reimbursable_count = len(reimbursable_list)

final_conclusion = ""
if invalid_record_count > 0:
    final_conclusion = "存在无效数据，当前报销审核结果不完整"
elif missing_invoice_count > 0:
    final_conclusion = "存在发票缺失，需补齐凭证后再审核"
elif over_budget_review_count > 0:
    final_conclusion = "存在超预算申请，需要进一步复核"
elif waiting_activity_end_count > 0:
    final_conclusion = "存在尚未结束的促销活动，暂不能完成报销审核"
elif pending_invoice_count > 0:
    final_conclusion = "存在待补凭证的报销单"
else:
    final_conclusion = "所有有效报销单均可正常报销"

# 11. 控制台输出
print("门店促销费用报销审核报告")
print("=" * 30)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("待活动结束数量:", waiting_activity_end_count)
print("凭证缺失数量:", missing_invoice_count)
print("待补凭证数量:", pending_invoice_count)
print("超预算复核数量:", over_budget_review_count)
print("可报销数量:", reimbursable_count)
print()

print("有效预算金额合计:", total_budget_amount)
print("有效报销申请金额合计:", total_requested_amount)
print()

print("待活动结束报销单:", waiting_activity_end_list)
print("凭证缺失报销单:", missing_invoice_list)
print("待补凭证报销单:", pending_invoice_list)
print("超预算复核报销单:", over_budget_review_list)
print("可报销报销单:", reimbursable_list)
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


# 12. 输出 cleaned CSV
with open(cleaned_file, "w", encoding="utf-8") as f:
    f.write("报销单号,活动状态,发票状态,预算金额,报销申请金额\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 13. 输出 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("门店促销费用报销审核报告\n")
    f.write("=" * 30 + "\n")

    f.write("原始记录数量: " + str(raw_record_count) + "\n")
    f.write("有效记录数量: " + str(valid_record_count) + "\n")
    f.write("无效记录数量: " + str(invalid_record_count) + "\n\n")

    f.write("待活动结束数量: " + str(waiting_activity_end_count) + "\n")
    f.write("凭证缺失数量: " + str(missing_invoice_count) + "\n")
    f.write("待补凭证数量: " + str(pending_invoice_count) + "\n")
    f.write("超预算复核数量: " + str(over_budget_review_count) + "\n")
    f.write("可报销数量: " + str(reimbursable_count) + "\n\n")

    f.write("有效预算金额合计: " + str(total_budget_amount) + "\n")
    f.write("有效报销申请金额合计: " + str(total_requested_amount) + "\n\n")

    f.write("待活动结束报销单: " + str(waiting_activity_end_list) + "\n")
    f.write("凭证缺失报销单: " + str(missing_invoice_list) + "\n")
    f.write("待补凭证报销单: " + str(pending_invoice_list) + "\n")
    f.write("超预算复核报销单: " + str(over_budget_review_list) + "\n")
    f.write("可报销报销单: " + str(reimbursable_list) + "\n\n")

    f.write("无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n最终结论: " + final_conclusion + "\n")