# 1. 路径设置
input_file = "D:/python-project/课后作业/input/tender_materials.csv"
report_file = "D:/python-project/课后作业/output/tender_materials_report.txt"
checked_file = "D:/python-project/课后作业/output/tender_materials_checked.csv"


with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

lines = csv_text.splitlines()

raw_record_list = []

# 第一层：排除表头和空行，空行不计入业务无效资料。
for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "资料名称,提交状态,是否必需":
        raw_record_list.append(clean_line)


submitted_material_list = []    # 已提交资料列表
missing_material_list = []      # 所有缺失资料列表
required_missing_list = []      # 必需但缺失资料列表
checked_record_list = []        # 最终要写进检查结果 CSV 的每一行
invalid_reason_list = []        # 无效数据的具体原因列表

checked_record_list.append("资料名称,提交状态,是否必需,检查结果,问题说明")
# 无效数据数量在校验阶段累加，不让无效记录进入正常业务统计。
invalid_count = 0

# 第二层：逐条校验字段、允许值，再进入已提交或缺失分类。
for record in raw_record_list:
    parts = record.split(",")

    # 字段数量正确后才能读取固定位置的三个字段。
    if len(parts) != 3:
        invalid_count += 1
        invalid_reason_list.append("字段数量错误：" + record)
        checked_record_list.append(
            "无法解析,,,无效,字段数量错误，原始记录：" + record.replace(",", "，")
        )
    else:
        material_name = parts[0].strip()
        submit_status = parts[1].strip()
        is_required = parts[2].strip()

        # 先隔离结构、空值和允许值不合法的记录。
        if material_name == "" or submit_status == "" or is_required == "":
            invalid_count += 1
            invalid_reason_list.append("字段为空：" + "，原始记录：" + record)
            checked_record_list.append(
                material_name + "," + submit_status + "," + is_required
                + ",无效,字段为空"
            )
        elif submit_status != "已提交" and submit_status != "缺失":
            invalid_count += 1
            invalid_reason_list.append(
                "提交状态不合法：" + submit_status + "，原始记录：" + record
            )
            checked_record_list.append(
                material_name + "," + submit_status + "," + is_required
                + ",无效,提交状态不合法"
            )
        elif is_required != "是" and is_required != "否":
            invalid_count += 1
            invalid_reason_list.append(
                "是否必需不合法：" + is_required + "，原始记录：" + record
            )
            checked_record_list.append(
                material_name + "," + submit_status + "," + is_required
                + ",无效,是否必需不合法"
            )

        else:
            # 只有完全合法的记录才能进入正常业务分类。
            if submit_status == "已提交":
                submitted_material_list.append(material_name)
                checked_record_list.append(
                    material_name + "," + submit_status + "," + is_required + ",通过,"
                )

            elif submit_status == "缺失":
                missing_material_list.append(material_name)
                if is_required == "是":
                    required_missing_list.append(material_name)
                    checked_record_list.append(
                        material_name + "," + submit_status + "," + is_required + ",不通过,必需资料缺失"
                    )

                else:
                    checked_record_list.append(
                        material_name + "," + submit_status + "," + is_required + ",提醒,非必需资料缺失"
                    )

raw_count = len(raw_record_list)
submitted_material_count = len(submitted_material_list)
missing_material_count = len(missing_material_list)
required_missing_count = len(required_missing_list)

# 最终结论优先级：关键缺失 > 无效资料 > 通过。
if required_missing_count > 0:
    conclusion = "资料不齐，需要补交关键资料"

elif invalid_count > 0:
    conclusion = "存在无效资料，需要先修正数据"

else:
    conclusion = "关键必备资料已提交齐全，检查通过"

# 输出逐条检查结果，供业务人员核对每条记录的处理原因。
with open(checked_file, "w", encoding="utf-8") as f:
    for checked_record in checked_record_list:
        f.write(checked_record + "\n")


# 输出汇总报告，保留数量、无效原因和最终结论。
with open(report_file, "w", encoding="utf-8") as f:
    f.write("招投标资料检查报告\n")
    f.write("================\n")

    f.write("原始资料数量：" + str(raw_count) + "\n")
    f.write("已提交资料数量：" + str(submitted_material_count) + "\n")
    f.write("无效资料数量：" + str(invalid_count) + "\n")
    f.write("缺失资料数量：" + str(missing_material_count) + "\n")
    f.write("必需缺失资料数量：" + str(required_missing_count) + "\n")

    f.write("无效资料明细：\n")

    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("检查结论：" + conclusion + "\n")



