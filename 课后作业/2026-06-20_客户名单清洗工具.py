#1.要求：
# 把字符串按英文逗号 , 拆成列表。
# 去掉每个客户名前后的空格。
# 过滤掉空客户。
# 把有效客户保存到新列表。
# 统计有效客户数量和无效客户数量。
# 最后输出：
# 原始数据：...
# 清洗后客户列表：...
# 有效客户数量：...
# 无效客户数量：...
customer_text = " 张三, 李四, , 王五, , 赵六, 钱七 "
customer_list = customer_text.split(",")

new_customer_list = []
invalid_count = 0

for customer in customer_list:
    clean_customer = customer.strip()
    if clean_customer != "":
        new_customer_list.append(clean_customer)
    else:
        invalid_count += 1

print("拆分后的原始列表:", customer_list)
print("清洗后的客户列表:", new_customer_list)
print("有效客户数量:", len(new_customer_list))
print("无效客户数量:", invalid_count)
#注释:# 输入：这一题的原始数据是customer_text
# 处理：用了 split 以","拆分原始数据为列表/ strip 去前后空格/for遍历每个客户, if 判断清理后客户是否无效/ append 有效客户进新列表
# 输出：最后输出: 原始数据,清洗后的客户列表,有效客户数量,无效客户数量

#2.要求：
#
# 把字符串按英文逗号 , 拆成列表。
# 去掉每个商品名前后的空格。
# 过滤掉空商品。
# 从有效商品里筛选出包含 "手机" 的商品，保存到新列表。
# 统计有效商品数量、无效商品数量、包含手机的商品数量。
product_text = " 苹果手机, 华为手机, , 小米耳机, 荣耀手机, , 平板电脑, 手机壳 "
product_list = product_text.split(",")

new_product_list = []
valid_product_list = []
invalid_count = 0

for product in product_list:
    clean_list = product.strip()
    if clean_list != "":
        valid_product_list.append(clean_list)
        if "手机" in clean_list:
            new_product_list.append(clean_list)
    else:
        invalid_count += 1

print("原始数据:", product_list)
print("清洗后有效商品列表", valid_product_list)
print("有效产品数量:", len(valid_product_list))
print("无效产品数量:", invalid_count)
print("包含手机的商品", new_product_list)
print("包含手机的商品数量:", len(new_product_list))
#注释:# 输入：这一题的原始数据是product_text
# 处理：用了 split 以","拆分原始数据为列表/ strip 去前后空格/for 遍历每个商品, if 判断清理后商品是否无效和"手机"是否在包含有效商品里/
# append 包含"手机"的商品进新列表
# 输出：最后输出:原始数据,清洗后有效商品列表,有效产品数量,无效产品数量,包含手机的商品,包含手机的商品数量


#3.要求：
# 把字符串按英文逗号 , 拆成列表。
# 去掉每个分数前后的空格。
# 过滤掉空值。
# 把有效分数转成整数。
# 筛选出及格分数：score >= 60。
# 把及格分数保存到新列表。
# 统计有效分数数量、无效数量、及格人数、不及格人数。
#
# 最后输出：
#
# 原始数据：...
# 清洗后分数列表：...
# 有效分数数量：...
# 无效数量：...
# 及格分数列表：...
# 及格人数：...
# 不及格人数：...
score_text = " 88, 59, , 76, 100, , 45, 60, 92 "
score_list = score_text.split(",")

new_score_list = []
clean_list = []
fail_count = 0
invalid_count = 0


for score in score_list:
    s = score.strip()
    if s != "":
        clean_item = int(s)
        clean_list.append(clean_item)
        if clean_item >= 60:
            new_score_list.append(clean_item)
        else:
            fail_count += 1
    else:
        invalid_count += 1

print("原始数据:", score_list)
print("清洗后分数列表:", clean_list)
print("有效数量:", len(clean_list))
print("无效数量:", invalid_count)
print("及格分数列表:", new_score_list)
print("及格人数:", len(new_score_list))
print("不及格人数:", fail_count)

