# 订单回款差额清洗、分类、统计及文件输出
# Order Payment Difference Cleaning, Classification, Statistics, and File Output
# 业务字段：客户名称（customer_name）、应收金额（receivable_amount）、实收金额（received_amount）、差额（difference_amount）

input_file_path = r"D:\python-project\课后作业\input\order_payment.csv"
cleaned_file_path = r"D:\python-project\课后作业\output\order_payment_cleaned.csv"
report_file_path = r"D:\python-project\课后作业\output\order_payment_report.txt"


raw_record_list = []

invalid_record_list = []
invalid_reason_list = []
customer_name_list = []
receivable_amount_list = []
received_amount_list = []
difference_amount_list = []

cleaned_record_list = []

overpaid_customer_list = []
settled_customer_list = []
outstanding_customer_list = []

total_receivable_amount = 0
total_received_amount = 0
total_difference_amount = 0

highest_difference_amount = 0
highest_difference_customer = ""

lowest_difference_amount = 0
lowest_difference_customer = ""

# 第1块：读取 CSV 文件（Read CSV File）

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

# 第2块：第一个循环，清理文件行（First Loop: Clean File Lines）
# 任务：
# 1. 遍历 lines
# 2. strip() 清洗每一行
# 3. 排除空行
# 4. 排除表头
# 5. 保存到 raw_record_list

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "客户名称,应收金额,实收金额":
        raw_record_list.append(clean_line)


