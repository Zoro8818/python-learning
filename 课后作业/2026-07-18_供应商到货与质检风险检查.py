# 业务目标：检查供应商到货与质检状态，识别待催货、待质检和质量风险。
# 输入字段：采购单号、供应商名称、采购金额、到货状态、质检结果。
# 处理链：读取 CSV -> 字段校验 -> 状态组合校验 -> 有效保存与分类 -> 统计输出。
# 特殊规则：字段值分别合法不代表组合合理；未到货却已合格或不合格属于无效记录。
# 分类口径：未到货未检为待催货，已到货未检为待质检，
#           已到货不合格为质量风险，已到货合格为正常入库。
# 输出结果：有效采购记录 cleaned CSV、金额统计、最高最低和 TXT 风险报告。

input_file_path = (
    r"D:\python-project\课后作业\input\supplier_delivery_check.csv"
)

cleaned_file_path = (
    r"D:\python-project\课后作业\output\supplier_delivery_cleaned.csv"
)

report_file_path = (
    r"D:\python-project\课后作业\output\supplier_delivery_report.txt"
)

raw_record_list = []

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "采购单号,供应商名称,采购金额,到货状态,质检结果"
    ):
        raw_record_list.append(clean_line)

# 五个有效字段列表
purchase_order_number_list = []      # 采购单号列表
supplier_name_list = []              # 供应商名称列表
purchase_amount_list = []            # 采购金额列表
arrival_status_list = []              # 到货状态列表
inspection_result_list = []           # 质检结果列表

# 清洗后的有效记录
cleaned_record_list = []

# 无效记录和无效原因
invalid_record_list = []
invalid_reason_list = []

# 四种业务分类
delivery_reminder_list = []           # 待催货采购单
pending_inspection_list = []          # 待质检采购单
quality_risk_list = []                # 质量风险采购单
normal_storage_list = []              # 正常入库采购单

# 采购金额合计
total_purchase_amount = 0

# 最高采购金额及对应采购单
highest_purchase_amount = 0
highest_purchase_order = ""

# 最低采购金额及对应采购单
lowest_purchase_amount = 0
lowest_purchase_order = ""

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录: " + record)
        continue

    purchase_order_number = parts[0].strip()
    supplier_name = parts[1].strip()
    purchase_amount_text = parts[2].strip()
    arrival_status = parts[3].strip()
    inspection_result = parts[4].strip()

    if (
        purchase_order_number == ""
        or supplier_name == ""
        or purchase_amount_text == ""
        or arrival_status == ""
        or inspection_result == ""
    ):
        invalid_record_list.append(record)
        invalid_reason_list.append("字段为空,原始记录: " + record)
        continue

    if not purchase_amount_text.replace(".", "", 1).isdigit():
        invalid_record_list.append(record)
        invalid_reason_list.append("采购金额不是数字: " + record)
        continue

    if arrival_status != "已到货" and arrival_status != "未到货":
        invalid_record_list.append(record)
        invalid_reason_list.append("到货状态不合法: " + record)
        continue

    if (
        inspection_result != "合格"
        and inspection_result != "不合格"
        and inspection_result != "未检"
        ):
        invalid_record_list.append(record)
        invalid_reason_list.append("判定质检结果不合法: " + record)
        continue

    if (
        arrival_status == "未到货"
        and (
            inspection_result == "合格"
            or inspection_result == "不合格"
        )
    ):
        invalid_record_list.append(record)
        invalid_reason_list.append("状态组合不合理: " + record)
        continue

    purchase_amount = float(purchase_amount_text)

    purchase_order_number_list.append(purchase_order_number)
    supplier_name_list.append(supplier_name)
    purchase_amount_list.append(purchase_amount)
    arrival_status_list.append(arrival_status)
    inspection_result_list.append(inspection_result)

    cleaned_record_list.append(
        purchase_order_number
        + ","
        + supplier_name
        + ","
        + str(purchase_amount)
        + ","
        + arrival_status
        + ","
        + inspection_result
    )

    total_purchase_amount += purchase_amount

    if len(purchase_amount_list) == 1:
        highest_purchase_amount = purchase_amount
        highest_purchase_order = purchase_order_number

        lowest_purchase_amount = purchase_amount
        lowest_purchase_order = purchase_order_number

    else:
        if purchase_amount > highest_purchase_amount:
            highest_purchase_amount = purchase_amount
            highest_purchase_order = purchase_order_number

        if purchase_amount < lowest_purchase_amount:
            lowest_purchase_amount = purchase_amount
            lowest_purchase_order = purchase_order_number

    if arrival_status == "未到货" and inspection_result == "未检":
        delivery_reminder_list.append(purchase_order_number)

    elif arrival_status == "已到货" and inspection_result == "未检":
        pending_inspection_list.append(purchase_order_number)

    elif arrival_status == "已到货" and inspection_result == "不合格":
        quality_risk_list.append(purchase_order_number)

    elif arrival_status == "已到货" and inspection_result == "合格":
        normal_storage_list.append(purchase_order_number)

