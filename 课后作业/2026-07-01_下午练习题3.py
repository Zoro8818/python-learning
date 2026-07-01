consume_text = " 张三:1500, 李四:0, 王五:300, 周十:500, , 赵六:abc, 钱七:800, 错误数据, :200, 孙八: "

consume_list = consume_text.split(",")

over_500_customer_list = []
over_500_amount_list = []
over_500_count = 0

for record in consume_list:
    clean_record = record.strip()

    if clean_record == "":
        continue
    elif ":" not in clean_record:
        continue
    else:
        parts = clean_record.split(":", 1)
        customer = parts[0].strip()
        amount_text_item = parts[1].strip()

        if customer == "" or amount_text_item == "":
            continue
        elif amount_text_item.replace(".", "", 1).isdigit():
            amount = float(amount_text_item)

            if amount >= 500:
                over_500_customer_list.append(customer)
                over_500_amount_list.append(amount)
                over_500_count += 1

        else:
            continue
print("消费金额 500 及以上的会员名单: ", over_500_customer_list)
print("对应消费金额列表: ", over_500_amount_list)
print("符合条件人数: ", over_500_count)