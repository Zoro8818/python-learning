customers = ["张三", "李四", "王五", "赵六", "孙八"]
amounts = [1200.5, 860.0, 2380.0, 450.0, 300.5]

invalid_count = 2
valid_count = len(amounts)
total_amount = sum(amounts)

if valid_count > 0:
    avg_amount = total_amount / valid_count

    max_amount = amounts[0]
    max_customer = customers[0]

    min_amount = amounts[0]
    min_customer = customers[0]

    for i in range(valid_count):
        if max_amount < amounts[i]:
            max_amount = amounts[i]
            max_customer = customers[i]

        if min_amount > amounts[i]:
            min_amount = amounts[i]
            min_customer = customers[i]

else:
    avg_amount = 0
    max_amount = 0
    max_customer = ""
    min_amount = 0
    min_customer = ""

print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高客户: ", max_customer, ", 最高金额: ", max_amount)
print("最低客户: ", min_customer, ", 最低金额: ", min_amount)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("有效数据数量: " + str(valid_count) + "\n")
    f.write("无效数据数量: " + str(invalid_count) + "\n")
    f.write("总金额: " + str(total_amount) + "\n")
    f.write("平均金额: " + str(round(avg_amount, 2)) + "\n")
    f.write("最高客户: " + max_customer + ", 最高金额: " + str(max_amount) + "\n")
    f.write("最低客户: " + min_customer + ", 最低金额: " + str(min_amount) + "\n")