raw_record_count = len(raw_record_list)
cleaned_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)
delivery_reminder_count = len(delivery_reminder_list)
pending_inspection_count = len(pending_inspection_list)
quality_risk_count = len(quality_risk_list)
normal_storage_count = len(normal_storage_list)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", cleaned_record_count)
print("无效记录数量:", invalid_record_count)

print()
print("待催货采购单:", delivery_reminder_list)
print("待质检采购单:", pending_inspection_list)
print("质量风险采购单:", quality_risk_list)
print("正常入库采购单:", normal_storage_list)

print()
print("待催货数量:", delivery_reminder_count)
print("待质检数量:", pending_inspection_count)
print("质量风险数量:", quality_risk_count)
print("正常入库数量:", normal_storage_count)

print()
print("采购金额合计:", total_purchase_amount)
print("最高采购金额采购单:", highest_purchase_order)
print("最高采购金额:", highest_purchase_amount)
print("最低采购金额采购单:", lowest_purchase_order)
print("最低采购金额:", lowest_purchase_amount)

print()
print("无效原因:")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("采购单号,供应商名称,采购金额,到货状态,质检结果\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")

if quality_risk_count > 0:
    business_conclusion = "存在质检不合格采购单，需要优先处理质量问题"

elif invalid_record_count > 0:
    business_conclusion = "存在无效数据，需要修正后重新检查"

elif delivery_reminder_count > 0 or pending_inspection_count > 0:
    business_conclusion = "当前仍有采购单尚未完成到货或质检，需要继续跟进"

else:
    business_conclusion = "所有有效采购单均已正常入库"

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("供应商到货与质检风险检查报告\n")
    file.write("============================\n")

    file.write("原始记录数量:" + str(raw_record_count) + "\n")
    file.write("有效记录数量:" + str(cleaned_record_count) + "\n")
    file.write("无效记录数量:" + str(invalid_record_count) + "\n")

    file.write("\n")
    file.write("待催货采购单:" + str(delivery_reminder_list) + "\n")
    file.write("待质检采购单:" + str(pending_inspection_list) + "\n")
    file.write("质量风险采购单:" + str(quality_risk_list) + "\n")
    file.write("正常入库采购单:" + str(normal_storage_list) + "\n")

    file.write("\n")
    file.write("待催货数量:" + str(delivery_reminder_count) + "\n")
    file.write("待质检数量:" + str(pending_inspection_count) + "\n")
    file.write("质量风险数量:" + str(quality_risk_count) + "\n")
    file.write("正常入库数量:" + str(normal_storage_count) + "\n")

    file.write("\n")
    file.write("采购金额合计:" + str(total_purchase_amount) + "\n")

    if cleaned_record_count > 0:
        file.write("最高采购金额采购单:" + highest_purchase_order + "\n")
        file.write("最高采购金额:" + str(highest_purchase_amount) + "\n")
        file.write("最低采购金额采购单:" + lowest_purchase_order + "\n")
        file.write("最低采购金额:" + str(lowest_purchase_amount) + "\n")
    else:
        file.write("最高采购金额采购单:无有效数据\n")
        file.write("最高采购金额:无有效数据\n")
        file.write("最低采购金额采购单:无有效数据\n")
        file.write("最低采购金额:无有效数据\n")

    file.write("\n")
    file.write("无效数据明细:\n")

    if invalid_record_count > 0:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")
    else:
        file.write("无\n")

    file.write("\n")
    file.write("业务结论:" + business_conclusion + "\n")
