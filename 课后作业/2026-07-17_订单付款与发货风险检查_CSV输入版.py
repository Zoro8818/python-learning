# 业务目标：从 CSV 批量检查订单付款与发货状态，输出清洗结果和风险报告。
# 输入字段：订单编号、客户名称、订单金额、付款状态、发货状态。
# 处理链：读取 CSV -> 清洗校验 -> 无效隔离 -> 状态组合分类 -> 金额统计。
# 分类口径：已付款已发货为正常完成；已付款未发货为待发货；
#           未付款未发货为待付款；未付款已发货为风险订单。
# 输出结果：有效订单 cleaned CSV、分类统计、最高最低金额和 TXT 报告。

input_file_path = (
    r"D:\python-project\课后作业\input\order_payment_shipping.csv"
)

cleaned_file_path = (
    r"D:\python-project\课后作业\output\order_payment_shipping_cleaned.csv"
)

report_file_path = (
    r"D:\python-project\课后作业\output\order_payment_shipping_report.txt"
)

raw_record_list = []

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "订单编号,客户名称,订单金额,付款状态,发货状态"
    ):
        raw_record_list.append(clean_line)


order_number_list = []          # 有效订单编号列表
customer_name_list = []         # 有效客户名称列表
order_amount_list = []          # 有效订单金额列表
payment_status_list = []        # 有效付款状态列表
shipping_status_list = []       # 有效发货状态列表
cleaned_record_list = []        # 清洗后的有效订单记录列表

invalid_record_list = []        # 无效原始记录列表
invalid_reason_list = []        # 无效原因列表

normal_completed_order_list = []   # 正常完成订单列表
pending_shipment_order_list = []   # 待发货订单列表
pending_payment_order_list = []    # 待付款订单列表
risk_order_list = []               # 风险订单列表

total_order_amount = 0

highest_order_amount = 0
highest_amount_order = ""

lowest_order_amount = 0
lowest_amount_order = ""

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 5:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录：" + record)

    else:
        order_number = parts[0].strip()
        customer_name = parts[1].strip()
        order_amount_text = parts[2].strip()
        payment_status = parts[3].strip()
        shipping_status = parts[4].strip()

        if (
            order_number == ""
            or customer_name == ""
            or order_amount_text == ""
            or payment_status == ""
            or shipping_status == ""
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("字段为空，原始记录：" + record)

        elif not order_amount_text.replace(".", "", 1).isdigit():
            invalid_record_list.append(record)
            invalid_reason_list.append("订单金额不是数字，原始记录：" + record)

        elif payment_status != "已付款" and payment_status != "未付款":
            invalid_record_list.append(record)
            invalid_reason_list.append("付款状态不合法, 原始记录: " + record)

        elif shipping_status != "已发货" and shipping_status != "未发货":
            invalid_record_list.append(record)
            invalid_reason_list.append("发货状态不合法, 原始记录: " + record)

        else:
            order_amount = float(order_amount_text)

            order_number_list.append(order_number)
            customer_name_list.append(customer_name)
            order_amount_list.append(order_amount)
            payment_status_list.append(payment_status)
            shipping_status_list.append(shipping_status)

            cleaned_record_list.append(
                order_number
                + ","
                + customer_name
                + ","
                + str(order_amount)
                + ","
                + payment_status
                + ","
                + shipping_status
            )

            total_order_amount += order_amount

            if len(order_amount_list) == 1:
                highest_order_amount = order_amount
                highest_amount_order = order_number

                lowest_order_amount = order_amount
                lowest_amount_order = order_number

            else:
                if order_amount > highest_order_amount:
                    highest_order_amount = order_amount
                    highest_amount_order = order_number

                if order_amount < lowest_order_amount:
                    lowest_order_amount = order_amount
                    lowest_amount_order = order_number

            if payment_status == "已付款" and shipping_status == "已发货":
                normal_completed_order_list.append(order_number)

            elif payment_status == "已付款" and shipping_status == "未发货":
                pending_shipment_order_list.append(order_number)

            elif payment_status == "未付款" and shipping_status == "未发货":
                pending_payment_order_list.append(order_number)

            else:
                risk_order_list.append(order_number)

print("原始订单数量：", len(raw_record_list))
print("有效订单数量：", len(order_number_list))
print("无效订单数量：", len(invalid_record_list))

print("\n无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print("\n无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print("\n正常完成订单：", normal_completed_order_list)
print("待发货订单：", pending_shipment_order_list)
print("待付款订单：", pending_payment_order_list)
print("风险订单：", risk_order_list)

print("\n有效订单金额合计：", total_order_amount)

if len(order_amount_list) == 0:
    print("\n没有有效订单，无法计算最高和最低订单金额")
else:
    print("\n最高金额订单：", highest_amount_order)
    print("最高订单金额：", highest_order_amount)

    print("最低金额订单：", lowest_amount_order)
    print("最低订单金额：", lowest_order_amount)

if len(invalid_record_list) > 0:
    business_conclusion = "存在无效订单数据，需要修正后重新检查"

elif len(order_number_list) == 0:
    business_conclusion = "没有有效订单，无法进行订单风险分析"

elif len(risk_order_list) > 0:
    business_conclusion = "存在未付款已发货的风险订单，需要优先处理"

elif (
    len(pending_shipment_order_list) > 0
    or len(pending_payment_order_list) > 0
):
    business_conclusion = "存在待发货或待付款订单，需要继续跟进"

else:
    business_conclusion = "有效订单均已付款并完成发货"

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("订单编号,客户名称,订单金额,付款状态,发货状态\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("订单付款与发货风险检查报告\n")
    file.write("==============================\n")

    file.write("原始订单数量：" + str(len(raw_record_list)) + "\n")
    file.write("有效订单数量：" + str(len(order_number_list)) + "\n")
    file.write("无效订单数量：" + str(len(invalid_record_list)) + "\n")

    file.write("\n订单分类统计\n")
    file.write("------------------------------\n")
    file.write(
        "正常完成订单数量："
        + str(len(normal_completed_order_list))
        + "\n"
    )
    file.write(
        "待发货订单数量："
        + str(len(pending_shipment_order_list))
        + "\n"
    )
    file.write(
        "待付款订单数量："
        + str(len(pending_payment_order_list))
        + "\n"
    )
    file.write(
        "风险订单数量："
        + str(len(risk_order_list))
        + "\n"
    )

    file.write("\n订单金额统计\n")
    file.write("------------------------------\n")
    file.write("有效订单金额合计：" + str(total_order_amount) + "\n")

    file.write("\n最高和最低订单金额\n")
    file.write("------------------------------\n")

    if len(order_amount_list) == 0:
        file.write("没有有效订单，无法计算最高和最低订单金额\n")

    else:
        file.write(
            "最高金额订单："
            + highest_amount_order
            + "，金额："
            + str(highest_order_amount)
            + "\n"
        )

        file.write(
            "最低金额订单："
            + lowest_amount_order
            + "，金额："
            + str(lowest_order_amount)
            + "\n"
        )

    file.write("\n订单分类明细\n")
    file.write("------------------------------\n")
    file.write(
        "正常完成订单："
        + str(normal_completed_order_list)
        + "\n"
    )
    file.write(
        "待发货订单："
        + str(pending_shipment_order_list)
        + "\n"
    )
    file.write(
        "待付款订单："
        + str(pending_payment_order_list)
        + "\n"
    )
    file.write(
        "风险订单："
        + str(risk_order_list)
        + "\n"
    )

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
