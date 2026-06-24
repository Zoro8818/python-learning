# 题目：客户订单金额统计
#
# 要求：
# 用 record 遍历 order_records
# 清洗整条记录
# 空记录算无效
# 不包含 ":" 算无效
# 用 split(":", 1) 拆成 customer 和 amount_text
# 客户名为空算无效
# 金额文本为空算无效
# 金额文本必须先判断是不是合法数字，再 float() 转换
# 有效客户名保存到 valid_customer_list
# 有效金额保存到 valid_amount_list
# 无效记录数量用 invalid_count 统计
# 累加订单总金额 total_amount
#
# 额外要求：
# 计算平均订单金额 avg_amount
# 找出最高订单客户 max_customer
# 找出最高订单金额 max_amount
# 找出最低订单客户 min_customer
# 找出最低订单金额 min_amount
#
# 输出：
# 有效客户数量
# 有效客户名单
# 无效记录数量
# 订单总金额
# 平均订单金额，保留 2 位小数
# 最高订单客户
# 最高订单金额
# 最低订单客户
# 最低订单金额

order_records = [
    "张三: 120.5",
    "李四:80",
    "王五:",
    " :200",
    "赵六:abc",
    "",
    "钱七: 300",
    "孙八:50",
    "周九:0",
    "吴十: 999.9"
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

        if customer == "" or amount_text == "" :
            invalid_count += 1

        elif amount_text.replace(".", "" ,1).isdigit():
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

print("有效客户数量:", len(valid_amount_list))
print("有效客户名单:", valid_customer_list)
print("无效记录数量:", invalid_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))
print("最高订单客户:", max_customer)
print("最高订单金额:", max_amount)
print("最低订单客户:", min_customer)
print("最低订单金额:", min_amount)
