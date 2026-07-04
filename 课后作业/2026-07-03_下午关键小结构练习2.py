missing_list = ["营业执照", "报价单", "资质证书", "项目负责人证明"]

key_required_list = ["营业执照", "资质证书"]

key_missing_list = []

for missing_material in missing_list:
    if missing_material in key_required_list:
        key_missing_list.append(missing_material)

if len(key_missing_list) == 0:
    print("本次关键必备资料已提交齐全。")
else:
    print("缺少关键资料，风险较高：", key_missing_list)