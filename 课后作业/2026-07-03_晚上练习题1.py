required_list = ["报名表", "营业执照", "资质证书", "报价单", "项目负责人证明"]

key_required_list = ["营业执照", "资质证书"]

raw_submitted_list = [
    "报名表",
    "报价单",
    "报价单",
    "项目负责人证明",
    "情况说明",
    "",
    "   ",
    "补充材料"
]

submitted_list = []
invalid_list = []
duplicate_list = []
checked_submitted_list = []
missing_list = []
key_missing_list = []
extra_list = []
suggestion_list = []

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

submitted_count = len(checked_submitted_list)
missing_count = len(missing_list)
key_missing_count = len(key_missing_list)
extra_count = len(extra_list)
invalid_count = len(invalid_list)
duplicate_count = len(duplicate_list)
suggestion_count = len(suggestion_list)

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
print("整改建议数量：", suggestion_count)

print()
print("整改建议如下：")
print(suggestion_list)

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