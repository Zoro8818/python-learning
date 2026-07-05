student_text = " 小王, 小李, , 小张 ,   ,小周,小王 "

student_list = student_text.split(",")

valid_student_list = []
invalid_count = 0

for record in student_list:
    clean_record = record.strip()

    if clean_record == "":
        invalid_count += 1
    else:
        valid_student_list.append(clean_record)

print("原始学生文本：", student_text)
print("有效学生列表：", valid_student_list)
print("有效学生数量：", len(valid_student_list))
print("无效学生数量：", invalid_count)