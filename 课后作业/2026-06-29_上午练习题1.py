#1
# 有效客户列表
# 有效金额列表
# 有效记录数量
# 无效记录数量
# 总金额
# 平均金额，保留 2 位小数
order_text = "张三:100, 李四:abc, 王五:200, , 赵六:, 钱七:0, 孙八:35.5, 周九"
order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0
total_amount = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order == "":
        invalid_count += 1
    elif ":" not in clean_order:
        invalid_count += 1
    else:
        parts = clean_order.split(":", 1)
        customer = parts[0].strip()
        amount_text = parts[1].strip()

        if customer == "" or amount_text == "":
            invalid_count += 1
        elif amount_text.replace(".", "", 1).isdigit():
            amount = float(amount_text)

            valid_customer_list.append(customer)
            valid_amount_list.append(amount)
            total_amount += amount

        else:
            invalid_count += 1

valid_count = len(valid_amount_list)

if valid_count > 0:
    avg_amount = total_amount / valid_count
else:
    avg_amount = 0

print("有效客户列表: ", valid_customer_list)
print("有效金额列表: ", valid_amount_list)
print("有效记录数量: ", valid_count)
print("无效记录数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))

#2
record = "  苹果 : 10  "
clean_record = record.strip()
parts = clean_record.split(":", 1)
product = parts[0].strip()
stock_text = parts[1].strip()
stock = float(stock_text)

print(product)
print(stock_text)
print(stock)

#3 要求输出
# 你要输出每个商品和库存：
product_text = " 苹果 : 10 , 香蕉 : 20 , 梨 : 5 "

product_list = product_text.split(",")

for record in product_list:
    clean_record = record.strip()
    parts = clean_record.split(":", 1)
    product = parts[0].strip()
    stock_text = parts[1].strip()
    stock = float(stock_text)
    print(product, stock)

#第 7 题：循环 + append 保存专项

product_text = " 苹果 : 10 , 香蕉 : 20 , 梨 : 5 "
product_list = product_text.split(",")

valid_product_list = []
valid_stock_list = []

for record in product_list:
    clean_record = record.strip()
    parts = clean_record.split(":", 1)
    product = parts[0].strip()
    stock_text = parts[1].strip()
    stock = float(stock_text)
    valid_product_list.append(product)
    valid_stock_list.append(stock)

print(valid_product_list)
print(valid_stock_list)


#第 8 题：循环 + append + 有效数量统计专项

product_text = " 苹果 : 10 , 香蕉 : 20 , 梨 : 5 "

product_list = product_text.split(",")

valid_product_list = []
valid_stock_list = []

for record in product_list:
    clean_record = record.strip()
    parts = clean_record.split(":", 1)
    product = parts[0].strip()
    stock_text = parts[1].strip()
    stock = float(stock_text)
    valid_product_list.append(product)
    valid_stock_list.append(stock)

valid_count = len(valid_stock_list)

print("有效商品列表：", valid_product_list)
print("有效库存列表：", valid_stock_list)
print("有效商品数量：", valid_count)
