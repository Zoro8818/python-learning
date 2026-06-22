#1. 要求输出：
#
# 原始报名列表
# 有效学生名单
# 有效学生数量
# 无效空值数量
# 第一个学生
# 最后一个学生

student_text = " 小明, 小红, , 小刚, 小丽, , 小强, "
student_list = student_text.split(",")

new_student_list = []
invalid_count = 0

for student in student_list:
    clean_student = student.strip()
    if clean_student != "":
        new_student_list.append(clean_student)
    else:
        invalid_count += 1

print("原始报名列表:", student_list)
print("有效学生名单:", new_student_list)
print("有效学生数量:", len(new_student_list))
print("无效空值数量:", invalid_count)
print("第一个学生:", new_student_list[0])
print("最后一个学生:", new_student_list[-1])

# 注释输入:student_text
# 处理:split 拆分成原始列表, for 遍历, if 判断是否为有效数据,成功则append 进新列表,否则 invalid_count += 1
# 保存:new_student_list, invalid_count
# 输出:student_list, new_student_list, len(new_student_list), new_student_list[0], new_student_list[-1]

#2. 要求输出：
#
# 原始商品列表
# 清洗后的商品列表
# 有效商品数量
# 无效空值数量
# 水果商品列表
# 水果商品数量
# 非水果商品数量
goods_text = " 苹果-水果, 牛奶-饮品, , 香蕉-水果, 面包-食品, 葡萄-水果, , 鸡蛋-食品 "
goods_list = goods_text.split(",")

new_goods_list = []
invalid_count = 0
fruit_list = []
normal_count = 0

for goods in goods_list:
    clean_goods = goods.strip()

    if clean_goods != "":
        new_goods_list.append(clean_goods)

        if "水果" in clean_goods:
            fruit_list.append(clean_goods)
        else:
            normal_count += 1
    else:
        invalid_count += 1

print("原始商品列表:", goods_list)
print("清洗后的商品列表:", new_goods_list)
print("有效商品数量:", len(new_goods_list))
print("无效空值数量:", invalid_count)
print("水果商品列表:", fruit_list)
print("水果商品数量:", len(fruit_list))
print("非水果类商品数量:", normal_count)


#注释 输入: goods_text
#处理:split 拆分成原始列表,for 遍历,if 判断是否为有效数据,有效数据 append 进新列表, 否则 invalid_count += 1.
#if判断关键词 "水果" in clean_goods, 成功append 进 fruit_list, 否则normal_count += 1
#保存:new_goods_list, invalid_count, fruit_list, normal_count
#输出:goods_list, new_goods_list, len(new_goods_list), invalid_count, fruit_list, len(fruit_list), normal_count

#3.要求输出：

# 原始分数列表
# 清洗后的分数列表
# 有效分数数量
# 无效空值数量
# 优秀分数列表，分数 >= 90
# 及格分数列表，60 <= 分数 < 90
# 不及格分数列表，分数 < 60
# 优秀人数
# 及格人数
# 不及格人数
# 总分
# 平均分

score_text = " 88, 95, , 59, 100, 76, , 45, 90 "
score_list = score_text.split(",")

new_score_list = []
invalid_count = 0
excellent_scores_list = []
pass_scores_list = []
fail_scores_list = []
total_score = 0

for score in score_list:
    new_score = score.strip()

    if new_score != "":
        s = int(new_score)

        total_score += s
        new_score_list.append(s)
        if s >= 90:
            excellent_scores_list.append(s)
        elif s >= 60:
            pass_scores_list.append(s)
        else:
            fail_scores_list.append(s)

    else:
        invalid_count += 1

avg_score = total_score / len(new_score_list)


print("原始分数列表:", score_list)
print("清洗后的分数列表:", new_score_list)
print("有效分数数量:", len(new_score_list))
print("无效空值数量:", invalid_count)
print("优秀分数列表:", excellent_scores_list)
print("及格分数列表:", pass_scores_list)
print("不及格分数列表:", fail_scores_list)
print("优秀人数:", len(excellent_scores_list))
print("及格人数:", len(pass_scores_list))
print("不及格人数:", len(fail_scores_list))
print("总分:", total_score)
print("平均分:", round(avg_score, 2))

