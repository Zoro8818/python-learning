#1. 要求输出：
# 有效部门数量
# 有效工资数量
# 无效记录数量
# 高工资部门数量（工资 >= 10000）
# 普通工资部门数量
# 工资总额
# 平均工资

records = [
    "技术部:12000",
    "销售部:8500",
    "",
    "财务部:9800.5",
    "行政部:abc",
    " :7000",
    "市场部:15000",
    "客服部: 6200 ",
    "运营部:",
]
valid_departments_list = []
valid_salary_list = []
large_count = 0
normal_count = 0
total_salary = 0
invalid_count = 0

for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1

    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        department = parts[0].strip()
        salary_text = parts[1].strip()

        if department == "" or salary_text == "":
            invalid_count += 1

        elif salary_text.replace(".", "", 1).isdigit():
            salary = float(salary_text)

            valid_departments_list.append(department)
            valid_salary_list.append(salary)
            total_salary += salary

            if salary >= 10000:
                large_count += 1
            else:
                normal_count += 1

        else:
            invalid_count += 1


if len(valid_salary_list) > 0:
    avg_salary = total_salary / len(valid_salary_list)

else:
    avg_salary = 0

print("有效部门数量:", len(valid_departments_list))
print("有效工资数量:", len(valid_salary_list))
print("无效记录数量:", invalid_count)
print("高工资部门数量:", large_count)
print("普通部门数量:", normal_count)
print("工资总额:", total_salary)
print("平均工资:", round(avg_salary, 2))


#2.
# 有效商品数量
# 有效库存数量
# 无效记录数量
# 高库存商品数量（库存 >= 100）
# 普通库存商品数量
# 库存总数
# 平均库存

records = [
    "苹果:120",
    "香蕉:80",
    "",
    "西瓜:abc",
    "橙子: 45 ",
    " :30",
    "草莓:",
    "葡萄:200",
    "芒果:15.5",
    "梨:0",
]

valid_product_list = []
valid_stock_list = []

large_count = 0
normal_count = 0
invalid_count = 0
total_stock = 0

for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        product = parts[0].strip()
        stock_text = parts[1].strip()

        if product == "" or stock_text == "":
            invalid_count += 1

        elif stock_text.isdigit():
            stock = int(stock_text)

            valid_product_list.append(product)
            valid_stock_list.append(stock)
            total_stock += stock

            if stock >= 100:
                large_count += 1

            else:
                normal_count += 1

        else:
            invalid_count += 1

if len(valid_stock_list) > 0:
    avg_stock = total_stock / len(valid_stock_list)

else:
    avg_stock = 0

print("有效商品数量:", len(valid_product_list))
print("有效库存数量:", len(valid_stock_list))
print("无效记录数量:", invalid_count)
print("高库存商品数量:", large_count)
print("普通库存数量:", normal_count)
print("库存总数:", total_stock)
print("平均库存:", avg_stock)


#要求输出：
# 有效员工数量
# 有效绩效数量
# 无效记录数量
# 优秀员工数量（绩效 >= 90）
# 合格员工数量（绩效 >= 60 且 < 90）
# 不合格员工数量（绩效 < 60）
# 绩效总分
# 平均绩效

records = [
    "张三:88",
    "李四: 92 ",
    "",
    "王五:abc",
    "赵六:",
    " :75",
    "孙七:59",
    "周八:100",
    "吴九:60",
    "郑十:89.5",
]

valid_employee_list = []
valid_score_list = []
excellent_count = 0
pass_count = 0
fail_count = 0
invalid_count = 0
total_score = 0

for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1

    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        employee = parts[0].strip()
        score_text = parts[1].strip()

        if employee == "" or score_text == "":
            invalid_count += 1

        elif score_text.replace(".", "", 1).isdigit():
            score = float(score_text)

            valid_employee_list.append(employee)
            valid_score_list.append(score)
            total_score += score

            if score >= 90:
                excellent_count += 1

            elif score >= 60:
                pass_count += 1

            else:
                fail_count += 1

        else:
            invalid_count += 1

if len(valid_score_list) > 0:
    avg_score = total_score / len(valid_score_list)

else:
    avg_score = 0

print("有效员工数量:", len(valid_employee_list))
print("有效绩效数量:", len(valid_score_list))
print("无效记录数量:", invalid_count)
print("优秀员工数量:", excellent_count)
print("合格员工数量:", pass_count)
print("不合格员工数量:", fail_count)
print("绩效总分:", total_score)
print("平均绩效:", round(avg_score, 2))



