# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/customer_orders.csv"
cleaned_file = "D:/python-project/课后作业/output/customer_orders_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/customer_orders_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "客户姓名,订单状态,订单金额":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_customer_name_list = []
valid_order_status_list = []
valid_order_amount_list = []

invalid_count = 0
total_order_amount = 0
large_order_count = 0
normal_order_count = 0
zero_order_count = 0


# 第 6 块：循环处理每一条客户记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        customer_name = parts[0].strip()
        order_status = parts[1].strip()
        order_amount_text = parts[2].strip()

        if customer_name == "" or order_amount_text == "":
            invalid_count += 1
        elif order_amount_text.replace(".", "", 1).isdigit():
            order_amount = float(order_amount_text)

            valid_customer_name_list.append(customer_name)
            valid_order_status_list.append(order_status)
            valid_order_amount_list.append(order_amount)
            total_order_amount += order_amount

            if order_amount >= 1000:
                large_order_count += 1
            elif order_amount > 0:
                normal_order_count += 1
            else:
                zero_order_count += 1
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均金额
raw_count = len(raw_record_list)
valid_count = len(valid_order_amount_list)

if valid_count > 0:
    avg_order_amount = total_order_amount / valid_count

else:
    avg_order_amount = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("客户姓名,订单状态,订单金额\n")

    for i in range(valid_count):
        f.write(
            valid_customer_name_list[i]
            + ","
            + valid_order_status_list[i]
            + ","
            + str(valid_order_amount_list[i])
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("客户订单金额清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总订单金额：" + str(total_order_amount) + "\n")
    f.write("平均订单金额：" + str(round(avg_order_amount, 2)) + "\n")
    f.write("大额订单数量：" + str(large_order_count) + "\n")
    f.write("普通订单数量：" + str(normal_order_count) + "\n")
    f.write("零元订单数量：" + str(zero_order_count) + "\n")
