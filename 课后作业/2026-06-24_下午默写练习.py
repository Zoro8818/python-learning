#1.
print("名单清洗")
names = [
    " 张三 ",
    "",
    "李四",
    "   ",
    "王五",
    "赵六 ",
    " 钱七"
]

valid_names_list = []
invalid_name_count = 0

for name in names:
    clean_name = name.strip()

    if clean_name == "":
        invalid_name_count += 1

    else:
        valid_names_list.append(clean_name)

print("有效客户数量:", len(valid_names_list))
print("有效客户名单:", valid_names_list)

#2.
print("订单金额统计")
orders = [
    "张三: 120.5",
    "李四:80",
    "王五:",
    " :200",
    "赵六:abc",
    "",
    "钱七: 300",
    "孙八:50"
]
valid_amount = []

invalid_order_count = 0
total_amount = 0
big_count = 0
medium_count = 0
small_count = 0

for order in orders:
    clean_order = order.strip()

    if clean_order == "":
        invalid_order_count += 1
    elif ":" not in clean_order:
        invalid_order_count += 1

    else:
        parts = clean_order.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_order_count += 1

        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_amount.append(amount)
            total_amount += amount

            if amount >= 200:
                big_count += 1
            elif amount >= 100:
                medium_count += 1

            else:
                small_count += 1

        else:
            invalid_order_count += 1

if len(valid_amount) > 0:
    avg_amount = total_amount / len(valid_amount)

else:
    avg_amount = 0

print("有效订单数量:", len(valid_amount))
print("无效订单数量:", invalid_order_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))
print("大订单数量:", big_count)
print("中订单数量:", medium_count)
print("小订单数量:", small_count)
