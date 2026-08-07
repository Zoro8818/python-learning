# 业务目标：检查售后工单优先级，隔离无效记录并识别需要优先处理的工单。
# 输入字段：工单编号、客户名称、预计损失金额、问题等级、处理状态。
# 处理链：读取 CSV -> 字段校验 -> 有效保存 -> 等级与状态组合分类 -> 金额统计。
# 分类口径：高等级未处理为紧急；中或低等级未处理为待处理；
#           处理中和已完成工单分别进入对应分类。
# 输出结果：有效工单 cleaned CSV、分类数量、最高最低损失和 TXT 报告。

input_file_path = (
    r"D:\python-project\课后作业\input\after_sales_tickets.csv"
)

cleaned_file_path = (
    r"D:\python-project\课后作业\output\after_sales_tickets_cleaned.csv"
)

report_file_path = (
    r"D:\python-project\课后作业\output\after_sales_tickets_report.txt"
)

raw_record_list = []

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "工单编号,客户名称,预计损失金额,问题等级,处理状态"
    ):
        raw_record_list.append(clean_line)

# 五个有效字段列表
ticket_number_list = []              # 工单编号列表
customer_name_list = []              # 客户名称列表
estimated_loss_amount_list = []      # 预计损失金额列表
issue_level_list = []                # 问题等级列表
handling_status_list = []            # 处理状态列表

# 清洗后的有效记录
cleaned_record_list = []

# 无效记录
invalid_record_list = []
invalid_reason_list = []

# 四种业务分类
urgent_ticket_list = []              # 紧急处理工单
pending_ticket_list = []             # 待处理工单
processing_ticket_list = []          # 处理中工单
completed_ticket_list = []           # 已完成工单

# 预计损失金额合计
total_estimated_loss_amount = 0

# 最高损失金额及对应工单
highest_loss_amount = 0
highest_loss_ticket = ""

