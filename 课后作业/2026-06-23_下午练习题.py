#1. 要求输出
# 有效员工数量
# 有效奖金数量
# 无效记录数量
# 高奖金员工数量（奖金 >= 2000）
# 普通奖金员工数量（奖金 > 0 且 < 2000）
# 零奖金员工数量（奖金 == 0）
# 奖金总额
# 平均奖金
records = [
    "张三:3000",
    "李四: 800 ",
    "",
    "王五:abc",
    "赵六:",
    " :500",
    "孙七:0",
    "周八:1500.5",
    "吴九:200",
    "郑十:5000",
]

valid_employee_list =  []
valid_bonus_list = []

invalid_count = 0
large_count = 0
normal_count = 0
zero_count = 0
total_bonus = 0

for record in records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1

    else:
        parts = clean_record.split(":", 1)
        employee = parts[0].strip()
        bonus_text = parts[1].strip()

        if employee == "" or bonus_text == "":
            invalid_count += 1

        elif bonus_text.replace(".", "", 1).isdigit():
            bonus = float(bonus_text)

            valid_employee_list.append(employee)
            valid_bonus_list.append(bonus)
            total_bonus += bonus

            if bonus >= 2000:
                large_count += 1

            elif bonus > 0:
                normal_count += 1

            else:
                zero_count += 1

        else:
            invalid_count += 1

if len(valid_bonus_list) > 0:
    avg_bonus = total_bonus / len(valid_bonus_list)

else:
    avg_bonus = 0

print("有效员工数量:", len(valid_employee_list))
print("有效奖金数量:", len(valid_bonus_list))
print("无效记录数量:", invalid_count)
print("高奖金员工数量:", large_count)
print("普通奖金员工数量:", normal_count)
print("零奖金员工数量:", zero_count)
print("奖金总额:", total_bonus)
print("平均奖金:", round(avg_bonus, 2))


