# 要求输出：
# 原始报名列表
# 有效报名名单
# 有效人数
# 无效空值数量
# 第一个报名人
# 最后一个报名人
signup_text = " 张三, , 李四, 王五, , 赵六, 钱七 "
sign_list = signup_text.split(",")

clean_signup_list = []
invalid_count = 0

for signup in sign_list:
    single_signup = signup.strip()
    if single_signup != "":
        clean_signup_list.append(single_signup)

    else:
        invalid_count += 1

print("原始报名列表:", sign_list)
print("有效报名名单:", clean_signup_list)
print("有效人数:", len(clean_signup_list))
print("无效空值数量:", invalid_count)
print("第一个报名人:", clean_signup_list[0])
print("最后一个报名人:", clean_signup_list[-1])

# 输入是什么：signup_text
# 处理过程是什么：split拆分成原始列表, for 遍历, strip去前后空格, if 判断是否为有效数据,成功 append 添加进clean_signup_list
#否则 invalid_count += 1
# 输出结果是什么：sign_list, clean_signup_list , len(clean_signup_list), invalid_count, clean_signup_list[0], clean_signup_list[-1]
# 现实用途：用于清理统计各类关于姓名的列表

# 要求输出：
# 清洗后销售金额列表
# 有效销售记录数量
# 无效数量
# 销售总额
# 平均销售额
# 大额销售列表，金额 >= 100
# 大额销售数量
sales_text = " 99, 268, , 35, 500, , 120, 60 "

sales_list = sales_text.split(",")

clean_sales_list = []
large_sales_list = []
invalid_count = 0
total_sales = 0
normal_count = 0

for sale in sales_list:
    clean_sales = sale.strip()

    if clean_sales != "":
        sales_amount = int(clean_sales)

        clean_sales_list.append(sales_amount)
        total_sales += sales_amount

        if sales_amount >= 100:
            large_sales_list.append(sales_amount)
        else:
            normal_count += 1

    else:
        invalid_count += 1

avg_sales = total_sales / len(clean_sales_list)


print("清洗后销售金额列表:", clean_sales_list)
print("有效销售记录数量:", len(clean_sales_list))
print("无效数量:", invalid_count)
print("销售总额:", total_sales)
print("平均销售额:", avg_sales)
print("大额销售列表:", large_sales_list)
print("大额销售数量:", len(large_sales_list))
print("普通销售数量:", normal_count)

# 输入是什么：sales_text
# 处理过程是什么：split()拆分成原始列表,for 遍历, strip去前后空格, total_sales += sales_amount,
# if判断是否为有效数据,成功append 进clean_sales_list,
# 失败 invalid_count += 1,if 判断 >= 100, append 进large_sales_list, avg_sales = total_sales / len(clean_sales_list)
# 输出结果是什么：clean_sales_list, len(clean_sales_list), invalid_count, total_sales, avg_sales,
# large_sales_list, len(large_sales_list), normal_count
# 现实用途: 用于清理各类关于数字类的列表

