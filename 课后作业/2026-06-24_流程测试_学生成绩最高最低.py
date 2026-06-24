# 用 record 遍历 score_records
# 清洗整条记录
# 空记录算无效
# 不包含 : 算无效
# 用 split(":", 1) 拆成 student 和 score_text
# 学生名为空算无效
# 分数文本为空算无效
# 分数文本必须先判断是不是合法数字，再 float() 转换
# 有效学生名保存到 valid_student_list
# 有效分数保存到 valid_score_list
# 无效记录数量用 invalid_count
# 累加总分 total_score
# 计算平均分 avg_score
# 找出：最高分学生 max_student
# 最高分 max_score
# 最低分学生 min_student
# 最低分 min_score
#
# 输出：
# 有效学生数量
# 有效学生名单
# 无效记录数量
# 总分
# 平均分，保留 2 位小数
# 最高分学生
# 最高分
# 最低分学生
# 最低分

score_records = [
    "张三: 88",
    "李四: 95.5",
    "王五:",
    " :76",
    "赵六:abc",
    "",
    "钱七: 60",
    "孙八:0",
    "周九:100",
    "吴十: 72.5"
]

valid_student_list = []
valid_score_list = []
invalid_count = 0
total_score = 0

for record in score_records:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    elif ":" not in clean_record:
        invalid_count += 1
    else:
        parts = clean_record.split(":", 1)
        student = parts[0].strip()
        score_text = parts[1].strip()

        if student == "" or score_text == "" :
            invalid_count += 1

        elif score_text.replace(".", "", 1).isdigit():
            score = float(score_text)

            valid_student_list.append(student)
            valid_score_list.append(score)
            total_score += score

        else:
            invalid_count += 1


if len(valid_score_list) > 0:
    avg_score = total_score / len(valid_score_list)
    max_score = valid_score_list[0]
    max_student = valid_student_list[0]
    min_score = valid_score_list[0]
    min_student = valid_student_list[0]

    for i in range(len(valid_score_list)):
        if valid_score_list[i] > max_score:
            max_score = valid_score_list[i]
            max_student = valid_student_list[i]

        if valid_score_list[i] < min_score:
            min_score = valid_score_list[i]
            min_student = valid_student_list[i]

else:
    avg_score = 0
    max_score = 0
    max_student = ""
    min_score = 0
    min_student = ""

print("有效学生数量:", len(valid_score_list))
print("有效学生名单:", valid_student_list)
print("无效记录数量:", invalid_count)
print("总分:", total_score)
print("平均分:", round(avg_score, 2))
print("最高分学生:", max_student)
print("最高分:", max_score)
print("最低分学生:", min_student)
print("最低分:", min_score)
