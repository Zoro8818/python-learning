# 1. 文件路径
input_file = "D:/python-project/课后作业/input/customer_credit_release.csv"

cleaned_file = "D:/python-project/课后作业/output/customer_credit_release_cleaned.csv"

report_file = "D:/python-project/课后作业/output/customer_credit_release_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 3. 按行拆分
lines = csv_text.splitlines()


# 4. 去除表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "客户编号,账户状态,授信状态,可用额度,本次订单金额"
    ):
        raw_record_list.append(clean_line)


# 5. 五个有效字段列表
valid_customer_id_list = []
valid_account_status_list = []
valid_credit_status_list = []
valid_available_credit_list = []
valid_order_amount_list = []


# 6. 有效和无效记录
cleaned_record_list = []

invalid_record_list = []
invalid_reason_list = []


# 7. 五个业务分类列表
suspended_account_order_list = []
overlimit_risk_order_list = []
frozen_credit_order_list = []
insufficient_credit_order_list = []
releasable_order_list = []


# 8. 最终业务结论
business_conclusion = ""


# 9. 开始逐条处理
for raw_record in raw_record_list:
    parts = raw_record.split(",")

    # 从这里开始写核心处理逻辑
    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    customer_id = parts[0].strip()
    account_status = parts[1].strip()
    credit_status = parts[2].strip()
    available_credit_text = parts[3].strip()
    order_amount_text = parts[4].strip()

    if (
        customer_id == ""
        or account_status == ""
        or credit_status == ""
        or available_credit_text == ""
        or order_amount_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if account_status != "正常" and account_status != "暂停":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("账户状态不合法, 原始记录: " + raw_record)
        continue

    if (
        credit_status != "正常"
        and credit_status != "超额"
        and credit_status != "冻结"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("授信状态不合法, 原始记录: " + raw_record)
        continue

    if not available_credit_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("可用额度不是数字, 原始记录: " + raw_record)
        continue

    if not order_amount_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("本次订单金额不是数字, 原始记录: " + raw_record)
        continue

    available_credit = float(available_credit_text)
    order_amount = float(order_amount_text)

    if order_amount <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("本次订单金额必须大于0, 原始记录: " + raw_record)
        continue

    if credit_status == "正常" and available_credit <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段组合矛盾, 原始记录: " + raw_record)
        continue

    if credit_status == "超额" and available_credit >= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段组合矛盾, 原始记录: " + raw_record)
        continue

    if credit_status == "冻结" and available_credit != 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段组合矛盾, 原始记录: " + raw_record)
        continue

    valid_customer_id_list.append(customer_id)
    valid_account_status_list.append(account_status)
    valid_credit_status_list.append(credit_status)
    valid_available_credit_list.append(available_credit)
    valid_order_amount_list.append(order_amount)

    cleaned_record_list.append(
        customer_id
        + ","
        + account_status
        + ","
        + credit_status
        + ","
        + str(available_credit)
        + ","
        + str(order_amount)
    )

    if account_status == "暂停":
        suspended_account_order_list.append(customer_id)
    elif account_status == "正常" and credit_status == "超额":
        overlimit_risk_order_list.append(customer_id)
    elif account_status == "正常" and credit_status == "冻结":
        frozen_credit_order_list.append(customer_id)
    elif (
        account_status == "正常"
        and credit_status == "正常"
        and order_amount > available_credit
    ):
        insufficient_credit_order_list.append(customer_id)
    else:
        releasable_order_list.append(customer_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)

suspended_account_order_count = len(suspended_account_order_list)
overlimit_risk_order_count = len(overlimit_risk_order_list)
frozen_credit_order_count = len(frozen_credit_order_list)
insufficient_credit_order_count = len(insufficient_credit_order_list)
releasable_order_count = len(releasable_order_list)

if invalid_record_count > 0:
    business_conclusion = "数据需要人工更正，统计结论不完整"
elif suspended_account_order_count > 0:
    business_conclusion = "存在暂停账户订单，暂不放行"
elif overlimit_risk_order_count > 0:
    business_conclusion = "存在超额客户，需要人工审核"
elif frozen_credit_order_count > 0:
    business_conclusion = "存在冻结授信订单，暂不放行"
elif insufficient_credit_order_count > 0:
    business_conclusion = "存在额度不足订单，需要补充授信"
else:
    business_conclusion = "全部订单可按授信额度放行"

print("客户授信放行风险检查报告")
print("============================")
print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("账户暂停订单数量:", suspended_account_order_count)
print("超额风险订单数量:", overlimit_risk_order_count)
print("授信冻结订单数量:", frozen_credit_order_count)
print("额度不足订单数量:", insufficient_credit_order_count)
print("可放行订单数量:", releasable_order_count)
print()

print("账户暂停订单:", suspended_account_order_list)
print("超额风险订单:", overlimit_risk_order_list)
print("授信冻结订单:", frozen_credit_order_list)
print("额度不足订单:", insufficient_credit_order_list)
print("可放行订单:", releasable_order_list)
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

with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("客户编号,账户状态,授信状态,可用额度,本次订单金额\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")

with open(report_file, "w", encoding="utf-8") as f:
    f.write("客户授信放行风险检查报告\n")
    f.write("============================\n")
    f.write("原始记录数量: " + str(raw_record_count) + "\n")
    f.write("有效记录数量: " + str(valid_record_count) + "\n")
    f.write("无效记录数量: " + str(invalid_record_count) + "\n\n")

    f.write(
        "账户暂停订单数量: "
        + str(suspended_account_order_count)
        + "\n"
    )
    f.write(
        "超额风险订单数量: "
        + str(overlimit_risk_order_count)
        + "\n"
    )
    f.write(
        "授信冻结订单数量: "
        + str(frozen_credit_order_count)
        + "\n"
    )
    f.write(
        "额度不足订单数量: "
        + str(insufficient_credit_order_count)
        + "\n"
    )
    f.write(
        "可放行订单数量: "
        + str(releasable_order_count)
        + "\n\n"
    )

    f.write(
        "账户暂停订单: "
        + str(suspended_account_order_list)
        + "\n"
    )
    f.write(
        "超额风险订单: "
        + str(overlimit_risk_order_list)
        + "\n"
    )
    f.write(
        "授信冻结订单: "
        + str(frozen_credit_order_list)
        + "\n"
    )
    f.write(
        "额度不足订单: "
        + str(insufficient_credit_order_list)
        + "\n"
    )
    f.write(
        "可放行订单: "
        + str(releasable_order_list)
        + "\n\n"
    )

    f.write("无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n业务结论: " + business_conclusion + "\n")