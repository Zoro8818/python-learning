# 要求输出：
#
# 有效客户数量
# 有效客户名单
# 有效金额列表
# 无效记录数量
# 总金额
# 平均金额，保留 2 位小数
# 最高消费客户
# 最高消费金额
# 最低消费客户
# 最低消费金额
#
# 你必须完成这些步骤：有效客户数量
# 有效客户名单
# 有效金额列表
# 无效记录数量
# 总金额
# 平均金额，保留 2 位小数
# 最高消费客户
# 最高消费金额
# 最低消费客户
# 最低消费金额

order_records = [
    "张三: 88.5",
    "李四: 120",
    "王五:",
    " :76",
    "赵六:abc",
    "",
    "钱七: 60",
    "孙八:0",
    "周九:300.5",
    "吴十: 72"
]

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0

for record in order_records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

    max_amount = valid_amount_list[0]
    max_customer = valid_customer_list[0]

    min_amount = valid_amount_list[0]
    min_customer = valid_customer_list[0]

    for i in range(len(valid_amount_list)):
        if valid_amount_list[i] > max_amount:
            max_amount = valid_amount_list[i]
            max_customer = valid_customer_list[i]

        if valid_amount_list[i] < min_amount:
            min_amount = valid_amount_list[i]
            min_customer = valid_customer_list[i]

else:
    avg_amount = 0
    max_amount = 0
    max_customer = ""
    min_amount = 0
    min_customer = ""

print("有效客户数量:", len(valid_customer_list))
print("有效客户名单:", valid_customer_list)
print("有效金额列表:", valid_amount_list)
print("无效记录数量:", invalid_count)
print("总金额:", total_amount)
print("平均金额:", round(avg_amount, 2))
print("最高消费客户:", max_customer)
print("最高消费金额:", max_amount)
print("最低消费客户:", min_customer)
print("最低消费金额:", min_amount)


