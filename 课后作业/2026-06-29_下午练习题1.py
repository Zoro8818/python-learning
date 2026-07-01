#第 1 题
record = "王五:abc"

clean_record = record.strip()


if clean_record == "":
    print("空记录")

elif ":" not in clean_record:
    print("缺冒号")

else:
    parts = clean_record.split(":", 1)
    customer = parts[0].strip()
    amount_text = parts[1].strip()

    if customer == "":
        print("客户名为空")

    elif amount_text == "":
        print("金额为空")

    elif not amount_text.replace(".", "", 1).isdigit():
        print("金额非法")

    else:
        amount = float(amount_text)
        print("有效记录")
        print(customer, amount)


#第 2 题
order_text = "张三:100, , 李四, :200, 王五:, 赵六:abc, 钱七:300"
order_list = order_text.split(",")

invalid_count = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order == "":
        invalid_count += 1
    elif ":" not in clean_order:
        invalid_count += 1
    else:
        parts = clean_order.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "":
            invalid_count += 1
        elif amount_text == "":
            invalid_count += 1
        elif not amount_text.replace(".", "", 1).isdigit():
            invalid_count += 1

print(invalid_count)

#第 3 题
order_text = "张三:100, , 李四, :200, 王五:, 赵六:abc, 钱七:300"
order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0

for record in order_list:
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

        else:
            invalid_count += 1

print("有效客户列表：", valid_customer_list)
print("有效金额列表：", valid_amount_list)
print("无效记录数量：", invalid_count)

#第 4 题
refund_text = "用户A:20, , 用户B, :30, 用户C:, 用户D:abc, 用户E:100"
refund_list = refund_text.split(",")

valid_user_list = []
valid_refund_list = []
invalid_count = 0

for record in refund_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        user = parts[0].strip()
        refund_text_value = parts[1].strip()

        if user == "":
            invalid_count += 1
        elif refund_text_value == "":
            invalid_count += 1
        elif not refund_text_value.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            refund = float(refund_text_value)
            valid_user_list.append(user)
            valid_refund_list.append(refund)

print("有效用户列表：", valid_user_list)
print("有效退款列表：", valid_refund_list)
print("无效记录数量：", invalid_count)

#第 5 题
refund_text = "用户A:20, , 用户B, :30, 用户C:, 用户D:abc, 用户E:100"
refund_list = refund_text.split(",")

valid_user_list = []
valid_refund_list = []
invalid_count = 0

for record in refund_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        user = parts[0].strip()
        refund_text_value = parts[1].strip()

        if user == "":
            invalid_count += 1
        elif refund_text_value == "":
            invalid_count += 1
        elif not refund_text_value.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            refund = float(refund_text_value)
            valid_user_list.append(user)
            valid_refund_list.append(refund)

valid_count = len(valid_refund_list)

print("有效用户列表：", valid_user_list)
print("有效退款列表：", valid_refund_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)

#第 6 题
refund_text = "用户A:20, , 用户B, :30, 用户C:, 用户D:abc, 用户E:100"
refund_list = refund_text.split(",")

valid_user_list = []
valid_refund_list = []
invalid_count = 0
total_refund = 0

for record in refund_list:
    clean_record = record.strip()
    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        user = parts[0].strip()
        refund_text_value = parts[1].strip()

        if user == "":
            invalid_count += 1
        elif refund_text_value == "":
            invalid_count += 1
        elif not refund_text_value.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            refund = float(refund_text_value)
            valid_user_list.append(user)
            valid_refund_list.append(refund)
            total_refund += refund

valid_count = len(valid_refund_list)

print("有效用户列表：", valid_user_list)
print("有效退款列表：", valid_refund_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("总退款金额：", total_refund)

#第 7 题 总退款金额 + 平均退款金额专项
refund_text = "用户A:20, , 用户B, :30, 用户C:, 用户D:abc, 用户E:100"
refund_list = refund_text.split(",")

valid_user_list = []
valid_refund_list = []
invalid_count = 0
total_refund = 0

for record in refund_list:
    clean_record = record.strip()
    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        user = parts[0].strip()
        refund_text_value = parts[1].strip()

        if user == "":
            invalid_count += 1
        elif refund_text_value == "":
            invalid_count += 1
        elif not refund_text_value.replace(".", "", 1).isdigit():
            invalid_count += 1

        else:
            refund = float(refund_text_value)
            valid_user_list.append(user)
            valid_refund_list.append(refund)
            total_refund += refund

valid_count = len(valid_refund_list)

if valid_count > 0:
    avg_refund = total_refund / valid_count
    max_user = valid_user_list[0]
    max_refund = valid_refund_list[0]

    min_user = valid_user_list[0]
    min_refund = valid_refund_list[0]

    for i in range(valid_count):
        if valid_refund_list[i] > max_refund:
            max_user = valid_user_list[i]
            max_refund = valid_refund_list[i]

        if valid_refund_list[i] < min_refund:
            min_user = valid_user_list[i]
            min_refund = valid_refund_list[i]

else:
    avg_refund = 0
    max_user = ""
    max_refund = 0
    min_user = ""
    min_refund = 0

print("有效用户列表：", valid_user_list)
print("有效退款列表：", valid_refund_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("总退款金额：", total_refund)
print("平均退款金额：", avg_refund)
print("最高退款用户：", max_user)
print("最高退款金额：", max_refund)
print("最低退款用户：", min_user)
print("最低退款金额：", min_refund)

#第 8 题 今日核心复盘题｜订单金额清洗统计

order_text = "张三:100, , 李四, :200, 王五:, 赵六:abc, 钱七:300, 孙八:0, 周九:50.5"

order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0

for record in order_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "":
            invalid_count += 1
        elif amount_text == "":
            invalid_count += 1
        elif not amount_text.replace(".", "", 1).isdigit():
            invalid_count += 1
        else:
            amount = float(amount_text)
            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

valid_count = len(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count

    max_customer = valid_customer_list[0]
    max_amount = valid_amount_list[0]

    min_customer = valid_customer_list[0]
    min_amount = valid_amount_list[0]

    for i in range(valid_count):
        if valid_amount_list[i] > max_amount:
            max_customer = valid_customer_list[i]
            max_amount = valid_amount_list[i]

        if valid_amount_list[i] < min_amount:
            min_customer = valid_customer_list[i]
            min_amount = valid_amount_list[i]

else:
    avg_amount = 0
    max_customer = ""
    max_amount = 0
    min_customer = ""
    min_amount = 0

print("有效客户列表：", valid_customer_list)
print("有效金额列表：", valid_amount_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("总金额：", total_amount)
print("平均金额：", round(avg_amount, 2))
print("最高金额客户：", max_customer)
print("最高金额：", max_amount)
print("最低金额客户：", min_customer)
print("最低金额：", min_amount)