#注释:输入:score_text
#过程:split 拆分成原始列表, for 遍历, if 判断是否为有效值, 成功 append 进新列表, total_score += s, 否则invalid_count += 1
#if判断 s >= 90, append 进excellent_scores_list, elif 判断 s >= 60, append 进pass_scores_list,
# 否则 append 进fail_scores_list , 平均分 = total_score / len(new_score_list)
#保存:new_score_list, invalid_count, excellent_scores_list, pass_scores_list, fail_scores_list,total_score,avg_score
#输出:score_list, new_score_list, len(new_score_list), invalid_count, excellent_scores_list, len(excellent_scores_list)
#pass_scores_list, len(pass_scores_list), fail_scores_list, len(fail_scores_list), total_score, round(avg_score, 2)

#4. 要求输出：
#
# 原始订单列表
# 清洗后的订单金额列表
# 有效订单数量
# 无效空值数量
# 高价值订单列表，金额 >= 300
# 高价值订单数量
# 普通订单数量，金额 < 300
# 订单总金额
# 平均订单金额
order_text = " 59.9, 120, , 300.5, 88, , 1000, 45.5 "
order_list = order_text.split(",")

new_order_list = []
invalid_count = 0
large_order_list = []
normal_count = 0
total_order = 0

for order in order_list:
    clean_order = order.strip()

    if clean_order != "":
        order_amount = float(clean_order)
        total_order += order_amount
        new_order_list.append(order_amount)

        if order_amount >= 300:
            large_order_list.append(order_amount)

        else:
            normal_count += 1

    else:
        invalid_count += 1

avg_order = total_order / len(new_order_list)

print("原始订单列表:", order_list)
print("清洗后的订单金额列表:", new_order_list)
print("有效订单数量:", len(new_order_list))
print("无效空值数量:", invalid_count)
print("高价值订单列表:", large_order_list)
print("高价值订单数量:", len(large_order_list))
print("普通订单数量:", normal_count)
print("订单总金额:", total_order)
print("订单平均金额:", round(avg_order, 2))

#注释:输入:order_text
#过程:split 拆分成原始列表,for 遍历, strip去前后空格, if判断是否为有效值, 成功则 append 进 new_order_list, 否则 invalid_count += 1
#total_order += order_amount,if 判断>= 300,成功 append 进large_order_list,否则 normal_count += 1,平均值 = total_order / len(new_order_list)
#保存:new_order_list, invalid_count, large_order_list, normal_count, total_order, avg_order
#输出:order_list, new_order_list, len(new_order_list), invalid_count, large_order_list, len(large_order_list)
#, normal_count, total_order, round(avg_order, 2)


#5.要求输出：
#
# 原始客户列表
# 清洗后的客户列表
# 有效客户数量
# 无效空值数量
# 金卡客户列表
# 金卡客户数量
# 非金卡客户数量
# 第一个金卡客户
# 最后一个金卡客户

member_text = " 张三-金卡, 李四-普通, , 王五-银卡, 赵六-金卡, 钱七-普通, , 孙八-金卡 "
member_list = member_text.split(",")

new_member_list = []
invalid_count = 0
gold_list = []
normal_count = 0

for member in member_list:
    clean_member = member.strip()
    if clean_member != "":
        new_member_list.append(clean_member)

        if "金卡" in clean_member:
            gold_list.append(clean_member)
        else:
            normal_count += 1

    else:
        invalid_count += 1


print("原始客户列表:", member_list)
print("清洗后的客户列表:", new_member_list)
print("有效客户数量:", len(new_member_list))
print("无效空值数量:", invalid_count)
print("金卡客户列表:", gold_list)
print("金卡客户数量:", len(gold_list))
print("非金卡客户数量:", normal_count)
print("第一个金卡客户:", gold_list[0])
print("最后一个金卡客户:", gold_list[-1])

#注释:输入:member_text
#过程:split 拆分成原始列表, for 遍历, strip去前后空格, if 判断是否为有效数据, 成功append 进new_member_list, 否则invalid_count += 1
#if 判断 关键词 "金卡" in clean_member, 成功 append 进gold_list,否则 normal_count += 1
#保存:new_member_list, invalid_count, gold_list, normal_count
#输出:member_list, new_member_list, len(new_member_list), invalid_count, gold_list, len(gold_list), normal_count
#gold_list[0],gold_list[-1]