required_list = ["报名表", "营业执照", "资质证书", "报价单", "项目负责人证明"]

key_required_list = ["营业执照", "资质证书"]

raw_submitted_list = [
    "报名表",
    " 营业执照 ",
    "营业执照",
    "项目负责人证明",
    "",
    "情况说明",
    "报价单",
    "   ",
    "补充承诺函"
]

# 1. 准备结果列表
submitted_list = []  # 有效提交资料列表
invalid_list = []  # 无效资料列表
duplicate_list = []  # 重复提交资料列表

checked_submitted_list = []  # 已确认提交的必备资料列表
missing_list = []  # 缺失资料列表
key_missing_list = []  # 缺失的关键必备资料列表
extra_list = []  # 多余资料列表

# 2. 清洗原始提交资料
for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()

    if clean_material == "":
        invalid_list.append(submitted_material)
    elif clean_material in submitted_list:
        duplicate_list.append(clean_material)
    else:
        submitted_list.append(clean_material)

# 3. 检查必备资料：生成 checked_submitted_list 和 missing_list
for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
    else:
        missing_list.append(required_material)

# 4. 检查关键缺失资料：从 missing_list 里筛出关键资料
for missing_material in missing_list:
    if missing_material in key_required_list:
        key_missing_list.append(missing_material)

# 5. 检查多余资料
for submitted_material in submitted_list:
    if submitted_material not in required_list:
        extra_list.append(submitted_material)

# 6. 统计数量
submitted_count = len(checked_submitted_list)
missing_count = len(missing_list)
key_missing_count = len(key_missing_list)
extra_count = len(extra_list)
invalid_count = len(invalid_list)
duplicate_count = len(duplicate_list)

# 7. 输出报告
print("本次资料检查结果如下：")
print()

print("客户已提交的必备资料包括：", checked_submitted_list)
print("目前仍缺失资料：", missing_list)
print("缺失关键必备资料包括：", key_missing_list)
print("另发现多余资料：", extra_list)
print("无效资料包括：", invalid_list)
print("重复提交资料包括：", duplicate_list)

print("已提交必备资料数量：", submitted_count)
print("缺失资料数量：", missing_count)
print("缺失关键必备资料数量：", key_missing_count)
print("多余资料数量：", extra_count)
print("无效资料数量：", invalid_count)
print("重复提交资料数量：", duplicate_count)

print()
print("最终结论：")

if len(missing_list) == 0:
    print("本次必备资料已提交齐全。")
else:
    print("本次资料不齐，需要补交以下资料：", missing_list)

if len(key_missing_list) == 0:
    print("本次关键必备资料已提交齐全。")
else:
    print("缺少关键资料，风险较高：", key_missing_list)