#注释:# 输入：这一题的原始数据是score_text
# 处理：用了 split 以","拆分原始数据为列表/ strip 去前后空格/for遍历每个分数, if 判断清理后分数是否无效,无效则无效分数 += 1,
# 有效分数里判断如果 >= 60,就 append 包含>= 60的分数进新列表.否则fail_count += 1.
# 输出：最后输出:原始数据,清洗后分数列表,有效数量,无效数量,及格分数列表,及格人数,不及格人数

#4.要求：
# 把字符串按英文逗号 , 拆成列表。
# 去掉每个订单金额前后的空格。
# 过滤掉空值。
# 把有效金额转成小数。
# 筛选出大额订单：金额 >= 100。
# 把大额订单保存到新列表。
# 统计有效订单数量、无效数量、大额订单数量、普通订单数量。
#
# 最后输出：
#
# 原始数据：...
# 清洗后订单金额列表：...
# 有效订单数量：...
# 无效数量：...
# 大额订单列表：...
# 大额订单数量：...
# 普通订单数量：...
order_text = " 99.9, 200, , 35.5, 500, , 120.8, 60 "
order_list = order_text.split(",")

new_order_list = []
large_order_list = []
invalid_count = 0
normal_order_count = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order != "":
        order_item = float(clean_order)
        new_order_list.append(order_item)

        if order_item >= 100:
            large_order_list.append(order_item)
        else:
            normal_order_count += 1
    else:
        invalid_count += 1

print("原始数据:", order_list)
print("清洗后的订单金额列表:", new_order_list)
print("有效订单数量:", len(new_order_list))
print("无效数量:", invalid_count)
print("大额订单列表:", large_order_list)
print("大额订单数量:", len(large_order_list))
print("普通订单数量:", normal_order_count)

#注释:# 输入：这一题的原始数据是order_text
# 处理：用了 split 以","拆分原始数据为列表/ strip 去前后空格/ for遍历每个订单,if 判断清理后订单是否无效,无效则无效订单数量 += 1,
# 有效订单里判断如果 >= 100,就 append 大额列表.否则normal_order_count += 1.
# 输出：原始数据、清洗后订单金额列表、有效订单数量、无效数量、大额订单列表、大额订单数量、普通订单数量


#5把字符串按英文逗号 , 拆成列表。
# 去掉每个客户等级前后的空格。
# 过滤掉空值。
# 把有效等级保存到新列表。
# 再分别筛选出：
#
# VIP客户
# 普通客户
# 黑名单客户
#
# 分别保存到 3 个新列表。
# 统计有效等级数量、无效数量、VIP数量、普通数量、黑名单数量。
#输出
# 原始数据：...
# 清洗后等级列表：...
# 有效等级数量：...
# 无效数量：...
# VIP客户列表：...
# VIP数量：...
# 普通客户列表：...
# 普通数量：...
# 黑名单客户列表：...
# 黑名单数量：...
level_text = " VIP, 普通, , VIP, 黑名单, 普通, , VIP, 黑名单, 普通 "
level_list = level_text.split(",")

new_level_list = []
vip_list = []
normal_list = []
black_list = []
invalid_count = 0

for level in level_list:
    level_item = level.strip()

    if level_item != "":
        new_level_list.append(level_item)

        if level_item == "VIP":
            vip_list.append(level_item)
        elif level_item == "普通":
            normal_list.append(level_item)
        elif level_item == "黑名单":
            black_list.append(level_item)
    else:
        invalid_count += 1

print("原始数据:", level_list)
print("清洗后等级列表:", new_level_list)
print("有效等级数量:", len(new_level_list))
print("无效数量:", invalid_count)

print("VIP客户列表:", vip_list)
print("VIP数量:", len(vip_list))

print("普通客户列表:", normal_list)
print("普通数量:", len(normal_list))

print("黑名单客户列表:", black_list)
print("黑名单数量:", len(black_list))

#注释:# 输入：这一题的原始数据是level_text
# 处理：用了 split 以","拆分原始数据为列表/ strip 去前后空格/ for遍历每个客户列表,if 判断清理后列表是否无效,无效则 invalid_count += 1,
# 列表名单包含"VIP" ,append 进vip_list,包含黑名单, append 进 black_list,黑名单客户加入 black_list,否则普通客户加入 normal_list
#输出：原始数据、清洗后等级列表、有效等级数量、无效数量、VIP列表、普通客户列表、黑名单客户列表及各自数量。





