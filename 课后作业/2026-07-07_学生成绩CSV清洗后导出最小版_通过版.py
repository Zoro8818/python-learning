# 2026-07-07 学生成绩 csv 清洗后导出最小版
# 字段：学生姓名,分数,班级
# 输入：input/students.csv
# 输出：
# output/students_cleaned.csv
# output/students_summary.txt

# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/students.csv"
cleaned_file = "D:/python-project/课后作业/output/students_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/students_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 第 3 块：按行拆分
lines = csv_text.splitlines()


# 第 4 块：去掉表头，准备处理数据行
raw_record_list = []


# 第 5 块：准备结果列表和统计变量
valid_student_list = []
valid_score_list = []
valid_class_list = []

invalid_count = 0
total_score = 0

excellent_count = 0
pass_count = 0
fail_count = 0


# 第 6 块：循环处理每一条记录
for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "学生姓名,分数,班级":
        raw_record_list.append(clean_line)

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        student = parts[0].strip()
        score_text = parts[1].strip()
        class_name = parts[2].strip()

        if student == "" or score_text == "":
            invalid_count += 1
        elif score_text.isdigit():
            score = int(score_text)

            valid_student_list.append(student)
            valid_score_list.append(score)
            valid_class_list.append(class_name)
            total_score += score

            if score >= 90:
                excellent_count += 1
            elif score >= 60:
                pass_count += 1
            else:
                fail_count += 1

        else:
            invalid_count += 1


# 第 7 块：统计数量和平均值
valid_count = len(valid_student_list)

if valid_count > 0:
    avg_score = total_score / valid_count
else:
    avg_score = 0


# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("学生姓名,分数,班级\n")

    for i in range(valid_count):
        f.write(
            valid_student_list[i]
            + ","
            + str(valid_score_list[i])
            + ","
            + valid_class_list[i]
            + "\n"
        )


# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("学生成绩 CSV 清洗统计报告\n")
    f.write("========================\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总分：" + str(total_score) + "\n")
    f.write("平均分：" + format(avg_score, ".2f") + "\n")
    f.write("优秀数量：" + str(excellent_count) + "\n")
    f.write("及格数量：" + str(pass_count) + "\n")
    f.write("不及格数量：" + str(fail_count) + "\n")


print("学生成绩 CSV 清洗完成")
print("有效记录数量：", valid_count)
print("无效记录数量：", invalid_count)
print("cleaned csv 输出路径：", cleaned_file)
print("summary txt 输出路径：", summary_file)