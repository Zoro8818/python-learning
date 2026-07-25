# 1. 文件路径
input_file = "D:/python-project/课后作业/input/site_worker_entry_check.csv"
cleaned_file = "D:/python-project/课后作业/output/site_worker_entry_check_cleaned.csv"
report_file = "D:/python-project/课后作业/output/site_worker_entry_check_report.txt"


# 2. 读取 CSV 文件
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 3. 按行拆分
lines = csv_text.splitlines()


# 4. 去掉表头和空行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if (
        clean_line != ""
        and clean_line != "人员编号,培训状态,证件状态,证件剩余有效天数"
    ):
        raw_record_list.append(clean_line)


# 5. 有效字段列表
valid_worker_id_list = []
valid_training_status_list = []
valid_certificate_status_list = []
valid_remaining_days_list = []


# 6. 有效完整记录列表
cleaned_record_list = []


# 7. 无效记录和原因
invalid_record_list = []
invalid_reason_list = []


# 8. 分类列表
double_ban_list = []                        #双重禁止进场人员列表
expired_certificate_ban_list = []           #证件失效禁止进场人员列表
training_incomplete_ban_list = []           #培训未完成禁止进场人员列表
certificate_renewal_reminder_list = []      #证件续期提醒人员列表
allowed_entry_list = []             #允许进场人员列表


# 9. 逐条处理记录
for raw_record in raw_record_list:
    parts = raw_record.split(",")

    # 从这里开始写核心处理逻辑
    if len(parts) != 4:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    worker_id = parts[0].strip()
    training_status = parts[1].strip()
    certificate_status = parts[2].strip()
    remaining_days_text = parts[3].strip()

    if (
        worker_id == ""
        or training_status == ""
        or certificate_status == ""
        or remaining_days_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if training_status != "已完成" and training_status != "未完成":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("培训状态不合法, 原始记录: " + raw_record)
        continue

    if (
        certificate_status != "有效"
        and certificate_status != "即将到期"
        and certificate_status != "失效"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("证件状态不合法, 原始记录: " + raw_record)
        continue

    if not remaining_days_text.removeprefix("-").isdigit():
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("剩余天数不是合法整数, 原始记录: " + raw_record)
        continue

    remaining_days = int(remaining_days_text)

    if (
        certificate_status == "有效"
        and remaining_days <= 30
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    if (
        certificate_status == "即将到期"
        and (
            remaining_days < 0
            or remaining_days > 30
            )
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("证件状态是即将到期, 并且天数小于0或者大于30, 原始记录: " + raw_record)
        continue

    if (
        certificate_status == "失效"
        and remaining_days >= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    valid_worker_id_list.append(worker_id)
    valid_training_status_list.append(training_status)
    valid_certificate_status_list.append(certificate_status)
    valid_remaining_days_list.append(remaining_days)

    cleaned_record_list.append(
        worker_id
        + ","
        + training_status
        + ","
        + certificate_status
        + ","
        + str(remaining_days)
    )
    if training_status == "未完成" and certificate_status == "失效":
        double_ban_list.append(worker_id)
    elif training_status == "已完成" and certificate_status == "失效":
        expired_certificate_ban_list.append(worker_id)
    elif (
        training_status == "未完成"
        and (
        certificate_status == "有效"
        or certificate_status == "即将到期"
            )
    ):
        training_incomplete_ban_list.append(worker_id)
    elif training_status == "已完成" and certificate_status == "即将到期":
        certificate_renewal_reminder_list.append(worker_id)
    else:
        allowed_entry_list.append(worker_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)

double_ban_count = len(double_ban_list)
expired_certificate_ban_count = len(expired_certificate_ban_list)
training_incomplete_ban_count = len(training_incomplete_ban_list)
certificate_renewal_reminder_count = len(certificate_renewal_reminder_list)
allowed_entry_count = len(allowed_entry_list)

final_conclusion = ""
if invalid_record_count > 0:
    final_conclusion = "无效数据"
elif double_ban_count > 0:
    final_conclusion = "双重禁止进场"
elif expired_certificate_ban_count > 0:
    final_conclusion = "证件失效禁止进场"
elif training_incomplete_ban_count > 0:
    final_conclusion = "培训未完成禁止进场"
elif certificate_renewal_reminder_count > 0:
    final_conclusion = "证件续期提醒"
else:
    final_conclusion = "允许进场"

# 10. 控制台输出
print("施工现场人员进场资格核验报告")
print("=" * 32)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("双重禁止进场数量:", double_ban_count)
print("证件失效禁止进场数量:", expired_certificate_ban_count)
print("培训未完成禁止进场数量:", training_incomplete_ban_count)
print("证件续期提醒数量:", certificate_renewal_reminder_count)
print("允许进场数量:", allowed_entry_count)
print()

print("双重禁止进场人员:", double_ban_list)
print("证件失效禁止进场人员:", expired_certificate_ban_list)
print("培训未完成禁止进场人员:", training_incomplete_ban_list)
print("证件续期提醒人员:", certificate_renewal_reminder_list)
print("允许进场人员:", allowed_entry_list)
print()

print("无效记录:")
for invalid_record in invalid_record_list:
    print(invalid_record)

print()
print("无效原因:")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print()
print("最终结论:", final_conclusion)


# 11. 输出 cleaned CSV
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("人员编号,培训状态,证件状态,证件剩余有效天数\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 12. 输出 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("施工现场人员进场资格核验报告\n")
    f.write("=" * 32 + "\n")

    f.write("原始记录数量: " + str(raw_record_count) + "\n")
    f.write("有效记录数量: " + str(valid_record_count) + "\n")
    f.write("无效记录数量: " + str(invalid_record_count) + "\n\n")

    f.write("双重禁止进场数量: " + str(double_ban_count) + "\n")
    f.write(
        "证件失效禁止进场数量: "
        + str(expired_certificate_ban_count)
        + "\n"
    )
    f.write(
        "培训未完成禁止进场数量: "
        + str(training_incomplete_ban_count)
        + "\n"
    )
    f.write(
        "证件续期提醒数量: "
        + str(certificate_renewal_reminder_count)
        + "\n"
    )
    f.write("允许进场数量: " + str(allowed_entry_count) + "\n\n")

    f.write("双重禁止进场人员: " + str(double_ban_list) + "\n")
    f.write(
        "证件失效禁止进场人员: "
        + str(expired_certificate_ban_list)
        + "\n"
    )
    f.write(
        "培训未完成禁止进场人员: "
        + str(training_incomplete_ban_list)
        + "\n"
    )
    f.write(
        "证件续期提醒人员: "
        + str(certificate_renewal_reminder_list)
        + "\n"
    )
    f.write("允许进场人员: " + str(allowed_entry_list) + "\n\n")

    f.write("无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n最终结论: " + final_conclusion + "\n")