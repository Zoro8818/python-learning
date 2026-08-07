input_file = "D:/python-project/课后作业/input/software_test_batch_release_review.csv"
cleaned_file = "D:/python-project/课后作业/output/software_test_batch_release_review_cleaned.csv"
report_file = "D:/python-project/课后作业/output/software_test_batch_release_review_report.txt"

with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    raw_record = line.strip()

    if (
        raw_record != ""
        and raw_record != "测试批次编号,测试执行状态,发布评审状态,未关闭缺陷数量"
    ):
        raw_record_list.append(raw_record)

# 有效、无效结果
valid_record_list = []
invalid_record_list = []
invalid_reason_list = []

# 有效记录分类
defect_excess_review_list = []       # 缺陷超标复核列表
waiting_test_execution_list = []     # 等待测试执行列表
waiting_release_review_list = []     # 等待发布评审列表
test_rectification_list = []         # 测试整改列表
release_allowed_list = []            # 允许发布列表

# ============================================================
# 核心处理区：由你独立完成
# ============================================================

for raw_record in raw_record_list:
    parts = raw_record.split(",")

    if len(parts) != 4:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录：" + raw_record)
        continue

    test_batch_id = parts[0].strip()
    test_execution_status = parts[1].strip()
    release_review_status = parts[2].strip()
    unclosed_defect_count_text = parts[3].strip()

    if (
        test_batch_id == ""
        or test_execution_status == ""
        or release_review_status == ""
        or unclosed_defect_count_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        test_execution_status != "未执行"
        and test_execution_status != "已执行"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("测试执行状态不合法, 原始记录: " + raw_record)
        continue

    if (
        release_review_status != "待评审"
        and release_review_status != "通过"
        and release_review_status != "不通过"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("发布评审状态不合法, 原始记录: " + raw_record)
        continue

    if not unclosed_defect_count_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未关闭缺陷数量不是有效整数, 原始记录: " + raw_record)
        continue

    unclosed_defect_count = int(unclosed_defect_count_text)

    if unclosed_defect_count < 0 or unclosed_defect_count > 50:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("未关闭缺陷数量必须是0—50 的整数, 原始记录: " + raw_record)
        continue

    if (
        test_execution_status == "未执行"
        and release_review_status != "待评审"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "未执行时发布评审状态只能是待评审, 原始记录: " + raw_record
        )
        continue

    if (
        test_execution_status == "未执行"
        and unclosed_defect_count != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "未执行时未关闭缺陷数量必须等于 0, 原始记录: " + raw_record
        )
        continue

    clean_record = (
        test_batch_id
        + ","
        + test_execution_status
        + ","
        + release_review_status
        + ","
        + str(unclosed_defect_count)
    )

    valid_record_list.append(clean_record)

    if unclosed_defect_count > 5:
        defect_excess_review_list.append(test_batch_id)
    elif (
        test_execution_status == "未执行"
        and release_review_status == "待评审"
    ):
        waiting_test_execution_list.append(test_batch_id)
    elif (
        test_execution_status == "已执行"
        and release_review_status == "待评审"
    ):
        waiting_release_review_list.append(test_batch_id)
    elif (
        test_execution_status == "已执行"
        and release_review_status == "不通过"
    ):
        test_rectification_list.append(test_batch_id)
    else:
        release_allowed_list.append(test_batch_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

defect_excess_review_count = len(defect_excess_review_list)
waiting_test_execution_count = len(waiting_test_execution_list)
waiting_release_review_count = len(waiting_release_review_list)
test_rectification_count = len(test_rectification_list)
release_allowed_count = len(release_allowed_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "当前审核结果仅供参考，需修正后重新审核"
elif defect_excess_review_count > 0:
    review_conclusion = "存在缺陷超标批次，需要优先复核"
elif test_rectification_count > 0:
    review_conclusion = "存在未通过发布评审的批次，需要整改"
elif waiting_test_execution_count > 0 or waiting_release_review_count > 0:
    review_conclusion = "发布流程尚未完成"
else:
    review_conclusion = "测试批次均可允许发布"


# ============================================================
# 机械统计与输出区
# ============================================================

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

defect_excess_review_count = len(defect_excess_review_list)
waiting_test_execution_count = len(waiting_test_execution_list)
waiting_release_review_count = len(waiting_release_review_list)
test_rectification_count = len(test_rectification_list)
release_allowed_count = len(release_allowed_list)

if invalid_record_count > 0:
    final_conclusion = "当前审核结果仅供参考，需修正后重新审核"
elif defect_excess_review_count > 0:
    final_conclusion = "存在缺陷超标批次，需要优先复核"
elif test_rectification_count > 0:
    final_conclusion = "存在未通过发布评审的批次，需要整改"
elif waiting_test_execution_count > 0 or waiting_release_review_count > 0:
    final_conclusion = "发布流程尚未完成"
else:
    final_conclusion = "测试批次均可允许发布"

cleaned_csv_text = "测试批次编号,测试执行状态,发布评审状态,未关闭缺陷数量\n"

if valid_record_count > 0:
    cleaned_csv_text += "\n".join(valid_record_list) + "\n"

with open(cleaned_file, "w", encoding="utf-8") as file:
    file.write(cleaned_csv_text)

report_text = "软件测试批次发布审核报告\n"
report_text += "=" * 40 + "\n"
report_text += "原始记录数量: " + str(raw_record_count) + "\n"
report_text += "有效记录数量: " + str(valid_record_count) + "\n"
report_text += "无效记录数量: " + str(invalid_record_count) + "\n\n"

report_text += "缺陷超标复核数量: " + str(defect_excess_review_count) + "\n"
report_text += "等待测试执行数量: " + str(waiting_test_execution_count) + "\n"
report_text += "等待发布评审数量: " + str(waiting_release_review_count) + "\n"
report_text += "测试整改数量: " + str(test_rectification_count) + "\n"
report_text += "允许发布数量: " + str(release_allowed_count) + "\n\n"

report_text += "缺陷超标复核批次: " + str(defect_excess_review_list) + "\n"
report_text += "等待测试执行批次: " + str(waiting_test_execution_list) + "\n"
report_text += "等待发布评审批次: " + str(waiting_release_review_list) + "\n"
report_text += "测试整改批次: " + str(test_rectification_list) + "\n"
report_text += "允许发布批次: " + str(release_allowed_list) + "\n\n"

report_text += "无效记录及原因:\n"

if invalid_record_count == 0:
    report_text += "无\n"
else:
    for invalid_reason in invalid_reason_list:
        report_text += invalid_reason + "\n"

report_text += "\n最终结论: " + final_conclusion + "\n"

with open(report_file, "w", encoding="utf-8") as file:
    file.write(report_text)

print(report_text)
