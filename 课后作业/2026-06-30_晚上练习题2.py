refund_text = " 张三:300, 李四:0, 王五:120, , 赵六:800, 错误数据, 钱七:abc, :50, 孙八: "

refund_list = refund_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0
valid_count = 0
avg_amount = 0


big_refund_customer_list = []
normal_refund_customer_list = []
zero_refund_customer_list = []

big_refund_count = 0
normal_refund_count = 0
zero_refund_count = 0

for refund in refund_list:
    clean_refund = refund.strip()

    if clean_refund == "":
        invalid_count += 1
    elif ":" not in clean_refund:
        invalid_count += 1
    else:
        parts = clean_refund.split(":", 1)
        customer = parts[0].strip()
        amount_text_item = parts[1].strip()

        if customer == "" or amount_text_item == "":
            invalid_count += 1
        elif amount_text_item.replace(".", "", 1).isdigit():
            amount = float(amount_text_item)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

            if amount >= 300:
                big_refund_customer_list.append(customer)
                big_refund_count += 1
            elif amount > 0:
                normal_refund_customer_list.append(customer)
                normal_refund_count += 1
            else:
                zero_refund_customer_list.append(customer)
                zero_refund_count += 1
        else:
            invalid_count += 1

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

print("原始退款记录列表: ", refund_list)
print("有效客户列表: ", valid_customer_list)
print("有效退款金额列表: ", valid_amount_list)
print("无效记录数量: ", invalid_count)
print("有效记录数量: ", valid_count)
print("退款总金额: ", total_amount)
print("平均退款金额: ", round(avg_amount, 2))
print("最高退款客户: ", max_customer)
print("最高退款金额: ", max_amount)
print("最低退款客户: ", min_customer)
print("最低退款金额: ", min_amount)
print("大额退款客户列表: ", big_refund_customer_list)
print("大额退款数量: ", big_refund_count)
print("普通退款客户列表: ", normal_refund_customer_list)
print("普通退款数量: ", normal_refund_count)
print("零元退款客户列表: ", zero_refund_customer_list)
print("零元退款数量: ", zero_refund_count)