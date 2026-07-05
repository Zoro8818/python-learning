# 1. 路径设置
input_file = "D:/python-project/课后作业/input/input.txt"
report_file = "D:/python-project/课后作业/output/report.txt"

# 2. 必备资料清单
required_list = [
    "营业执照",
    "法人身份证",
    "授权委托书",
    "报价单",
    "项目实施方案",
    "售后服务承诺",
    "纳税证明",
    "近三年业绩证明"
]

key_required_list = [
    "营业执照",
    "法人身份证",
    "报价单",
    "项目实施方案"
]

# 3. 读取 input.txt
with open(input_file, "r", encoding="utf-8") as f:
    submitted_text = f.read()

raw_submitted_list = submitted_text.splitlines()

# 4. 准备结果列表
submitted_list = []  # 有效提交资料列表
key_missing_list = []  # 缺失的关键必备资料列表
invalid_list = []  # 无效资料列表
duplicate_list = []  # 重复提交资料列表
checked_submitted_list = []  # 已确认提交的必备资料列表
missing_list = []  # 缺失资料列表
extra_list = []  # 多余资料列表
suggestion_list = []    # 整改建议列表

# 5. A++ 核心处理
for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()

    if clean_material == "":
        invalid_list.append(submitted_material)
    elif clean_material in submitted_list:
        duplicate_list.append(clean_material)
    else:
        submitted_list.append(clean_material)

for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
    else:
        missing_list.append(required_material)

# 6. 生成整改建议
for missing_material in missing_list:
    if missing_material in key_required_list:
        key_missing_list.append(missing_material)

for submitted_material in submitted_list:
    if submitted_material not in required_list:
        extra_list.append(submitted_material)

for missing_material in missing_list:
    suggestion_list.append("请补交必备资料：" + missing_material)

for key_missing_material in key_missing_list:
    suggestion_list.append("关键资料缺失，请优先处理：" + key_missing_material)

for extra_material in extra_list:
    suggestion_list.append("请确认是否需要保留多余资料：" + extra_material)

for duplicate_material in duplicate_list:
    suggestion_list.append("请删除重复提交资料：" + duplicate_material)

if len(invalid_list) > 0:
    suggestion_list.append("请清理空白无效资料项。")

# 7. 数量统计
submitted_count = len(checked_submitted_list)
missing_count = len(missing_list)
key_missing_count = len(key_missing_list)
extra_count = len(extra_list)
invalid_count = len(invalid_list)
duplicate_count = len(duplicate_list)
suggestion_count = len(suggestion_list)

# 8. 写入 report.txt
with open(report_file, "w", encoding="utf-8") as f:
    f.write("招投标资料检查报告\n")
    f.write("=" * 30 + "\n")
    f.write("\n")

    f.write("一、资料检查明细\n")
    f.write("-" * 30 + "\n")
    f.write("已提交的必备资料：" + str(checked_submitted_list) + "\n")
    f.write("缺失的必备资料：" + str(missing_list) + "\n")
    f.write("缺失的关键必备资料：" + str(key_missing_list) + "\n")
    f.write("多余资料：" + str(extra_list) + "\n")
    f.write("无效资料：" + str(invalid_list) + "\n")
    f.write("重复提交资料：" + str(duplicate_list) + "\n")
    f.write("\n")

    f.write("二、数量统计\n")
    f.write("-" * 30 + "\n")
    f.write("已提交必备资料数量：" + str(submitted_count) + "\n")
    f.write("缺失资料数量：" + str(missing_count) + "\n")
    f.write("缺失关键必备资料数量：" + str(key_missing_count) + "\n")
    f.write("多余资料数量：" + str(extra_count) + "\n")
    f.write("无效资料数量：" + str(invalid_count) + "\n")
    f.write("重复提交资料数量：" + str(duplicate_count) + "\n")
    f.write("整改建议数量：" + str(suggestion_count) + "\n")
    f.write("\n")

    f.write("三、整改建议\n")
    f.write("-" * 30 + "\n")
    if len(suggestion_list) == 0:
        f.write("暂无整改建议。\n")
    else:
        f.write(str(suggestion_list) + "\n")
    f.write("\n")

    f.write("四、最终结论\n")
    f.write("-" * 30 + "\n")

    if len(missing_list) == 0:
        f.write("本次必备资料已提交齐全。\n")
    else:
        f.write("本次资料不齐，需要补交以下资料：" + str(missing_list) + "\n")

    if len(key_missing_list) == 0:
        f.write("本次关键必备资料已提交齐全。\n")
    else:
        f.write("缺少关键资料，风险较高：" + str(key_missing_list) + "\n")
