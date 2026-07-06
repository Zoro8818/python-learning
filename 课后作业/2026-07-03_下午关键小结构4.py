missing_list = ["报价单"]
key_missing_list = []
extra_list = ["情况说明", "补充材料"]
duplicate_list = ["资质证书"]
invalid_list = ["", "   "]

suggestion_list = []

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

print("整改建议如下：")
print(suggestion_list)
