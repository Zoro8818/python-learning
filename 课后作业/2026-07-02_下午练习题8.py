#1案例1

checked_submitted_list = ["营业执照", "法人身份证", "授权委托书", "财务报表"]
missing_list = ["纳税证明", "安全生产许可证"]
extra_list = ["公司简介", "开户许可证"]
invalid_count = 1
duplicate_list = ["法人身份证", "营业执照"]
duplicate_count = 2

print("本次资料检查结果如下：")
print()

print("客户已提交的必备资料包括：", checked_submitted_list)
print("目前仍缺失资料：", missing_list)
print("另发现多余资料：", extra_list)
print("无效空项数量：", invalid_count)
print("重复提交资料包括：", duplicate_list)
print("重复提交资料数量：", duplicate_count)

print()
print("最终结论：")
if len(missing_list) == 0:
    print("本次必备资料已提交齐全。")
else:
    print("本次资料不齐，需要补交以下资料：", missing_list)

#案例2
print("-----------------------------------------------分割线---------------------------------------------")

checked_submitted_list = ["营业执照", "法人身份证", "授权委托书", "财务报表", "纳税证明", "安全生产许可证"]
missing_list = []
extra_list = ["公司简介", "开户许可证"]
invalid_count = 1
duplicate_list = ["营业执照", "法人身份证"]
duplicate_count = 2

print("本次资料检查结果如下：")
print()

print("客户已提交的必备资料包括：", checked_submitted_list)
print("目前仍缺失资料：", missing_list)
print("另发现多余资料：", extra_list)
print("无效空项数量：", invalid_count)
print("重复提交资料包括：", duplicate_list)
print("重复提交资料数量：", duplicate_count)

print()
print("最终结论：")
if len(missing_list) == 0:
    print("本次必备资料已提交齐全。")
else:
    print("本次资料不齐，需要补交以下资料：", missing_list)

print("-----------------------------------------------分割线---------------------------------------------")

checked_submitted_list = ["营业执照", "法人身份证", "授权委托书"]
missing_list = ["财务报表", "纳税证明", "安全生产许可证"]
extra_list = []
invalid_count = 0
duplicate_list = []
duplicate_count = 0

print("本次资料检查结果如下：")
print()

print("客户已提交的必备资料包括：", checked_submitted_list)
print("目前仍缺失资料：", missing_list)
print("另发现多余资料：", extra_list)
print("无效空项数量：", invalid_count)
print("重复提交资料包括：", duplicate_list)
print("重复提交资料数量：", duplicate_count)

print()
print("最终结论：")
if len(missing_list) == 0:
    print("本次必备资料已提交齐全。")
else:
    print("本次资料不齐，需要补交以下资料：", missing_list)