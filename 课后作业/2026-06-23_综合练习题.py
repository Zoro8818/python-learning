# 第一组：报名名单
# 有效学生数量
# 无效学生数量
# 有效学生名单
student_records = [
    " 张三 ",
    "",
    "李四",
    "   ",
    "王五",
    "赵六",
    "",
]

valid_student_list = []
invalid_count = 0

for record in student_records:
    clean_record = record.strip()

    if clean_record != "":
        valid_student_list.append(clean_record)
    else:
        invalid_count += 1

print("有效学生数量:", len(valid_student_list))
print("无效学生数量:", invalid_count)
print("有效学生名单:", valid_student_list)



#第二组：订单金额
# 有效客户数量
# 有效订单数量
# 无效订单记录数量
# 大额订单数量（金额 >= 500）
# 普通订单数量（金额 > 0 且 < 500）
# 零元订单数量（金额 == 0）
# 订单总金额
# 平均订单金额

order_records = [
    "张三:199.9",
    "李四: 0 ",
    "",
    "王五:abc",
    "赵六:800",
    " :300",
    "孙七:1200.5",
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