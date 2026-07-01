#1
# field_list = ['"2026/06/27"', ' AI工具更新 ', ' 中小企业老板 ', ' 企业主 ', ' AI流程清单 ', ' 列3个流程 ', ' 不要夸大 "', '', '']
#
# clean_field_list = []
#
# for field in field_list:
#     clean_field = field.strip().strip('"')
#
#     if clean_field != "":
#         clean_field_list.append(clean_field)
#
# print("清洗后的列表: ", clean_field_list)
# print("字段数量: ", len(clean_field_list))


#2
rows = [
    ['"2026/06/27"', ' AI工具更新 ', ' 中小企业老板 ', ' 企业主 ', ' AI流程清单 ', ' 列3个流程 ', ' 不要夸大 "', '', ''],
    ['2026/06/27', '字段不完整测试', '测试人群', '测试付费方', '测试服务'],
    ['2026/06/27', '物流成本波动', '跨境卖家', '电商团队', '成本跟踪表', '做一张价格对比表', '标明数据来源']
]

invalid_count = 0
valid_rows = []

for row in rows:
    clean_row = []

    for field in row:
        clean_field = field.strip().strip('"').strip()

        if clean_field != "":
            clean_row.append(clean_field)

    if len(clean_row) != 7:
        invalid_count += 1
        continue

    valid_rows.append(clean_row)
valid_count = len(valid_rows)

print("清理后列表: ", valid_rows)
print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)

