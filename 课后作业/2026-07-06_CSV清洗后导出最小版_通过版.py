# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/customers.csv"
cleaned_file = "D:/python-project/课后作业/output/customers_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/customers_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="gbk") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "客户名称,手机号,金额":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_customer_list = []
valid_phone_list = []
valid_amount_list = []

invalid_count = 0
total_amount = 0


# 第 6 块：循环处理每一条客户记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        customer = parts[0].strip()
        phone = parts[1].strip()
        amount_text = parts[2].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_customer_list.append(customer)
            valid_phone_list.append(phone)
            valid_amount_list.append(amount)
            total_amount += amount
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均金额
raw_count = len(raw_record_list)
valid_count = len(valid_customer_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count

else:
    avg_amount = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("客户名称,手机号,金额\n")

    for i in range(valid_count):
        f.write(
            valid_customer_list[i]
            + ","
            + valid_phone_list[i]
            + ","
            + str(valid_amount_list[i])
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("客户金额清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("金额总和：" + str(total_amount) + "\n")
    f.write("平均金额：" + str(round(avg_amount, 2)) + "\n")
