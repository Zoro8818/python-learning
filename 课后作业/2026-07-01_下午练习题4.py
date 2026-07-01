required_list = ["营业执照", "法人身份证", "授权委托书", "财务报表", "安全生产许可证", "纳税证明"]

submitted_list = ["营业执照", "授权委托书", "安全生产许可证"]
checked_submitted_list = []
missing_list = []
submitted_count = 0
missing_count = 0


for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
        submitted_count += 1
    else:
        missing_list.append(required_material)
        missing_count += 1

print("已提交资料列表: ", checked_submitted_list)
print("缺失资料列表: ", missing_list)
print("已提交数量: ", submitted_count)
print("缺失数量: ", missing_count)

if len(missing_list) == 0:
    print("资料齐全")
else:
    print("资料不齐，需要补交")