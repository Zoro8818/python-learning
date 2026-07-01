required_list = ["营业执照", "法人身份证", "授权委托书", "财务报表", "安全生产许可证", "纳税证明"]

raw_submitted_list = [" 营业执照 ", "公司简介", " 授权委托书", "开户许可证 ", " 安全生产许可证 "]

submitted_list = []             # 清洗后的提交资料清单
checked_submitted_list = []     # 已确认提交的必备资料
missing_list = []               # 缺失的必备资料
extra_list = []                 # 多交但不是必备的资料

submitted_count = 0             # 已提交的必备资料数量
missing_count = 0               # 缺失数量
extra_count = 0                 # 多余资料数量

for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()
    submitted_list.append(clean_material)

for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
        submitted_count += 1

    else:
        missing_list.append(required_material)
        missing_count += 1

for submitted_material in submitted_list:
    if submitted_material not in required_list:
        extra_list.append(submitted_material)
        extra_count += 1

print("清洗后的提交资料列表: ", submitted_list)
print("已确认提交的必备资料列表: ", checked_submitted_list)
print("缺失资料列表: ", missing_list)
print("多余资料列表: ", extra_list)

print("已提交的必备资料数量: ", submitted_count)
print("缺失数量: ", missing_count)
print("多余资料数量: ", extra_count)

if len(missing_list) == 0:
    print("资料齐全")
else:
    print("资料不齐，需要补交")
