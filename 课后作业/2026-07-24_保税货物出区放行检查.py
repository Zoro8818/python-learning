# 1. 文件路径
input_file = "D:/python-project/课后作业/input/bonded_goods_release.csv"

cleaned_file = "D:/python-project/课后作业/output/bonded_goods_release_cleaned.csv"

report_file = "D:/python-project/课后作业/output/bonded_goods_release_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

line_list = csv_text.splitlines()


# 3. 去掉表头和空行
raw_record_list = []

for line in line_list:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line
        != "货物编号,申报状态,海关状态,货检状态,申报数量,实收数量"
    ):
        raw_record_list.append(clean_line)


# 4. 有效字段列表
goods_id_list = []              #货物编号列表
declaration_status_list = []    #申报状态列表
customs_status_list = []        #海关状态列表
inspection_status_list = []     #货检状态列表
declared_quantity_list = []     #申报数量列表
received_quantity_list = []     #实收数量列表


# 5. 有效记录和无效记录
cleaned_record_list = []

invalid_record_list = []
invalid_reason_list = []


# 6. 七个业务分类列表
supplement_declaration_list = []        #补申报货物列表

customs_detention_list = []             #海关扣留货物列表

pending_customs_inspection_list = []    #待海关查验货物列表

quality_review_list = []                #质量复核货物列表

goods_inspection_review_list = []       #货检复核货物列表

quantity_review_list = []               #数量复核货物列表

release_allowed_list = []               #可出区货物列表

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 6:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    goods_id = parts[0].strip()
    declaration_status = parts[1].strip()
    customs_status = parts[2].strip()
    inspection_status = parts[3].strip()
    declared_quantity_text = parts[4].strip()
    received_quantity_text = parts[5].strip()

    if (
        goods_id == ""
        or declaration_status == ""
        or customs_status == ""
        or inspection_status == ""
        or declared_quantity_text == ""
        or received_quantity_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        declaration_status != "已申报"
        and declaration_status != "未申报"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("申报状态不合法, 原始记录: " + raw_record)
        continue

    if (
        customs_status != "放行"
        and customs_status != "查验"
        and customs_status != "扣留"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("海关状态不合法, 原始记录: " + raw_record)
        continue

    if (
        inspection_status != "合格"
        and inspection_status != "待检"
        and inspection_status != "不合格"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("货检状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not declared_quantity_text.removeprefix("-").replace(".", "", 1).isdigit()
        or not received_quantity_text.removeprefix("-").replace(".", "", 1).isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("申报数量或实收数量不是合法数字, 原始记录: " + raw_record)
        continue

    declared_quantity = float(declared_quantity_text)
    received_quantity = float(received_quantity_text)

    if declared_quantity <= 0 or received_quantity <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("申报数量和实收数量必须大于 0, 原始记录: " + raw_record)
        continue

    if (
        declaration_status == "未申报"
        and (
        customs_status != "扣留"
        or inspection_status != "待检"
        )
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    if (
        declaration_status == "已申报"
        and customs_status == "查验"
        and inspection_status != "待检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    goods_id_list.append(goods_id)
    declaration_status_list.append(declaration_status)
    customs_status_list.append(customs_status)
    inspection_status_list.append(inspection_status)
    declared_quantity_list.append(declared_quantity)
    received_quantity_list.append(received_quantity)

    cleaned_record_list.append(
        goods_id
        + ","
        + declaration_status
        + ","
        + customs_status
        + ","
        + inspection_status
        + ","
        + str(declared_quantity)
        + ","
        + str(received_quantity)
    )

    if declaration_status == "未申报":
        supplement_declaration_list.append(goods_id)
    elif declaration_status == "已申报" and customs_status == "扣留":
        customs_detention_list.append(goods_id)
    elif declaration_status == "已申报" and customs_status == "查验":
        pending_customs_inspection_list.append(goods_id)
    elif declaration_status == "已申报" and customs_status == "放行" and inspection_status == "不合格":
        quality_review_list.append(goods_id)
    elif declaration_status == "已申报" and customs_status == "放行" and inspection_status == "待检":
        goods_inspection_review_list.append(goods_id)
    elif declaration_status == "已申报" and customs_status == "放行" and inspection_status == "合格" and received_quantity > declared_quantity:
        quantity_review_list.append(goods_id)
    else:
        release_allowed_list.append(goods_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)


supplement_declaration_count = len(supplement_declaration_list)
customs_detention_count = len(customs_detention_list)
pending_customs_inspection_count = len(pending_customs_inspection_list)
quality_review_count = len(quality_review_list)
goods_inspection_review_count = len(goods_inspection_review_list)
quantity_review_count = len(quantity_review_list)
release_allowed_count = len(release_allowed_list)

final_conclusion = ""

if invalid_record_count > 0:
    final_conclusion = "存在无效数据，货物出区统计不完整"
elif supplement_declaration_count > 0:
    final_conclusion = "存在未申报货物，需要先完成补申报"
elif customs_detention_count > 0:
    final_conclusion = "存在海关扣留货物，暂不允许出区"
elif quality_review_count > 0:
    final_conclusion = "存在质量不合格货物，需要进行质量复核"
elif pending_customs_inspection_count > 0:
    final_conclusion = "存在待海关查验货物，需要等待查验"
elif goods_inspection_review_count > 0:
    final_conclusion = "存在待检货物，需要进行货检复核"
elif quantity_review_count > 0:
    final_conclusion = "存在实收数量超过申报数量的货物，需要进行数量复核"
else:
    final_conclusion = "全部保税货物可以出区"

# 统计报告文本
report_text = (
    "保税货物出区放行检查报告\n"
    + "============================\n"
    + "原始记录数量: " + str(raw_record_count) + "\n"
    + "有效记录数量: " + str(valid_record_count) + "\n"
    + "无效记录数量: " + str(invalid_record_count) + "\n\n"

    + "补申报数量: " + str(supplement_declaration_count) + "\n"
    + "海关扣留数量: " + str(customs_detention_count) + "\n"
    + "待海关查验数量: " + str(pending_customs_inspection_count) + "\n"
    + "质量复核数量: " + str(quality_review_count) + "\n"
    + "货检复核数量: " + str(goods_inspection_review_count) + "\n"
    + "数量复核数量: " + str(quantity_review_count) + "\n"
    + "可出区数量: " + str(release_allowed_count) + "\n\n"

    + "补申报货物: " + str(supplement_declaration_list) + "\n"
    + "海关扣留货物: " + str(customs_detention_list) + "\n"
    + "待海关查验货物: " + str(pending_customs_inspection_list) + "\n"
    + "质量复核货物: " + str(quality_review_list) + "\n"
    + "货检复核货物: " + str(goods_inspection_review_list) + "\n"
    + "数量复核货物: " + str(quantity_review_list) + "\n"
    + "可出区货物: " + str(release_allowed_list) + "\n\n"

    + "无效记录:\n"
)

for invalid_record in invalid_record_list:
    report_text += invalid_record + "\n"

report_text += "\n无效原因:\n"

for invalid_reason in invalid_reason_list:
    report_text += invalid_reason + "\n"

report_text += "\n最终结论:\n" + final_conclusion


# 控制台输出
print(report_text)


# 输出 cleaned CSV
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("货物编号,申报状态,海关状态,货检状态,申报数量,实收数量\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 输出 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write(report_text)