# 第3块：第二个循环，校验并处理业务记录（Second Loop: Validate and Process Business Records）
# 字段对应：
# parts[0] → 客户名称
# parts[1] → 应收金额文字
# parts[2] → 实收金额文字
#
# 任务顺序：
# 1. record.split(",")
# 2. 先判断字段数量是否等于 3
# 3. 清洗三个字段
# 4. 判断字段是否为空
# 5. 判断两个金额是不是合法数字
# 6. 保存无效记录和无效原因
# 7. 合法金额转 float 并计算差额（Convert Valid Amounts to float and Calculate Difference）
# 8. 保存有效数据、累加金额、同步最大最小（Save Valid Data, Accumulate Amounts, and Sync Max/Min）
# 9. 按多收、已结清、待收分类（Classify as Overpaid, Settled, or Outstanding）

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录：" + record)
    else:
        customer_name = parts[0].strip()
        receivable_amount_text = parts[1].strip()
        received_amount_text = parts[2].strip()

        if customer_name == "" or receivable_amount_text == "" or received_amount_text == "":
            invalid_record_list.append(record)
            invalid_reason_list.append("字段为空，原始记录：" + record)
        elif (
            not receivable_amount_text.replace(".", "", 1).isdigit()
            or not received_amount_text.replace(".", "", 1).isdigit()
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("金额不是数字，原始记录：" + record)
        else:
            # 7. 两个金额都合法后，转换为 float 并计算回款差额。
            receivable_amount = float(receivable_amount_text)
            received_amount = float(received_amount_text)
            difference_amount = received_amount - receivable_amount

            # 8. 保存有效数据，累加金额，并让客户名称与最大/最小差额保持同步。
            customer_name_list.append(customer_name)
            receivable_amount_list.append(receivable_amount)
            received_amount_list.append(received_amount)
            difference_amount_list.append(difference_amount)

            if len(difference_amount_list) == 1:
                highest_difference_amount = difference_amount
                highest_difference_customer = customer_name

                lowest_difference_amount = difference_amount
                lowest_difference_customer = customer_name

            else:
                if difference_amount > highest_difference_amount:
                    highest_difference_amount = difference_amount
                    highest_difference_customer = customer_name

                if difference_amount < lowest_difference_amount:
                    lowest_difference_amount = difference_amount
                    lowest_difference_customer = customer_name

            total_receivable_amount += receivable_amount
            total_received_amount += received_amount
            total_difference_amount += difference_amount

            cleaned_record_list.append(
                customer_name
                + ","
                + str(receivable_amount)
                + ","
                + str(received_amount)
                + ","
                + str(difference_amount)
            )

            # 9. 根据差额分类：多收（overpaid）、已结清（settled）、待收（outstanding）。
            if difference_amount > 0:
                overpaid_customer_list.append(customer_name)
            elif difference_amount == 0:
                settled_customer_list.append(customer_name)
            else:
                outstanding_customer_list.append(customer_name)

# 第4块：控制台检查输出（Console Check Output）

print("原始业务记录数量：", len(raw_record_list))
print("无效记录数量：", len(invalid_record_list))

print("\n无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print("\n无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print("\n有效记录数量：", len(cleaned_record_list))
print("多收客户数量：", len(overpaid_customer_list))
print("已结清客户数量：", len(settled_customer_list))
print("待收客户数量：", len(outstanding_customer_list))

print("\n清洗后的有效记录：")
for cleaned_record in cleaned_record_list:
    print(cleaned_record)

print("\n多收客户：", overpaid_customer_list)
print("已结清客户：", settled_customer_list)
print("待收客户：", outstanding_customer_list)

print("\n应收金额合计：", total_receivable_amount)
print("实收金额合计：", total_received_amount)
print("差额合计：", total_difference_amount)

if len(cleaned_record_list) == 0:
    print("\n没有有效数据，无法计算最大和最小差额")

else:
    print("\n最大差额客户：", highest_difference_customer)
    print("最大差额金额：", highest_difference_amount)

    print("最小差额客户：", lowest_difference_customer)
    print("最小差额金额：", lowest_difference_amount)

# 第5块：生成最终业务结论（Generate Final Business Conclusion）

if len(invalid_record_list) > 0:
    business_conclusion = "存在无效数据，当前回款统计仅供参考，需要修正后重新核算"

elif len(cleaned_record_list) == 0:
    business_conclusion = "没有有效数据，无法进行回款核算"

elif total_difference_amount > 0:
    business_conclusion = "有效订单整体存在多收款项"

elif total_difference_amount == 0:
    business_conclusion = "有效订单应收与实收整体一致"

else:
    business_conclusion = "有效订单整体仍有待收款项"

# 第6块：输出清洗后的 CSV（Write Cleaned CSV）

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("客户名称,应收金额,实收金额,差额\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")


# 第7块：输出 TXT 统计报告（Write TXT Statistical Report）

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("订单回款差额清洗与分类报告\n")
    file.write("==============================\n")

    file.write("原始业务记录数量：" + str(len(raw_record_list)) + "\n")
    file.write("有效记录数量：" + str(len(cleaned_record_list)) + "\n")
    file.write("无效记录数量：" + str(len(invalid_record_list)) + "\n")

    file.write("\n分类统计\n")
    file.write("------------------------------\n")
    file.write("多收客户数量：" + str(len(overpaid_customer_list)) + "\n")
    file.write("已结清客户数量：" + str(len(settled_customer_list)) + "\n")
    file.write("待收客户数量：" + str(len(outstanding_customer_list)) + "\n")

    file.write("\n金额统计\n")
    file.write("------------------------------\n")
    file.write("应收金额合计：" + str(total_receivable_amount) + "\n")
    file.write("实收金额合计：" + str(total_received_amount) + "\n")
    file.write("差额合计：" + str(total_difference_amount) + "\n")

    file.write("\n最大和最小差额\n")
    file.write("------------------------------\n")

    if len(cleaned_record_list) == 0:
        file.write("没有有效数据，无法计算最大和最小差额\n")

    else:
        file.write(
            "最大差额客户："
            + highest_difference_customer
            + "，差额："
            + str(highest_difference_amount)
            + "\n"
        )

        file.write(
            "最小差额客户："
            + lowest_difference_customer
            + "，差额："
            + str(lowest_difference_amount)
            + "\n"
        )

    file.write("\n客户分类明细\n")
    file.write("------------------------------\n")
    file.write("多收客户：" + str(overpaid_customer_list) + "\n")
    file.write("已结清客户：" + str(settled_customer_list) + "\n")
    file.write("待收客户：" + str(outstanding_customer_list) + "\n")

    file.write("\n无效数据明细\n")
    file.write("------------------------------\n")

    if len(invalid_reason_list) == 0:
        file.write("无\n")
    else:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")

    file.write("\n最终业务结论\n")
    file.write("------------------------------\n")
    file.write(business_conclusion + "\n")


print("\ncleaned CSV 已生成：", cleaned_file_path)
print("TXT 报告已生成：", report_file_path)
print("最终业务结论：", business_conclusion)
