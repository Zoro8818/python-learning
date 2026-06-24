#1
# 有效客户数量
# 有效订单数量
# 无效记录数量
# 大额订单数量（订单金额 >= 500）
# 普通订单数量（订单金额 > 0 且 < 500）
# 零元订单数量（订单金额 == 0）
# 订单总金额
# 平均订单金额

records = [
    "张三:199.9",
    "李四: 88 ",
    "",
    "王五:abc",
    "赵六:",
    " :300",
    "孙七:1200.5",
    "周八:0",
    "吴九:600",
    "郑十:49.9",
]

valid_customer_list = []
valid_amount_list = []

invalid_count = 0
large_count = 0
normal_count = 0
zero_count = 0
total_amount = 0

for record in records:
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
                large_count += 1

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
print("无效记录数量:", invalid_count)
print("大额订单数量:", large_count)
print("普通订单数量:", normal_count)
print("零元订单数量:", zero_count)
print("订单总金额:", total_amount)
print("平均订单金额:", round(avg_amount, 2))


#2.要求输出：
# 有效商品数量
# 有效销售额数量
# 无效记录数量
# 高销售额商品数量（销售额 >= 500）
# 普通销售额商品数量（销售额 > 0 且 < 500）
# 零销售额商品数量（销售额 == 0）
# 销售总额
# 平均销售额

records = [
    "鼠标:99.9",
    "键盘: 299 ",
    "",
    "显示器:1299",
    "耳机:abc",
    " :88",
    "U盘:",
    "硬盘:599.5",
    "数据线:0",
    "摄像头:450",
]

valid_product_list = []
valid_sales_list = []

invalid_count = 0
large_count = 0
normal_count = 0
zero_count = 0
total_sales = 0

for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        sales_text = parts[1].strip()

        if product == "" or sales_text == "":
            invalid_count += 1

        elif sales_text.replace(".", "", 1).isdigit():
            sales = float(sales_text)

            valid_product_list.append(product)
            valid_sales_list.append(sales)
            total_sales += sales

            if sales >= 500:
                large_count += 1

            elif sales > 0:
                normal_count += 1

            else:
                zero_count += 1

        else:
            invalid_count += 1

if len(valid_sales_list) > 0:
    avg_sales = total_sales / len(valid_sales_list)

else:
    avg_sales = 0

print("有效商品数量:", len(valid_product_list))
print("有效销售额数量:", len(valid_sales_list))
print("无效记录数量:", invalid_count)
print("高销售额商品数量:", large_count)
print("普通销售额商品数量:", normal_count)
print("零销售额商品数量:", zero_count)
print("销售总额:", total_sales)
print("平均销售额:", round(avg_sales, 2))



