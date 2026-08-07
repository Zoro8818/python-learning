input_file = "D:/python-project/课后作业/input/construction_hazard_rectification.csv"
cleaned_file = "D:/python-project/课后作业/output/construction_hazard_rectification_threshold5_cleaned.csv"
report_file = "D:/python-project/课后作业/output/construction_hazard_rectification_threshold5_report.txt"

with open(input_file, encoding="utf-8") as f:
    csv_text = f.read()

line_list = csv_text.splitlines()

raw_record_list  = []

for line in line_list:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "整改单号,隐患等级,整改状态,复核结果,逾期天数,整改费用"
    ):
        raw_record_list.append(clean_line)

urgent_rectification_order_list = []    #紧急整改整改单列表

pending_rectification_order_list = []       #待整改整改单列表

pending_review_order_list = []          #待复核整改单列表

returned_rectification_order_list = []      #退回整改整改单列表
closable_order_list = []            #可结案整改单列表

overdue_closed_order_list = []          #逾期结案整改单列表

cleaned_record_list = []

invalid_record_list = []
invalid_reason_list = []

valid_rectification_id_list = []
valid_hazard_level_list = []
valid_rectification_status_list = []
valid_review_result_list = []
valid_overdue_days_list = []
valid_rectification_cost_list = []

total_rectification_cost = 0.0

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 6:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    rectification_id = parts[0].strip()
    hazard_level = parts[1].strip()
    rectification_status = parts[2].strip()
    review_result = parts[3].strip()
    overdue_days_text = parts[4].strip()
    rectification_cost_text = parts[5].strip()

    if (
        rectification_id == ""
        or hazard_level == ""
        or rectification_status == ""
        or review_result == ""
        or overdue_days_text == ""
        or rectification_cost_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        hazard_level != "高"
        and hazard_level != "中"
        and hazard_level != "低"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("隐患等级不符合, 原始记录: " + raw_record)
        continue

    if (
        rectification_status != "已整改"
        and rectification_status != "未整改"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("整改状态不符合, 原始记录: " + raw_record)
        continue

    if (
        review_result != "未复核"
        and review_result != "通过"
        and review_result != "不通过"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("复核结果不符合, 原始记录: " + raw_record)
        continue

    if not overdue_days_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "逾期天数不是整数, 原始记录: " + raw_record
        )
        continue

    if not rectification_cost_text.removeprefix("-").replace(".", "", 1).isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "整改费用不是数字, 原始记录: " + raw_record
        )
        continue

    overdue_days = int(overdue_days_text)
    rectification_cost = float(rectification_cost_text)

    if overdue_days < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "逾期天数小于0, 原始记录: " + raw_record
        )
        continue

    if rectification_cost < 0:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "整改费用小于0, 原始记录: " + raw_record
        )
        continue

    if rectification_status == "未整改" and review_result != "未复核":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未整改却出现复核结果, 原始记录: " + raw_record)
        continue

    valid_rectification_id_list.append(rectification_id)
    valid_hazard_level_list.append(hazard_level)
    valid_rectification_status_list.append(rectification_status)
    valid_review_result_list.append(review_result)
    valid_overdue_days_list.append(overdue_days)
    valid_rectification_cost_list.append(rectification_cost)

    cleaned_record_list.append(
        rectification_id
        + ","
        + hazard_level
        + ","
        + rectification_status
        + ","
        + review_result
        + ","
        + str(overdue_days)
        + ","
        + str(rectification_cost)
    )

    total_rectification_cost += rectification_cost

    if rectification_status == "未整改":
        if hazard_level == "高":
            urgent_rectification_order_list.append(rectification_id)
        else:
            pending_rectification_order_list.append(rectification_id)

    elif rectification_status == "已整改":
        if review_result == "未复核":
            pending_review_order_list.append(rectification_id)
        elif review_result == "不通过":
            returned_rectification_order_list.append(rectification_id)
        elif review_result == "通过" and overdue_days <= 5:
            closable_order_list.append(rectification_id)
        elif review_result == "通过" and overdue_days > 5:
            overdue_closed_order_list.append(rectification_id)

