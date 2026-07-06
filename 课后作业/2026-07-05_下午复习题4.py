input_file = "D:/python-project/课后作业/input/input.txt"
report_file = "D:/python-project/课后作业/output/student_report.txt"

valid_student_list = []
invalid_count = 0

with open(input_file, "r", encoding="utf-8") as f:
    student_text = f.read()

raw_student_list = student_text.splitlines()

for record in raw_student_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    else:
        valid_student_list.append(clean_record)

with open(report_file, "w", encoding="utf-8") as f:
    f.write("学生名单清洗结果如下：\n")
    f.write("\n")
    f.write("有效学生列表：" + str(valid_student_list) + "\n")
    f.write("有效学生数量：" + str(len(valid_student_list)) + "\n")
    f.write("无效行数量：" + str(invalid_count) + "\n")