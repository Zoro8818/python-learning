#题目：
# 要求：
# 用 split(",") 切成列表。
# 用 strip() 清洗每个名字。
# 空字符串不要保存。
# 输出清洗后的客户列表。
# 输出有效客户数量。
# 输出第一个客户和最后一个客户。
customer_text = " 张三, 李四, , 王五, 赵六, , 钱七, 孙八 "

customer_list = customer_text.split(",")
print("拆分后的原始列表:", customer_list)

new_customer_list = []

for customer in customer_list:
    clean_customer = customer.strip()

    if clean_customer != "":
        new_customer_list.append(clean_customer)

customer_count = len(new_customer_list)

print("清洗后的客户列表:", new_customer_list)
print("有效客户数量:", customer_count)
print("第一个客户为:", new_customer_list[0])
print("最后一个客户为:", new_customer_list[-1])
#注释:看到切成列表,用split(), 清洗每个名字.用 strip() , 有效客户数量用len,count也可以,输出有效客户用append(),
# 有效客户用!= "",输出第一个客户和最后一个客户s[0] s[-1]

# 要求：
# 清洗成列表。
# 筛选包含 "手机" 的商品。
# 保存到
# 输出筛选结果。
# 输出数量。
# 如果数量大于 3，输出：手机相关商品较多，否则输出：手机相关商品较少。
goods_text = " 手机壳, 数据线, 手机支架, 鼠标, 手机膜, 键盘, 手机充电器 "
#-->split(",")按逗号分割列表
goods_list = goods_text.split(",")
print("拆分后的原始列表:", goods_list)
#新列表
phone_goods_list = []
#遍历每个商品，清洗后判断是否包含“手机”
for goods in goods_list:
    clean_goods = goods.strip()

    if "手机" in clean_goods:
        phone_goods_list.append(clean_goods)
#统计手机相关商品数量
phone_count = len(phone_goods_list)

print("手机相关商品:", phone_goods_list)
print("手机相关商品数量:", phone_count)

if phone_count > 3:
    print("手机相关商品较多")
else:
    print("手机相关商品较少")

#题目：
# 要求：
# 切成列表。-->split()
# 每个分数去空格。  -->strip()
# 转成整数。  -->int
# 统计及格人数。  -->  -> len(pass_score_list)
# 保存不及格分数到 fail_score_list。  -->append()
# 计算总分和平均分。   total_score-->    avg_score-->total_score / len(pass_score_list + fail_score_list)

score_text = " 88, 59, 60, 76, 45, 90, 100, 30 "
#先把成绩字符串按逗号切开。
score_list = score_text.split(",")
print("拆分后的原始列表:", score_list)
#pass_score_list 保存及格分数
# fail_score_list 保存不及格分数
# total_score 保存总分
pass_score_list = []
fail_score_list = []
total_score = 0
#循环处理每一个分数：
# 先去掉空格
# 再转成整数
# 然后加到总分里
for score in score_list:
    clean_score = int(score.strip())

    total_score += clean_score
#如果分数 >= 60，就放进及格列表。
#否则，就放进不及格列表。
    if clean_score >= 60:
        pass_score_list.append(clean_score)
    else:
        fail_score_list.append(clean_score)

pass_count = len(pass_score_list)
total_count = len(pass_score_list) + len(fail_score_list)
avg_score = total_score / total_count

print("及格人数为:", pass_count)
print("不及格分数为:", fail_score_list)
print("总分为:", total_score)
print("平均分为:", avg_score)

#任务 4：tuple 固定信息
# 要求：
# 拆包成 name, department, salary。
# 分三行输出姓名、部门、工资。
# 写一句注释：为什么这里可以用 tuple？

employee = ("张三", "销售", 5000)
name, department, salary = employee
print("姓名:", name)
print("部门:", department)
print("工资:", salary)
#注释:这题看到“固定员工信息”，我想到 tuple，因为这组数据创建后不需要修改。


#
goods_text = " 苹果, , 香蕉, 牛奶, , 面包 "
goods_list = goods_text.split(",")

clean_goods_list = []

for goods in goods_list:
    clean_goods = goods.strip()
    if clean_goods != "":
        clean_goods_list.append(clean_goods)

print("清洗后的商品列表:", clean_goods_list)
print("商品数量:", len(clean_goods_list))

#注释:
# split：把字符串切成列表
# strip：去掉前后空格
# if != ""：过滤空值
# append：保存清洗后的结果