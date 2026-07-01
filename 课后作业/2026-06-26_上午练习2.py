valid_count = 3
invalid_count = 1
total_amount = 3560.5
avg_amount = 1186.83
max_customer = "王五"
max_amount = 2380.0
min_customer = "李四"
min_amount = 320.5

print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高客户: ", max_customer)
print("最高金额: ", max_amount)
print("最低客户: ", min_customer)
print("最低金额: ", min_amount)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("无效数据数量: " + str(invalid_count) + "\n")
    f.write("总金额: " + str(total_amount) + "\n")
    f.write("平均金额: " + str(round(avg_amount, 2)) + "\n")
    f.write("最高客户: " + max_customer + "\n")
    f.write("最高金额: " + str(max_amount) + "\n")
    f.write("最低客户: " + min_customer + "\n")
    f.write("最低金额: " + str(min_amount) + "\n")