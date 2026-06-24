#第一题：外卖订单金额统计
# 1：外卖订单金额
# 要求输出：
# 有效客户数量
# 有效订单数量
# 无效订单记录数量
# 大额订单数量（金额 >= 200）
# 普通订单数量（金额 > 0 且 < 200）
# 零元订单数量（金额 == 0）
# 订单总金额
# 平均订单金额
print("第一题：外卖订单金额统计")
order_records = [
    "张三:56.5",
    "李四: 0 ",
    "",
    "王五:abc",
    "赵六:220",
    " :88",
    "孙七:399.9",
    "周八:",
    "吴九:18",
]

valid_customer_list = []
valid_amount_list = []

invalid_count = 0
high_count = 0
normal_count = 0
zero_count = 0
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

            if amount >= 200:
                high_count += 1
            elif amount > 0:
                normal_count += 1
            else:
                zero_count += 1

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

else:
    avg_amount = 0

print("有效客户数量:", len(valid_customer_list))
print("有效订单数量:", len(valid_amount_list))
print("无效订单记录数量:", invalid_count)
print("大额订单数量:", high_count)
print("普通订单数量:", normal_count)
print("零元订单数量:", zero_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))


# 2：网店订单金额统计
# 2：网店订单金额
# 要求输出：
# 有效客户数量
# 有效订单数量
# 无效订单记录数量
# 大额订单数量（金额 >= 500）
# 普通订单数量（金额 > 0 且 < 500）
# 零元订单数量（金额 == 0）
# 订单总金额
# 平均订单金额
print("第二题：网店订单金额统计")
order_records = [
    "客户A:499.9",
    "客户B:500",
    "客户C:0",
    "",
    "客户D:abc",
    " :300",
    "客户E:1200",
    "客户F:",
    "客户G:88.8",
]

valid_customer_list = []
valid_amount_list = []

invalid_count = 0
high_count = 0
normal_count = 0
zero_count = 0
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

            if amount >= 500:
                high_count += 1
            elif amount > 0:
                normal_count += 1
            else:
                zero_count += 1

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

else:
    avg_amount = 0

print("有效客户数量:", len(valid_customer_list))
print("有效订单数量:", len(valid_amount_list))
print("无效订单记录数量:", invalid_count)
print("大额订单数量:", high_count)
print("普通订单数量:", normal_count)
print("零元订单数量:", zero_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))


# 第三题：课程报名订单金额
# 要求输出：
# 有效客户名单
# 有效订单金额列表
# 有效客户数量
# 有效订单数量
# 无效订单记录数量
# 大额订单数量（金额 >= 1000）
# 普通订单数量（金额 > 0 且 < 1000）
# 零元订单数量（金额 == 0）
# 订单总金额
# 平均订单金额
print("第三题课程报名订单金额统计")
order_records = [
    "张同学:980",
    "李同学: 1500 ",
    "",
    "王同学:free",
    "赵同学:0",
    " :600",
    "孙同学:2500.5",
    "周同学:",
    "吴同学:300",
]

valid_customer_list = []
valid_amount_list = []

invalid_count = 0
high_count = 0
normal_count = 0
zero_count = 0
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

            if amount >= 1000:
                high_count += 1
            elif amount > 0:
                normal_count += 1
            else:
                zero_count += 1

        else:
            invalid_count += 1

if len(valid_amount_list) > 0:
    avg_amount = total_amount / len(valid_amount_list)

else:
    avg_amount = 0

print("有效客户名单:", valid_customer_list)
print("有效订单金额列表:", valid_amount_list)
print("有效客户数量:", len(valid_customer_list))
print("有效订单数量:", len(valid_amount_list))
print("无效订单记录数量:", invalid_count)
print("大额订单数量:", high_count)
print("普通订单数量:", normal_count)
print("零元订单数量:", zero_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))