# 最低损失金额及对应工单
lowest_loss_amount = 0
lowest_loss_ticket = ""

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误,原始记录: " + raw_record)
        continue

    ticket_number = parts[0].strip()
    customer_name = parts[1].strip()
    estimated_loss_amount_text = parts[2].strip()
    issue_level = parts[3].strip()
    handling_status = parts[4].strip()

    if (
        ticket_number == ""
        or customer_name == ""
        or estimated_loss_amount_text == ""
        or issue_level == ""
        or handling_status == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空,原始记录: " + raw_record)
        continue

    if not estimated_loss_amount_text.replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("预计损失金额不是数字: " + raw_record)
        continue

    if (
        issue_level != "高"
        and issue_level != "中"
        and issue_level != "低"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("问题等级不合法: " + raw_record)
        continue

    if (
        handling_status != "未处理"
        and handling_status != "处理中"
        and handling_status != "已完成"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("处理状态不合法: " + raw_record)
        continue

    estimated_loss_amount = float(estimated_loss_amount_text)

    ticket_number_list.append(ticket_number)
    customer_name_list.append(customer_name)
    estimated_loss_amount_list.append(estimated_loss_amount)
    issue_level_list.append(issue_level)
    handling_status_list.append(handling_status)

    cleaned_record_list.append(
        ticket_number
        + ","
        + customer_name
        + ","
        + str(estimated_loss_amount)
        + ","
        + issue_level
        + ","
        + handling_status
    )

    total_estimated_loss_amount += estimated_loss_amount

    if len(estimated_loss_amount_list) == 1:
        highest_loss_amount = estimated_loss_amount
        highest_loss_ticket = ticket_number

        lowest_loss_amount = estimated_loss_amount
        lowest_loss_ticket = ticket_number

    else:
        if estimated_loss_amount > highest_loss_amount:
            highest_loss_amount = estimated_loss_amount
            highest_loss_ticket = ticket_number

        if estimated_loss_amount < lowest_loss_amount:
            lowest_loss_amount = estimated_loss_amount
            lowest_loss_ticket = ticket_number

    if issue_level == "高" and handling_status == "未处理":
        urgent_ticket_list.append(ticket_number)

    elif (
        (issue_level == "中" or issue_level == "低")
        and handling_status == "未处理"
    ):
        pending_ticket_list.append(ticket_number)

    elif handling_status == "处理中":
        processing_ticket_list.append(ticket_number)

    elif handling_status == "已完成":
        completed_ticket_list.append(ticket_number)

raw_record_count = len(raw_record_list)
cleaned_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)
urgent_ticket_count = len(urgent_ticket_list)
pending_ticket_count = len(pending_ticket_list)
processing_ticket_count = len(processing_ticket_list)
completed_ticket_count = len(completed_ticket_list)

print("原始记录数量：", raw_record_count)
print("有效记录数量：", cleaned_record_count)
print("无效记录数量：", invalid_record_count)

print()
print("紧急处理工单：", urgent_ticket_list)
print("待处理工单：", pending_ticket_list)
print("处理中工单：", processing_ticket_list)
print("已完成工单：", completed_ticket_list)

print()
print("紧急处理数量：", urgent_ticket_count)
print("待处理数量：", pending_ticket_count)
print("处理中数量：", processing_ticket_count)
print("已完成数量：", completed_ticket_count)

print()
print("预计损失金额合计：", total_estimated_loss_amount)
print("最高损失工单：", highest_loss_ticket)
print("最高损失金额：", highest_loss_amount)
print("最低损失工单：", lowest_loss_ticket)
print("最低损失金额：", lowest_loss_amount)

print()
print("无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print()
print("无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("工单编号,客户名称,预计损失金额,问题等级,处理状态\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")

if urgent_ticket_count > 0:
    business_conclusion = "存在高等级未处理工单，需要优先处理"

elif invalid_record_count > 0:
    business_conclusion = "存在无效数据，需要修正后重新检查"

elif pending_ticket_count > 0 or processing_ticket_count > 0:
    business_conclusion = "当前仍有工单尚未完成，需要继续跟进"

else:
    business_conclusion = "所有有效工单均已完成"

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("售后工单优先级检查报告\n")
    file.write("========================\n")

    file.write("原始记录数量：" + str(raw_record_count) + "\n")
    file.write("有效记录数量：" + str(cleaned_record_count) + "\n")
    file.write("无效记录数量：" + str(invalid_record_count) + "\n")

    file.write("\n")
    file.write("紧急处理工单：" + str(urgent_ticket_list) + "\n")
    file.write("待处理工单：" + str(pending_ticket_list) + "\n")
    file.write("处理中工单：" + str(processing_ticket_list) + "\n")
    file.write("已完成工单：" + str(completed_ticket_list) + "\n")

    file.write("\n")
    file.write("紧急处理数量：" + str(urgent_ticket_count) + "\n")
    file.write("待处理数量：" + str(pending_ticket_count) + "\n")
    file.write("处理中数量：" + str(processing_ticket_count) + "\n")
    file.write("已完成数量：" + str(completed_ticket_count) + "\n")

    file.write("\n")
    file.write(
        "预计损失金额合计："
        + str(total_estimated_loss_amount)
        + "\n"
    )

    if cleaned_record_count > 0:
        file.write("最高损失工单：" + highest_loss_ticket + "\n")
        file.write("最高损失金额：" + str(highest_loss_amount) + "\n")
        file.write("最低损失工单：" + lowest_loss_ticket + "\n")
        file.write("最低损失金额：" + str(lowest_loss_amount) + "\n")
    else:
        file.write("最高损失工单：无有效数据\n")
        file.write("最高损失金额：无有效数据\n")
        file.write("最低损失工单：无有效数据\n")
        file.write("最低损失金额：无有效数据\n")

    file.write("\n")
    file.write("无效数据明细：\n")

    if invalid_record_count > 0:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")
    else:
        file.write("无\n")

    file.write("\n")
    file.write("业务结论：" + business_conclusion + "\n")
