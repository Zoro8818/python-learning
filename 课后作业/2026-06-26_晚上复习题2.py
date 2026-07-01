# 第 1 题：split 核心块复写，5 分钟
# 你只写代码完成：
# 用英文逗号拆成 record_list
# 遍历 record_list
# 每条 strip()
# 保存到 clean_record_list
# 打印两个列表

text = "苹果:120, 香蕉:45, 梨:80, 桃子:30"

clean_record_list = []
record_list = text.split(",")

for record in record_list:
    clean_record = record.strip()
    clean_record_list.append(clean_record)

print(record_list)
print(clean_record_list)

#第 2 题：最高/最低核心块，10-15 分钟
# valid_count
# 最高商品/金额
# 最低商品/金额
# 打印结果

valid_product_list = ["苹果", "香蕉", "梨", "桃子", "芒果"]
valid_amount_list = [120.0, 45.0, 80.0, 30.0, 200.0]

valid_count = len(valid_amount_list)

if valid_count > 0:
    max_product = valid_product_list[0]
    max_amount = valid_amount_list[0]

    min_product = valid_product_list[0]
    min_amount = valid_amount_list[0]

    for i in range(valid_count):
        if valid_amount_list[i] > max_amount:
            max_product = valid_product_list[i]
            max_amount = valid_amount_list[i]

        if valid_amount_list[i] < min_amount:
            min_product = valid_product_list[i]
            min_amount = valid_amount_list[i]

else:
    max_product = ""
    max_amount = 0
    min_product = ""
    min_amount = 0

print("最高商品: ", max_product)
print("最高金额: ", max_amount)
print("最低商品: ", min_product)
print("最低金额: ", min_amount)

#3 输出标签和变量对应

valid_count = 5
invalid_count = 2
total_amount = 475.0
avg_amount = 95.0
max_product = "芒果"
max_amount = 200.0
min_product = "桃子"
min_amount = 30.0

print("有效数据数量: ", valid_count)
print("无效数据数量: ", invalid_count)
print("总金额: ", total_amount)
print("平均金额: ", round(avg_amount, 2))
print("最高商品: ", max_product)
print("最高金额: ", max_amount)
print("最低商品: ", min_product)
print("最低金额: ", min_amount)