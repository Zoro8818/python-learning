required_list = ["营业执照", "法人身份证", "授权委托书", "财务报表", "纳税证明", "安全生产许可证"]

raw_submitted_list = [
    "营业执照",
    "法人身份证",
    "法人身份证",
    "授权委托书",
    "公司简介",
    "财务报表",
    "",
    "开户许可证",
    "营业执照"
]

submitted_list = []  # 有效提交资料列表
invalid_list = []  # 无效资料列表
duplicate_list = []  # 重复提交资料列表
checked_submitted_list = []  # 已确认提交的必备资料列表
missing_list = []  # 缺失资料列表
extra_list = []  # 多余资料列表

invalid_count = 0
duplicate_count = 0

for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()

    if clean_material == "":
        invalid_list.append(submitted_material)
        invalid_count += 1
    elif clean_material in submitted_list:
        duplicate_list.append(clean_material)
        duplicate_count += 1
    else:
        submitted_list.append(clean_material)

for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
    else:
        missing_list.append(required_material)

for submitted_material in submitted_list:
    if submitted_material not in required_list:
        extra_list.append(submitted_material)


submitted_count = len(checked_submitted_list)
missing_count = len(missing_list)
extra_count = len(extra_list)

print("# 招投标资料检查报告")
print()

print("## 清洗后的有效提交资料")
print(submitted_list)
print()

print("## 无效资料")
print(invalid_list)
print("无效资料数量:", invalid_count)
print()

print("## 重复提交资料")
print(duplicate_list)
print("重复提交资料数量:", duplicate_count)
print()

print("## 已确认提交的必备资料")
print(checked_submitted_list)
print("已确认提交的必备资料数量:", submitted_count)
print()

print("## 缺失资料")
print(missing_list)
print("缺失资料数量:", missing_count)
print()

print("## 多余资料")
print(extra_list)
print("多余资料数量:", extra_count)
print()

print("## 最终状态")
if len(missing_list) == 0:
    print("资料齐全")
else:
    print("资料不齐，需要补交")

print("本次资料检查结果如下: ")
print()

print("客户已提交的必备资料包括: ", checked_submitted_list)
print("目前仍缺失: ", missing_list)
print("另发现多余资料: ", extra_list)

print("无效空项数量：", invalid_count)
print("重复提交资料包括：", duplicate_list)
print("重复提交资料数量：", duplicate_count)

print("综上，本次资料不齐，需要补交: ", missing_list)


