# 1. 文件路径
input_file = "D:/python-project/课后作业/input/purchase_material_payment.csv"

cleaned_file = "D:/python-project/课后作业/output/purchase_material_payment_cleaned.csv"

report_file = "D:/python-project/课后作业/output/purchase_material_payment_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

line_list = csv_text.splitlines()


# 3. 保存去除表头和空行后的原始记录
raw_record_list = []

for line in line_list:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "采购单号,到货状态,验收状态,可用预算,付款申请金额":
        raw_record_list.append(clean_line)

# 有效字段列表
valid_purchase_order_id_list = []       #有效采购单号列表
valid_delivery_status_list = []         #有效到货状态列表
valid_inspection_status_list = []       #有效验收状态列表
valid_available_budget_list = []        #有效可用预算列表
valid_payment_amount_list = []          #有效付款申请金额列表

# 4. 无效记录和有效记录
invalid_record_list = []
invalid_reason_list = []

cleaned_record_list = []


# 5. 五类业务结果
prepayment_review_record_list = []      #预付款复核记录列表
quality_rejection_record_list = []      #质量不合格记录列表
pending_inspection_record_list = []     #待验收记录列表
insufficient_budget_record_list = []    #预算不足记录列表
payment_release_record_list = []        #可付款记录列表


# 6. 最终业务结论
business_conclusion = ""

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    purchase_order_id = parts[0].strip()
    delivery_status = parts[1].strip()
    inspection_status = parts[2].strip()
    available_budget_text = parts[3].strip()
    payment_amount_text = parts[4].strip()

    if (
        purchase_order_id == ""
        or delivery_status == ""
        or inspection_status == ""
        or available_budget_text == ""
        or payment_amount_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if delivery_status != "已到货" and delivery_status != "未到货":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("到货状态不合法, 原始记录: " + raw_record)
        continue

    if (
        inspection_status != "合格"
        and inspection_status != "不合格"
        and inspection_status != "待检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("验收状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not available_budget_text.removeprefix("-").replace(".", "", 1).isdigit()
        or not payment_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("可用预算或付款申请金额不是数字, 原始记录: " + raw_record)
        continue

    available_budget = float(available_budget_text)
    payment_amount = float(payment_amount_text)

    if available_budget < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("可用预算必须大于等于 0, 原始记录: " + raw_record)
        continue

    if payment_amount <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("付款申请金额必须大于 0, 原始记录: " + raw_record)
        continue

    if (
        delivery_status == "未到货"
        and inspection_status == "合格"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态矛盾, 原始记录: " + raw_record)
        continue

    if (
        delivery_status == "未到货"
        and inspection_status == "不合格"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("状态矛盾, 原始记录: " + raw_record)
        continue

    valid_purchase_order_id_list.append(purchase_order_id)
    valid_delivery_status_list.append(delivery_status)
    valid_inspection_status_list.append(inspection_status)
    valid_available_budget_list.append(available_budget)
    valid_payment_amount_list.append(payment_amount)

    cleaned_record_list.append(
            purchase_order_id
            + ","
            + delivery_status
            + ","
            + inspection_status
            + ","
            + str(available_budget)
            + ","
            + str(payment_amount)
    )

    if delivery_status == "未到货" and inspection_status == "待检":
        prepayment_review_record_list.append(purchase_order_id)

    elif delivery_status == "已到货" and inspection_status == "不合格":
        quality_rejection_record_list.append(purchase_order_id)

    elif delivery_status == "已到货" and inspection_status == "待检":
        pending_inspection_record_list.append(purchase_order_id)

    elif (
            delivery_status == "已到货"
            and inspection_status == "合格"
            and payment_amount > available_budget
    ):
        insufficient_budget_record_list.append(purchase_order_id)

    else:
        payment_release_record_list.append(purchase_order_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)

prepayment_review_count = len(prepayment_review_record_list)
quality_rejection_count = len(quality_rejection_record_list)
pending_inspection_count = len(pending_inspection_record_list)
insufficient_budget_count = len(insufficient_budget_record_list)
payment_release_count = len(payment_release_record_list)

if invalid_record_count > 0:
    business_conclusion = "数据需要人工更正，付款统计不完整"

elif quality_rejection_count > 0:
    business_conclusion = "存在质量不合格材料，相关付款不予放行"

elif pending_inspection_count > 0 or prepayment_review_count > 0:
    business_conclusion = "存在尚未完成正常验收的采购单，需要人工处理"

elif insufficient_budget_count > 0:
    business_conclusion = "存在预算不足的付款申请，需要补充预算"

else:
    business_conclusion = "全部采购材料付款申请可以放行"

# 8. 控制台输出
print("采购材料付款放行判断报告")
print("=" * 30)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)

print()
print("预付款复核数量:", prepayment_review_count)
print("质量不合格数量:", quality_rejection_count)
print("待验收数量:", pending_inspection_count)
print("预算不足数量:", insufficient_budget_count)
print("可付款数量:", payment_release_count)

print()
print("预付款复核采购单:", prepayment_review_record_list)
print("质量不合格采购单:", quality_rejection_record_list)
print("待验收采购单:", pending_inspection_record_list)
print("预算不足采购单:", insufficient_budget_record_list)
print("可付款采购单:", payment_release_record_list)

print()
print("无效记录:")
for invalid_record in invalid_record_list:
    print(invalid_record)

print()
print("无效原因:")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()
print("业务结论:", business_conclusion)


# 9. 写入清洗后的 CSV 文件
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("采购单号,到货状态,验收状态,可用预算,付款申请金额\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 10. 写入 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("采购材料付款放行判断报告\n")
    f.write("=" * 30 + "\n")

    f.write("原始记录数量: " + str(raw_record_count) + "\n")
    f.write("有效记录数量: " + str(valid_record_count) + "\n")
    f.write("无效记录数量: " + str(invalid_record_count) + "\n")

    f.write("\n")
    f.write("预付款复核数量: " + str(prepayment_review_count) + "\n")
    f.write("质量不合格数量: " + str(quality_rejection_count) + "\n")
    f.write("待验收数量: " + str(pending_inspection_count) + "\n")
    f.write("预算不足数量: " + str(insufficient_budget_count) + "\n")
    f.write("可付款数量: " + str(payment_release_count) + "\n")

    f.write("\n")
    f.write("预付款复核采购单: " + str(prepayment_review_record_list) + "\n")
    f.write("质量不合格采购单: " + str(quality_rejection_record_list) + "\n")
    f.write("待验收采购单: " + str(pending_inspection_record_list) + "\n")
    f.write("预算不足采购单: " + str(insufficient_budget_record_list) + "\n")
    f.write("可付款采购单: " + str(payment_release_record_list) + "\n")

    f.write("\n")
    f.write("无效记录:\n")

    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n")
    f.write("无效原因:\n")

    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n")
    f.write("业务结论: " + business_conclusion + "\n")