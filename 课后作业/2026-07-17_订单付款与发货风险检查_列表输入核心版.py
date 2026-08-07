# 业务目标：检查订单付款与发货状态，隔离无效记录并识别履约风险。
# 输入字段：订单编号、客户名称、订单金额、付款状态、发货状态。
# 处理链：字段校验 -> 金额转换 -> 有效保存 -> 状态组合分类 -> 金额统计。
# 分类口径：已付款已发货为正常完成；已付款未发货为待发货；
#           未付款未发货为待付款；未付款已发货为风险订单。
# 本版本使用代码内置列表，只验证核心业务处理逻辑，不负责文件读写。

raw_record_list = [
    "SO001,华东商贸,1200.5,已付款,已发货",
    "SO002,蓝海科技,850,已付款,未发货",
    "SO003,远航公司,600,未付款,未发货",
    "SO004,晨光门店,300,未付款,已发货",
    "SO005,华南客户,abc,已付款,已发货",
    "SO006,,500,已付款,未发货",
    "SO007,星河公司,700,付款中,未发货",
    "SO008,万盛公司,900,已付款"
]

order_number_list = []          # 有效订单编号列表
customer_name_list = []         # 有效客户名称列表
order_amount_list = []          # 有效订单金额列表
payment_status_list = []        # 有效付款状态列表
shipping_status_list = []       # 有效发货状态列表

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

print("\n最终业务结论：", business_conclusion)
