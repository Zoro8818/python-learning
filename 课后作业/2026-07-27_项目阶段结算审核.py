input_file = "D:/python-project/课后作业/input/project_stage_settlement_review.csv"
cleaned_file = "D:/python-project/课后作业/output/project_stage_settlement_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/project_stage_settlement_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "结算单号,交付状态,验收状态,合同金额,已结算金额,本次结算金额":
        raw_record_list.append(clean_line)

# 有效、无效结果
valid_record_list = []          # 有效记录列表
invalid_record_list = []        # 无效记录列表
invalid_reason_list = []        # 无效原因列表

# 有效记录分类
over_contract_review_list = []  # 超合同结算复核列表
waiting_delivery_list = []      # 等待交付列表
acceptance_correction_list = [] # 验收整改列表
waiting_acceptance_list = []    # 等待验收列表
ready_for_settlement_list = []  # 可结算列表

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 6:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    settlement_id = parts[0].strip()
    delivery_status = parts[1].strip()
    acceptance_status = parts[2].strip()
    contract_amount_text = parts[3].strip()
    settled_amount_text = parts[4].strip()
    current_settlement_amount_text = parts[5].strip()

    if (
        settlement_id == ""
        or delivery_status == ""
        or acceptance_status == ""
        or contract_amount_text == ""
        or settled_amount_text == ""
        or current_settlement_amount_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if delivery_status != "已交付" and delivery_status != "未交付":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("交付状态不合法, 原始记录: " + raw_record)
        continue

    if (
        acceptance_status != "通过"
        and acceptance_status != "待验收"
        and acceptance_status != "不通过"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("验收状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not contract_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
        or not settled_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
        or not current_settlement_amount_text.removeprefix("-").replace(".", "", 1).isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("合同金额或已结算金额或本次结算金额不是合法数字, 原始记录: " + raw_record)
        continue

    contract_amount = float(contract_amount_text)
    settled_amount = float(settled_amount_text)
    current_settlement_amount = float(current_settlement_amount_text)

    if contract_amount <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("合同金额必须大于 0, 原始记录: " + raw_record)
        continue

    if settled_amount < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已结算金额必须大于等于 0, 原始记录: " + raw_record)
        continue

    if current_settlement_amount <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("本次结算金额必须大于 0, 原始记录: " + raw_record)
        continue

    # 状态组合合理性检查
    if (
        delivery_status == "未交付"
        and acceptance_status != "待验收"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "未交付时验收状态只能是待验收, 原始记录: " + raw_record
        )
        continue

    # 保存清洗后的有效记录
    clean_record = (
        settlement_id + ","
        + delivery_status + ","
        + acceptance_status + ","
        + str(contract_amount) + ","
        + str(settled_amount) + ","
        + str(current_settlement_amount)
    )

    valid_record_list.append(clean_record)

    # 计算结算金额合计
    total_settlement_amount = (
        settled_amount + current_settlement_amount
    )

    if total_settlement_amount > contract_amount:
        over_contract_review_list.append(settlement_id)

    elif (
        delivery_status == "未交付"
        and acceptance_status == "待验收"
    ):
        waiting_delivery_list.append(settlement_id)

    elif (
        delivery_status == "已交付"
        and acceptance_status == "不通过"
    ):
        acceptance_correction_list.append(settlement_id)

    elif (
        delivery_status == "已交付"
        and acceptance_status == "待验收"
    ):
        waiting_acceptance_list.append(settlement_id)

    else:
        ready_for_settlement_list.append(settlement_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

over_contract_review_count = len(over_contract_review_list)
waiting_delivery_count = len(waiting_delivery_list)
acceptance_correction_count = len(acceptance_correction_list)
waiting_acceptance_count = len(waiting_acceptance_list)
ready_for_settlement_count = len(ready_for_settlement_list)

final_conclusion = ""
if invalid_record_count > 0:
    final_conclusion = "无效数据"
elif over_contract_review_count > 0:
    final_conclusion = "超合同结算复核"
elif acceptance_correction_count > 0:
    final_conclusion = "验收整改"
elif waiting_delivery_count > 0:
    final_conclusion = "等待交付"
elif waiting_acceptance_count > 0:
    final_conclusion = "等待验收"
else:
    final_conclusion = "可结算"

print("项目阶段结算审核报告")
print("============================")
print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("超合同结算复核数量:", over_contract_review_count)
print("验收整改数量:", acceptance_correction_count)
print("等待交付数量:", waiting_delivery_count)
print("等待验收数量:", waiting_acceptance_count)
print("可结算数量:", ready_for_settlement_count)
print()

print("超合同结算复核单:", over_contract_review_list)
print("验收整改结算单:", acceptance_correction_list)
print("等待交付结算单:", waiting_delivery_list)
print("等待验收结算单:", waiting_acceptance_list)
print("可结算结算单:", ready_for_settlement_list)
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

# 写入清洗后的有效 CSV 文件
with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write(
        "结算单号,交付状态,验收状态,合同金额,已结算金额,本次结算金额\n"
    )

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# 写入 TXT 审核报告
with open(report_file, "w", encoding="utf-8") as file:
    file.write("项目阶段结算审核报告\n")
    file.write("============================\n")
    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")
    file.write("\n")

    file.write(
        "超合同结算复核数量: "
        + str(over_contract_review_count)
        + "\n"
    )
    file.write(
        "验收整改数量: "
        + str(acceptance_correction_count)
        + "\n"
    )
    file.write(
        "等待交付数量: "
        + str(waiting_delivery_count)
        + "\n"
    )
    file.write(
        "等待验收数量: "
        + str(waiting_acceptance_count)
        + "\n"
    )
    file.write(
        "可结算数量: "
        + str(ready_for_settlement_count)
        + "\n"
    )
    file.write("\n")

    file.write(
        "超合同结算复核单: "
        + str(over_contract_review_list)
        + "\n"
    )
    file.write(
        "验收整改结算单: "
        + str(acceptance_correction_list)
        + "\n"
    )
    file.write(
        "等待交付结算单: "
        + str(waiting_delivery_list)
        + "\n"
    )
    file.write(
        "等待验收结算单: "
        + str(waiting_acceptance_list)
        + "\n"
    )
    file.write(
        "可结算结算单: "
        + str(ready_for_settlement_list)
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
    file.write("最终结论: " + final_conclusion + "\n")