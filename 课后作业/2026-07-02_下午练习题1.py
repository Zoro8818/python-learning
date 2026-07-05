required_list = ["营业执照", "法人身份证", "授权委托书", "财务报表"]  # 必备资料列表

raw_submitted_list = [" 营业执照", "法人身份证 ", " ", "授权委托书", "公司简介", "", " 财务报表 ", "开户许可证"]  # 原始提交资料列表

submitted_list = []  # 有效提交资料列表：清洗后、去掉空项后的资料
invalid_list = []  # 无效资料列表：空字符串、全是空格的资料
checked_submitted_list = []  # 已确认提交的必备资料列表
missing_list = []  # 缺失资料列表：必备但客户没交的资料
extra_list = []  # 多余资料列表：客户交了但不是必备的资料

invalid_count = 0  # 无效资料数量

for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()

    if clean_material == "":
        invalid_list.append(submitted_material)
        invalid_count += 1
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

submitted_count = len(checked_submitted_list)  # 已确认提交的必备资料数量
missing_count = len(missing_list)  # 缺失资料数量
extra_count = len(extra_list)  # 多余资料数量

print("# 招投标资料检查报告")
print()

print("## 清洗后的有效提交资料")
print(submitted_list)
print()

print("## 无效资料")
print(invalid_list)
print("无效资料数量:", invalid_count)
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
