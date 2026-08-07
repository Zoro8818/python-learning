# 1. 输入文件路径
input_file = "D:/python-project/课后作业/input/cold_chain_medicine_arrivals.csv"
cleaned_file = "D:/python-project/课后作业/output/cold_chain_medicine_arrivals_cleaned.csv"
report_file = "D:/python-project/课后作业/output/cold_chain_medicine_arrivals_report.txt"

# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

# 3. 按行拆分
lines = csv_text.splitlines()

# 4. 保存去掉表头和空行后的原始记录
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "批次号,签收状态,运输温度,封签状态,应收数量,实收数量"
    ):
        raw_record_list.append(clean_line)

valid_record_list = []       # 所有检查通过的有效记录
invalid_record_list = []     # 无效原始记录
invalid_reason_list = []     # 每条无效记录对应的具体原因

rejected_record_list = []    # 拒收批次
approved_record_list = []    # 可入库批次
inspection_record_list = []  # 待复检批次

rejected_count = 0
approved_count = 0
inspection_count = 0
total_expected_qty = 0
total_received_qty = 0

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 6:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue


    # 六个字段分别清洗
    batch_number = parts[0].strip()
    receipt_status = parts[1].strip()
    transport_temperature_text = parts[2].strip()
    seal_status = parts[3].strip()
    expected_qty_text = parts[4].strip()
    received_qty_text = parts[5].strip()

    if (
        batch_number == ""
        or receipt_status == ""
        or transport_temperature_text == ""
        or seal_status == ""
        or expected_qty_text == ""
        or received_qty_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空,原始记录: " + raw_record)
        continue

    if receipt_status != "已签收" and receipt_status != "拒收":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("签收状态不合法: " + raw_record)
        continue

    if seal_status != "完好" and seal_status != "破损":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("封签状态不合法: " + raw_record)
        continue

    if not transport_temperature_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("运输温度不是数字: " + raw_record)
        continue

    if not expected_qty_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("应收数量不是数字: " + raw_record)
        continue

    if not received_qty_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实收数量不是数字: " + raw_record)
        continue

    transport_temperature = float(transport_temperature_text)
    expected_qty = float(expected_qty_text)
    received_qty = float(received_qty_text)

    if expected_qty <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("应收数量必须大于 0, 原始记录: " + raw_record)
        continue

    if received_qty < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实收数量不能小于 0, 原始记录: " + raw_record)
        continue

    if receipt_status == "拒收" and received_qty != 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("拒收记录的实收数量必须为 0, 原始记录: " + raw_record)
        continue

    if receipt_status == "已签收" and received_qty <= 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("已签收记录的实收数量必须大于 0, 原始记录: " + raw_record)
        continue

    valid_record_list.append(raw_record)

    total_expected_qty += expected_qty
    total_received_qty += received_qty

    if receipt_status == "拒收":
        rejected_record_list.append(raw_record)
        rejected_count += 1

    elif (
            2 <= transport_temperature <= 8
            and seal_status == "完好"
            and received_qty == expected_qty
    ):
        approved_record_list.append(raw_record)
        approved_count += 1

    else:
        inspection_record_list.append(raw_record)
        inspection_count += 1

if len(invalid_record_list) > 0:
    final_conclusion = "数据需要人工更正，统计结论不完整"

elif rejected_count > 0:
    final_conclusion = "存在拒收批次，不得入库"

elif inspection_count > 0:
    final_conclusion = "存在待复检批次，复检后再决定是否入库"

else:
    final_conclusion = "全部批次可入库"

print("冷链药品到货放行判断报告")
print("============================")

print("原始记录数量:", len(raw_record_list))
print("有效记录数量:", len(valid_record_list))
print("无效记录数量:", len(invalid_record_list))

print()
print("拒收批次数量:", rejected_count)
print("可入库批次数量:", approved_count)
print("待复检批次数量:", inspection_count)

print()
print("有效应收数量合计:", total_expected_qty)
print("有效实收数量合计:", total_received_qty)

print()
print("拒收批次:")
if len(rejected_record_list) == 0:
    print("无")
else:
    for record in rejected_record_list:
        print(record)

print()
print("可入库批次:")
if len(approved_record_list) == 0:
    print("无")
else:
    for record in approved_record_list:
        print(record)

print()
print("待复检批次:")
if len(inspection_record_list) == 0:
    print("无")
else:
    for record in inspection_record_list:
        print(record)

print()
print("无效记录及原因:")
if len(invalid_reason_list) == 0:
    print("无")
else:
    for reason in invalid_reason_list:
        print(reason)

print()
print("最终结论:", final_conclusion)

with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("批次号,签收状态,运输温度,封签状态,应收数量,实收数量\n")

    for record in valid_record_list:
        f.write(record + "\n")

with open(report_file, "w", encoding="utf-8") as f:
    f.write("冷链药品到货放行判断报告\n")
    f.write("============================\n")

    f.write("原始记录数量:" + str(len(raw_record_list)) + "\n")
    f.write("有效记录数量:" + str(len(valid_record_list)) + "\n")
    f.write("无效记录数量:" + str(len(invalid_record_list)) + "\n")

    f.write("\n")
    f.write("拒收批次数量:" + str(rejected_count) + "\n")
    f.write("可入库批次数量:" + str(approved_count) + "\n")
    f.write("待复检批次数量:" + str(inspection_count) + "\n")

    f.write("\n")
    f.write("有效应收数量合计:" + str(total_expected_qty) + "\n")
    f.write("有效实收数量合计:" + str(total_received_qty) + "\n")

    f.write("\n拒收批次:\n")
    if len(rejected_record_list) == 0:
        f.write("无\n")
    else:
        for record in rejected_record_list:
            f.write(record + "\n")

    f.write("\n可入库批次:\n")
    if len(approved_record_list) == 0:
        f.write("无\n")
    else:
        for record in approved_record_list:
            f.write(record + "\n")

    f.write("\n待复检批次:\n")
    if len(inspection_record_list) == 0:
        f.write("无\n")
    else:
        for record in inspection_record_list:
            f.write(record + "\n")

    f.write("\n无效记录及原因:\n")
    if len(invalid_reason_list) == 0:
        f.write("无\n")
    else:
        for reason in invalid_reason_list:
            f.write(reason + "\n")

    f.write("\n最终结论:" + final_conclusion + "\n")