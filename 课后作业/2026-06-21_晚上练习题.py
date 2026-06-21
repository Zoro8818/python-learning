#1. 要求输出：
# 原始姓名列表
# 清洗后的姓名列表
# 有效姓名数量
# 无效空值数量
# 第一个有效姓名
# 最后一个有效姓名

name_text = " 张三, , 李四, 王五, , 赵六, 钱七, "
name_list = name_text.split(",")

clean_name_list = []
invalid_count = 0

for name in name_list:
    clean_name = name.strip()
    if clean_name != "":
        clean_name_list.append(clean_name)

    else:
        invalid_count += 1

print("原始姓名列表:", name_list)
print("清理后的姓名列表:", clean_name_list)
print("有效姓名数量:", len(clean_name_list))
print("无效空值数量:", invalid_count)
print("第一个有效姓名:", clean_name_list[0])
print("最后一个有效姓名:", clean_name_list[-1])

# 注释:输入是什么：name_text
# 处理过程是什么：split() 拆分成原始列表, for 遍历,strip()去前后空格,if 判断是否为有效数据,
# 成功: append 添加进clean_name_list,空值就 invalid_count += 1
# 输出结果是什么：name_list, clean_name_list, len(clean_name_list), invalid_count, clean_name_list[0], clean_name_list[-1]


#2. 要求输出：
# 原始商品列表
# 清洗后的商品列表
# 有效商品数量
# 无效空值数量

goods_text = " 苹果, , 香蕉, 牛奶, , 面包, 鸡蛋, "
goods_list = goods_text.split(",")

clean_goods_list = []
invalid_count = 0

for goods in goods_list:
    clean_goods = goods.strip()
    if clean_goods != "":
        clean_goods_list.append(clean_goods)

    else:
        invalid_count += 1

print("原始商品列表:", goods_list)
print("清洗后的商品列表:", clean_goods_list)
print("有效商品数量:", len(clean_goods_list))
print("无效空值数量:", invalid_count)

# 注释:输入是什么：goods_text
# 处理过程是什么：split 拆分成原始列表, for 遍历, strip 去前后空格, 有效数据 append 进新列表,空值就 invalid_count += 1
# 输出结果是什么：goods_list, clean_goods_list, len(clean_goods_list), invalid_count

#3. 要求输出：
# 原始分数列表
# 清洗后的分数列表
# 有效分数数量
# 无效空值数量
# 及格分数列表，分数 >= 60
# 不及格分数列表，分数 < 60
# 及格人数
# 不及格人数
# 总分
# 平均分

score_text = " 88, 59, 60, 76, , 45, 90, , 100 "
score_list = score_text.split(",")

clean_score_list = []
invalid_count = 0
pass_score = []
fail_score = []
total_score = 0

for score in score_list:
    clean_score = score.strip()

    if clean_score != "":
        s = int(clean_score)
        clean_score_list.append(s)

        total_score += s
        if s >= 60:
            pass_score.append(s)
        else:
            fail_score.append(s)

    else:
        invalid_count += 1

avg_score = total_score / len(clean_score_list)

print("原始分数列表:", score_list)
print("清理后的分数列表:", clean_score_list)
print("有效分数数量:", len(clean_score_list))
print("无效空值数量:", invalid_count)
print("及格分数列表:", pass_score)
print("不及格分数列表:", fail_score)
print("及格人数:", len(pass_score))
print("不及格人数:", len(fail_score))
print("总分:", total_score)
print("平均分:", avg_score)

# 注释:输入是什么:score_text
# 处理过程是什么：split拆分成原始列表, for 遍历每个数据, strip 去每个数据前后空格, 有效数据 append 进新列表, 空值invalid_count += 1
# 如果>= 60,append 进pass_score, 否则append 进fail_score, 平均分 = 总分数 / 总人数
# 输出是什么:score_list, clean_score_list, len(clean_score_list), invalid_count, pass_score, fail_score, len(pass_score)
#, len(fail_score), total_score, avg_score


#4. 要求输出：
# 原始订单列表
# 清洗后的订单金额列表
# 有效订单数量
# 无效空值数量
# 大额订单列表，金额 >= 100
# 大额订单数量
# 普通订单数量，金额 < 100
# 订单总金额
# 平均订单金额

order_text = " 99.9, 200, , 35.5, 500, , 120.8, 60 "
order_list = order_text.split(",")

clean_order_list = []
invalid_count = 0
large_order = []
normal_order = []
total_order = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order != "":
        o = float(clean_order)

        total_order += o
        clean_order_list.append(o)
        if o >= 100:
            large_order.append(o)
        else:
            normal_order.append(o)

    else:
        invalid_count += 1

avg_order = total_order / len(clean_order_list)

print("原始订单列表:", order_list)
print("清洗后的订单金额列表:", clean_order_list)
print("有效订单数量:", len(clean_order_list))
print("无效空值数量:", invalid_count)
print("大额订单列表:", large_order)
print("大额订单数量:", len(large_order))
print("普通订单数量:", len(normal_order))
print("订单总金额:", total_order)
print("平均订单金额:", avg_order)


# 注释:输入是什么:order_text
# 处理过程是什么：split 拆分成原始列表,for 遍历, if判断 , 有效数据 append 进clean_order_list, 无效则invalid_count += 1
#if 判断 >= 100 ,append 进large_order,否则 添加进normal_order,平均值 = total_order / len(clean_order_list)
# 输出是什么:, order_text, clean_order_list, len(clean_order_list), invalid_count, large_order, len(large_order)
#, len(normal_order), total_order, avg_order

#5.要求输出：
# 原始客户列表
# 清洗后的客户列表
# 有效客户数量
# 无效空值数量
# VIP客户列表
# VIP客户数量
# 普通客户数量
# 第一个VIP客户
# 最后一个VIP客户

vip_text = " 张三-VIP, 李四-普通, , 王五-VIP, 赵六-普通, 钱七-VIP, "
customer_list = vip_text.split(",")

clean_vip_list = []
invalid_count = 0
vip_list = []
normal_count = 0

for vip in customer_list:
    clean_vip = vip.strip()
    if clean_vip != "":
        clean_vip_list.append(clean_vip)

        if "VIP" in clean_vip:
            vip_list.append(clean_vip)
        else:
            normal_count += 1

    else:
        invalid_count += 1

print("原始客户列表:", customer_list)
print("清洗后的客户列表:", clean_vip_list)
print("有效客户数量:", len(clean_vip_list))
print("无效空值数量:", invalid_count)
print("VIP客户列表:", vip_list)
print("VIP客户数量:", len(vip_list))
print("普通客户数量:", normal_count)
print("第一个VIP客户:", vip_list[0])
print("最后一个VIP客户:", vip_list[-1])


# 注释:输入是什么:vip_text
# 处理过程是什么：split 拆分成新列表, for 遍历, if 判断是否为有效数据, 成功 append 进clean_vip_list, 否则 invalid_count += 1
# if 判断关键词 "VIP" in clean_vip,成功 append 进vip_list 否则normal_count += 1
# 输出结果:, customer_list, clean_vip_list, len(clean_vip_list), invalid_count, vip_list, len(vip_list), normal_count
#, vip_list[0], vip_list[-1]