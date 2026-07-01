#1 学生成绩清洗统计变体题
score_text = "小王:80, , 小李, :90, 小赵:, 小孙:abc, 小周:100, 小吴:0, 小郑:59.5, 小钱:60, 小陈:89.5, 小冯:95, 小刘:30"
score_list = score_text.split(",")

valid_student_list = []
valid_score_list = []
invalid_count = 0
total_score = 0

high_score_student_list = []
pass_student_list = []
fail_student_list = []

high_score_count = 0
pass_count = 0
fail_count = 0

for record in score_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        student = parts[0].strip()
        score_value_text = parts[1].strip()

        if student == "":
            invalid_count += 1
        elif score_value_text == "":
            invalid_count += 1
        elif not score_value_text.replace(".", "", 1).isdigit():
            invalid_count += 1
        else:
            score = float(score_value_text)

            valid_student_list.append(student)
            valid_score_list.append(score)
            total_score += score

            if score >= 90:
                high_score_student_list.append(student)
                high_score_count += 1

            elif score >= 60:
                pass_student_list.append(student)
                pass_count += 1

            else:
                fail_student_list.append(student)
                fail_count += 1

valid_count = len(valid_score_list)

if valid_count > 0:
    avg_score = total_score / valid_count

    max_student = valid_student_list[0]
    max_score = valid_score_list[0]

    min_student = valid_student_list[0]
    min_score = valid_score_list[0]

    for i in range(valid_count):
        if valid_score_list[i] > max_score:
            max_student = valid_student_list[i]
            max_score = valid_score_list[i]

        if valid_score_list[i] < min_score:
            min_student = valid_student_list[i]
            min_score = valid_score_list[i]

else:
    avg_score = 0
    max_student = ""
    max_score = 0
    min_student = ""
    min_score = 0

print("有效学生列表：", valid_student_list)
print("有效成绩列表：", valid_score_list)
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("总分：", total_score)
print("平均分：", avg_score)

print("最高分学生：", max_student)
print("最高分：", max_score)
print("最低分学生：", min_student)
print("最低分：", min_score)

print("高分学生列表：", high_score_student_list)
print("高分数量：", high_score_count)
print("合格学生列表：", pass_student_list)
print("合格数量：", pass_count)
print("不合格学生列表：", fail_student_list)
print("不合格数量：", fail_count)


