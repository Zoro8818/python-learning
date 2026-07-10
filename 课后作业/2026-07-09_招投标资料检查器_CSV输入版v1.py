# 1. 路径设置
input_file = "D:/python-project/课后作业/input/tender_materials.csv"
report_file = "D:/python-project/课后作业/output/tender_materials_report.txt"


with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()

lines = csv_text.splitlines()

raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "资料名称,提交状态,是否必需":
        raw_record_list.append(clean_line)


submitted_material_list = []    # 已提交资料列表
missing_material_list = []      # 所有缺失资料列表
required_missing_list = []      # 必需但缺失资料列表

# 统计数量
invalid_count = 0

# 5. A++ 核心处理
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        material_name = parts[0].strip()
        submit_status = parts[1].strip()
        is_required = parts[2].strip()

        if material_name == "" or submit_status == "" or is_required == "":
            invalid_count += 1
        elif submit_status != "已提交" and submit_status != "缺失":
            invalid_count += 1
        elif is_required != "是" and is_required != "否":
            invalid_count += 1

        else:
            if submit_status == "已提交":
                submitted_material_list.append(material_name)
            elif submit_status == "缺失":
                missing_material_list.append(material_name)

                if is_required == "是":
                    required_missing_list.append(material_name)

raw_count = len(raw_record_list)
submitted_material_count = len(submitted_material_list)
missing_material_count = len(missing_material_list)
required_missing_count = len(required_missing_list)

if required_missing_count == 0:
    conclusion = "关键必备资料已提交齐全"
else:
    conclusion = "资料不齐，需要补交关键资料"

with open(report_file, "w", encoding="utf-8") as f:
    f.write("招投标资料检查报告\n")
    f.write("================\n")

    f.write("原始资料数量：" + str(raw_count) + "\n")
    f.write("已提交资料数量：" + str(submitted_material_count) + "\n")
    f.write("缺失资料数量：" + str(missing_material_count) + "\n")
    f.write("必需缺失资料数量：" + str(required_missing_count) + "\n")

    f.write("检查结论：" + conclusion + "\n")