raw_count = len(raw_record_list)
valid_count = len(valid_rectification_id_list)
invalid_count = len(invalid_record_list)

urgent_rectification_count = len(urgent_rectification_order_list)
pending_rectification_count = len(pending_rectification_order_list)
pending_review_count = len(pending_review_order_list)
returned_rectification_count = len(returned_rectification_order_list)
closable_count = len(closable_order_list)
overdue_closed_count = len(overdue_closed_order_list)

final_conclusion = ""

if invalid_count > 0:
    final_conclusion = "数据需要人工更正，统计结论不完整"

elif urgent_rectification_count > 0:
    final_conclusion = "存在高风险未整改隐患，立即处理"
elif returned_rectification_count > 0:
    final_conclusion = "存在复核不通过隐患，不能结案"
elif pending_review_count > 0:
    final_conclusion = "存在待复核整改单"
elif pending_rectification_count > 0:
    final_conclusion = "存在未整改隐患"
elif overdue_closed_count > 0:
    final_conclusion = "已结案但存在逾期记录，需要复盘"

else:
    final_conclusion = "全部整改单正常结案"

print("施工隐患整改结案判断报告")
print("============================")

print("原始记录数量:", raw_count)
print("有效记录数量:", valid_count)
print("无效记录数量:", invalid_count)

print()
print("紧急整改数量:", urgent_rectification_count)
print("待整改数量:", pending_rectification_count)
print("待复核数量:", pending_review_count)
print("退回整改数量:", returned_rectification_count)
print("可结案数量:", closable_count)
print("逾期结案数量:", overdue_closed_count)

print()
print("有效整改费用合计:", total_rectification_cost)

print()
print("紧急整改整改单:", urgent_rectification_order_list)
print("待整改整改单:", pending_rectification_order_list)
print("待复核整改单:", pending_review_order_list)
print("退回整改整改单:", returned_rectification_order_list)
print("可结案整改单:", closable_order_list)
print("逾期结案整改单:", overdue_closed_order_list)

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

with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("整改单号,隐患等级,整改状态,复核结果,逾期天数,整改费用\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")

with open(report_file, "w", encoding="utf-8") as f:
    f.write("施工隐患整改结案判断报告\n")
    f.write("============================\n")

    f.write("原始记录数量: " + str(raw_count) + "\n")
    f.write("有效记录数量: " + str(valid_count) + "\n")
    f.write("无效记录数量: " + str(invalid_count) + "\n")

    f.write("\n")
    f.write("紧急整改数量: " + str(urgent_rectification_count) + "\n")
    f.write("待整改数量: " + str(pending_rectification_count) + "\n")
    f.write("待复核数量: " + str(pending_review_count) + "\n")
    f.write("退回整改数量: " + str(returned_rectification_count) + "\n")
    f.write("可结案数量: " + str(closable_count) + "\n")
    f.write("逾期结案数量: " + str(overdue_closed_count) + "\n")

    f.write("\n")
    f.write("有效整改费用合计: " + str(total_rectification_cost) + "\n")

    f.write("\n紧急整改整改单:\n")
    for rectification_id in urgent_rectification_order_list:
        f.write(rectification_id + "\n")

    f.write("\n待整改整改单:\n")
    for rectification_id in pending_rectification_order_list:
        f.write(rectification_id + "\n")

    f.write("\n待复核整改单:\n")
    for rectification_id in pending_review_order_list:
        f.write(rectification_id + "\n")

    f.write("\n退回整改整改单:\n")
    for rectification_id in returned_rectification_order_list:
        f.write(rectification_id + "\n")

    f.write("\n可结案整改单:\n")
    for rectification_id in closable_order_list:
        f.write(rectification_id + "\n")

    f.write("\n逾期结案整改单:\n")
    for rectification_id in overdue_closed_order_list:
        f.write(rectification_id + "\n")

    f.write("\n无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n最终结论: " + final_conclusion + "\n")