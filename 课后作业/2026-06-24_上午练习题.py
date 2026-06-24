records = [
    "销售部: 8500",
    "技术部:12000",
    "行政部:",
    " :7000",
    "财务部:abc",
    "",
    "运营部: 6000",
    "市场部:9500",
    "客服部: 4000",
    "人事部:10000"
]

valid_salaries = []
valid_salary_count = 0
high_count = 0
normal_count = 0
low_count = 0
invalid_count = 0
total_salary = 0

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

        if department =="" or salary_text == "":
            invalid_count += 1

        elif salary_text.replace(".", "", 1).isdigit():
            salary = float(salary_text)

            valid_salaries.append(salary)
            valid_salary_count += 1
            total_salary += salary

            if salary >= 10000:
                high_count += 1
            elif salary >=7000:
                normal_count += 1
            else:
                low_count += 1

        else:
            invalid_count += 1

if len(valid_salaries) > 0:
    avg_salary = total_salary / len(valid_salaries)

else:
    avg_salary = 0

print("有效数据数量:", valid_salary_count)
print("无效数据数量:", invalid_count)
print("工资总和:", total_salary)
print("平均工资:", round(avg_salary, 2))
print("高工资部门数量:", high_count)
print("中工资部门数量:", normal_count)
print("低工资部门数量:", low_count)