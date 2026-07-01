#1
# 要求输出：
#
# 原始退款记录列表
# 有效客户列表
# 有效退款金额列表
# 有效记录数量
# 无效记录数量
# 总退款金额
# 平均退款金额，保留 2 位小数
#
# 判断规则：
#
# 空记录：无效
# 缺冒号：无效
# 客户名为空：无效
# 金额为空：无效
# 金额不是合法数字：无效
# 0 是合法金额，不要当成无效

refund_text = " 张三:30.5, 李四:abc, , 王五:0, :50, 赵六, 钱七: 88.8 , 孙八: "

refund_list = refund_text.split(",")

valid_customer_list = []
valid_refund_amount_list = []
invalid_count = 0
total_refund_amount = 0

for record in refund_list:
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
            valid_refund_amount_list.append(amount)
            total_refund_amount += amount

        else:
            invalid_count += 1

valid_count = len(valid_refund_amount_list)

if valid_count > 0:
    avg_refund_amount = total_refund_amount / valid_count
else:
    avg_refund_amount = 0

print("原始退款记录列表: ", refund_list)
print("有效客户列表: ", valid_customer_list)
print("有效退款金额列表: ", valid_refund_amount_list)
print("有效记录数量: ", valid_count)
print("无效记录数量: ", invalid_count)
print("总退款金额: ", total_refund_amount)
print("平均退款金额: ", round(avg_refund_amount, 2))



