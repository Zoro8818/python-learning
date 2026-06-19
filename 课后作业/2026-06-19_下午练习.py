#第 1 题：统计有效客户数量
customer_text = " 张三, 李四, , 王五, 赵六, , 钱七 "
customer_list = customer_text.split(",")
print("拆分后的原始列表:",customer_list)
new_customer_list = []

for customer in customer_list:
    new_customer = customer.strip()
    if new_customer != "":
        new_customer_list.append(new_customer)
count = len(new_customer_list)

print("清理后列表为:",new_customer_list)
print("有效客户数量:", count)
#注释:这题看到“去空格”，我想到 strip() ,保存有效客户用 append() , 统计数量用 len()

#第 2 题：筛选包含“手机”的商品
# 要求：
# 清洗成列表
# 找出包含 "手机" 的商品
# 保存到 phone_goods_list
# 输出结果和数量

goods_text = " 手机壳, 数据线, 手机支架, 鼠标, 手机膜, 键盘 "
goods_list = goods_text.split(",")
print("拆分后的原始列表:",goods_list)

phone_goods_list = []

for goods in goods_list:
    clean_goods = goods.strip()

    if "手机" in clean_goods:
        phone_goods_list.append(clean_goods)

count = len(phone_goods_list)

print("包含手机的商品:", phone_goods_list)
print("数量:", count)

##注释:看到清洗用split(), 找出包含XXX的商品用in, 数量用count, 统计新的商品append()
#3第 3 题：成绩字符串统计
# 要求：
# 切成列表
# 去空格
# 转成整数
# 统计及格人数
# 保存不及格分数到 fail_score_list

score_text = " 88, 59, 60, 76, 45, 90 "
score_list = score_text.split(",")
print("拆分后的原始列表:", score_list)
fail_score_list = []
count = 0

for score in score_list:
    clean_score = int(score.strip()) #字符串里的数字 → 要比较大小 / 求和 / 平均值 用int转为整数
    if clean_score >= 60:
        count += 1
    else:
        fail_score_list.append(clean_score)

print("及格人数为:", count)
print("不及格的分数为:", fail_score_list)
#注释:去空格split,转成整数用int , 统计几个人数用count, 保存不及格分数到 fail_score_list 用append()

#要求：
#拆包成 name, department, salary
employee = ("张三", "销售", 5000)
name, department, salary = employee
print("员工姓名:", name)
print("所属部门:", department)
print("工资:", salary)
#注释:看到“固定员工信息”，我想到 tuple