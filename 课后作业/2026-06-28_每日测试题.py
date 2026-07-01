# 题目 1：
# 完成标准：
# name 得到干净的姓名
# amount_text 得到干净的金额文本
# 能说明 split(",") 负责拆记录，strip() 负责清洗字段，不混用到整行列表上

record = "  张三,98.5,合格  "

clean_record = record.strip()

parts = clean_record.split(",")
name = parts[0].strip()
amount_text = parts[1].strip()

print("姓名:", name)
print("金额文本:", amount_text)

#注释: split(",") 负责拆字段, strip() 负责清洗前后空格

#题目 2：
# 下面这段判断里，哪一种输入会被当作“合法金额文本”？
# 请分别判断这 4 个值："12.5"、"12.5.3"、" 12.5 "、"abc"
# 完成标准：
# 能明确指出哪些能过、哪些不能过
# 能说明这是“字符串格式检查”，不是数值运算
# 如果提到空格问题，要说明先 strip() 再判断

amount_text = amount_text.strip()

if amount_text.replace(".", "", 1).isdigit():
    amount = float(amount_text)

#注释: 能过:"12.5". 不能过"12.5.3"、"abc". " 12.5 "如果去空格能过

#题目 3：
# 你已经有两个列表：
# 请说出如何同步找出最高金额对应的人，以及最低金额对应的人。
names = ["A", "B", "C"]
amounts = [10.0, 25.0, 18.0]

max_names = names[0]
max_amounts = amounts[0]

min_names = names[0]
min_amounts = amounts[0]

for i in range(len(amounts)):
    if amounts[i] > max_amounts:
        max_names = names[i]
        max_amounts = amounts[i]

    if amounts[i] < min_amounts:
        min_names = names[i]
        min_amounts = amounts[i]

# 题目 4：
# 有一个文件读取任务，要求把整个文本读出来后再逐行处理。请写出读取和输出的关键骨架：
order_text = " 张三:120.5, 李四:abc, , 王五:300, 赵六, 钱七: , 孙八:80 "

order_list = order_text.split(",")

valid_customer_list = []
valid_amount_list = []
invalid_count = 0

for record in order_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
        continue

    if ":" not in clean_record:
        invalid_count += 1
        continue

    parts = clean_record.split(":", 1)
    customer = parts[0].strip()
    amount_text = parts[1].strip()

    if customer == "" or amount_text == "":
        invalid_count += 1
        continue

    if amount_text.replace(".", "", 1).isdigit() == False:
        invalid_count += 1
        continue

    amount = float(amount_text)
    valid_customer_list.append(customer)
    valid_amount_list.append(amount)

print(valid_customer_list)
print(valid_amount_list)
print(invalid_count)

#注释: 读取关键骨架:f.read()
# 输出关键骨架:f.write()
# 读取后要拆行,清洗,不能直接遍历



