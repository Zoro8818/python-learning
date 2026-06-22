# 要求输出：
# 原始商品记录列表
# 有效商品名列表
# 有效价格列表
# 有效记录数量
# 无效记录数量
# 高价商品列表，价格 >= 10
# 高价商品数量
# 普通商品数量
# 总价格
# 平均价格，保留 2 位小数
# 要求还是一样：先判空，再判冒号，再拆分，再判金额，再 float()。
product_text = " 苹果:5.5, 牛奶:8, 面包: , 鸡蛋:abc, 香蕉:3.2, 大米:45, , 可乐:6 "
product_list = product_text.split(",")

valid_product_list = []
valid_price_list = []
large_product_list = []

normal_count = 0
total_price = 0
invalid_count = 0

for product in product_list:
    clean_product = product.strip()

    if clean_product == "":
        invalid_count += 1

    elif ":" not in clean_product:
        invalid_count += 1

    else:
        parts = clean_product.split(":", 1)

        product_name = parts[0].strip()
        amount_text = parts[1].strip()

        if product_name == "" or amount_text == "":
            invalid_count += 1

        elif amount_text.replace(".", "", 1).isdigit():
            price = float(amount_text)

            valid_product_list.append(product_name)
            valid_price_list.append(price)
            total_price += price

            if price >= 10:
                large_product_list.append(product_name)
            else:
                normal_count += 1

        else:
            invalid_count += 1

if len(valid_price_list) > 0:
    avg_price = total_price / len(valid_price_list)
else:
    avg_price = 0


print("原始商品记录列表:", product_list)
print("有效商品名列表:", valid_product_list)
print("有效价格列表:", valid_price_list)
print("有效记录数量:", len(valid_price_list))
print("无效记录数量:", invalid_count)
print("高价商品列表:", large_product_list)
print("高价商品数量:", len(large_product_list))
print("普通商品数量:", normal_count)
print("商品总价格:", total_price)
print("平均价:", round(avg_price, 2))








