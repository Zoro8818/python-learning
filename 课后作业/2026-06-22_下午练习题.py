# 要求输出：
# 原始客户记录列表
# 有效客户名单
# 有效消费金额列表
# 有效记录数量
# 无效记录数量
# 高价值客户列表，消费金额 >= 200
# 高价值客户数量
# 普通客户数量，消费金额 < 200
# 消费总金额
# 平均消费金额，保留 2 位小数
customer_text = " 张三:120, 李四: , 王五:300, 赵六:abc, 钱七:80, 孙八:0, 周九:200, , 吴十:500 "
record_list = customer_text.split(",")

valid_names = []
valid_amounts = []
high_value_customers = []

invalid_count = 0
normal_count = 0
total_amount = 0

for record in record_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1

    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":")
        name = parts[0].strip()
        amount_text = parts[1].strip()

        if name == "" or amount_text == "":
            invalid_count += 1

        elif amount_text.replace(".", "",1).isdigit():  #-->判断金额文本是不是数字或小数
            amount = float(amount_text)

            valid_names.append(name)
            valid_amounts.append(amount)
            total_amount += amount

            if amount >= 200:
                high_value_customers.append(name)
            else:
                normal_count += 1

        else:
            invalid_count += 1

avg_amount = total_amount / len(valid_amounts)

print("原始客户记录列表:", record_list)
print("有效客户名单:", valid_names)
print("有效消费金额列表:", valid_amounts)
print("有效记录数量:", len(valid_amounts))
print("无效记录数量:", invalid_count)
print("高价值客户列表:", high_value_customers)
print("高价值客户数量:", len(high_value_customers))
print("普通客户数量:", normal_count)
print("消费总金额:", total_amount)
print("平均消费金额:", round(avg_amount, 2))

#注释:输入customer_text
#过程:split 成原始列表,for 遍历, strip去空格,if 判断是否为空记录, 是空数据 invalid_count += 1,elif 判断":"是否在数据里,不在 invalid_count += 1
#否则:split以冒号拆分去前后空格,strip()去空格.
#if判断 name or amount_text 是否有空记录,有 invalid_count += 1
#判断 amount_text 是不是一个数字或小数。(把金额里的一个小数点先拿掉，再看看剩下的是不是全是数字。判断是否为数字)
#成功name append 进valid_names, amount append 进valid_amounts.total_amount += amount
#否则invalid_count += 1
#判断amount >= 200,append 进high_value_customers,否则normal_count += 1 平均值 = total_amount / len(valid_amounts)
#保存:valid_names, valid_amounts, high_value_customers, invalid_count, normal_count, total_amount, avg_amount
#输出:record_list, valid_names, valid_amounts, len(valid_amounts), invalid_count, high_value_customers, len(high_value_customers)
#, normal_count, total_amount, round(avg_amount, 2)












