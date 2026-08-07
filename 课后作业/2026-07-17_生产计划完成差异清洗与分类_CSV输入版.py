# 业务目标：清洗生产计划数据，计算完成差异并按完成情况分类。
# 输入字段：产品名称、计划数量、完成数量。
# 核心计算：完成差异 = 完成数量 - 计划数量。
# 分类口径：差异大于 0 为超额完成，等于 0 为按计划完成，
#           小于 0 为未完成。
# 输出结果：有效记录 cleaned CSV、差异统计、最高最低差异和 TXT 报告。

input_file_path = r"D:\python-project\课后作业\input\production_plan.csv"
cleaned_file_path = r"D:\python-project\课后作业\output\production_plan_cleaned.csv"
report_file_path = r"D:\python-project\课后作业\output\production_plan_report.txt"

raw_record_list = []

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "产品名称,计划数量,完成数量":
        raw_record_list.append(clean_line)

product_name_list = []                # 有效产品名称列表
planned_quantity_list = []
completed_quantity_list = []
completion_difference_list = []       # 完成差异列表

invalid_record_list = []
invalid_reason_list = []

over_completed_product_list = []      # 超额完成产品列表
completed_as_planned_list = []        # 按计划完成产品列表
unfinished_product_list = []          # 未完成产品列表
cleaned_record_list = []

total_planned_quantity = 0
total_completed_quantity = 0
total_completion_difference = 0

highest_completion_difference = 0
highest_difference_product = ""

lowest_completion_difference = 0
lowest_difference_product = ""

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录：" + record)

    else:
        product_name = parts[0].strip()
        planned_quantity_text = parts[1].strip()
        completed_quantity_text = parts[2].strip()

        if (
            product_name == ""
            or planned_quantity_text == ""
            or completed_quantity_text == ""
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("字段为空，原始记录：" + record)
        elif (
            not planned_quantity_text.isdigit()
            or not completed_quantity_text.isdigit()
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("数量不是整数，原始记录：" + record)

        else:
            planned_quantity = int(planned_quantity_text)
            completed_quantity = int(completed_quantity_text)
            completion_difference = completed_quantity - planned_quantity

            product_name_list.append(product_name)
            planned_quantity_list.append(planned_quantity)
            completed_quantity_list.append(completed_quantity)
            completion_difference_list.append(completion_difference)

            if len(completion_difference_list) == 1:
                highest_completion_difference = completion_difference
                highest_difference_product = product_name

                lowest_completion_difference = completion_difference
                lowest_difference_product = product_name

            else:
                if completion_difference > highest_completion_difference:
                    highest_completion_difference = completion_difference
                    highest_difference_product = product_name

                if completion_difference < lowest_completion_difference:
                    lowest_completion_difference = completion_difference
                    lowest_difference_product = product_name

            total_planned_quantity += planned_quantity
            total_completed_quantity += completed_quantity
            total_completion_difference += completion_difference

            cleaned_record_list.append(
                product_name
                + ","
                + str(planned_quantity)
                + ","
                + str(completed_quantity)
                + ","
                + str(completion_difference)
            )

            if completion_difference > 0:
                over_completed_product_list.append(product_name)

            elif completion_difference == 0:
                completed_as_planned_list.append(product_name)

            else:
                unfinished_product_list.append(product_name)

print("原始记录数量：", len(raw_record_list))
print("有效记录数量：", len(product_name_list))
print("无效记录数量：", len(invalid_record_list))

print("\n无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print("\n无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print("\n超额完成产品：", over_completed_product_list)
print("按计划完成产品：", completed_as_planned_list)
print("未完成产品：", unfinished_product_list)

print("\n计划数量合计：", total_planned_quantity)
print("完成数量合计：", total_completed_quantity)
print("完成差异合计：", total_completion_difference)

if len(product_name_list) == 0:
    print("\n没有有效数据，无法计算最大和最小完成差异")
else:
    print("\n最大完成差异产品：", highest_difference_product)
    print("最大完成差异：", highest_completion_difference)

    print("最小完成差异产品：", lowest_difference_product)
    print("最小完成差异：", lowest_completion_difference)

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("产品名称,计划数量,完成数量,完成差异\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")

if len(invalid_record_list) > 0:
    business_conclusion = (
        "存在无效数据，当前生产完成统计仅供参考，需要修正后重新核算"
    )

elif len(cleaned_record_list) == 0:
    business_conclusion = "没有有效数据，无法进行生产计划完成分析"

elif total_completion_difference > 0:
    business_conclusion = "有效生产数据整体超额完成计划"

elif total_completion_difference == 0:
    business_conclusion = "有效生产数据整体与生产计划一致"

else:
    business_conclusion = "有效生产数据整体未达到生产计划"

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("生产计划完成差异清洗与分类报告\n")
    file.write("==============================\n")

    file.write("原始记录数量：" + str(len(raw_record_list)) + "\n")
    file.write("有效记录数量：" + str(len(cleaned_record_list)) + "\n")
    file.write("无效记录数量：" + str(len(invalid_record_list)) + "\n")

    file.write("\n分类统计\n")
    file.write("------------------------------\n")
    file.write(
        "超额完成产品数量："
        + str(len(over_completed_product_list))
        + "\n"
    )
    file.write(
        "按计划完成产品数量："
        + str(len(completed_as_planned_list))
        + "\n"
    )
    file.write(
        "未完成产品数量："
        + str(len(unfinished_product_list))
        + "\n"
    )

    file.write("\n数量合计\n")
    file.write("------------------------------\n")
    file.write("计划数量合计：" + str(total_planned_quantity) + "\n")
    file.write("完成数量合计：" + str(total_completed_quantity) + "\n")
    file.write("完成差异合计：" + str(total_completion_difference) + "\n")

    file.write("\n最大和最小完成差异\n")
    file.write("------------------------------\n")

    if len(cleaned_record_list) == 0:
        file.write("没有有效数据，无法计算最大和最小完成差异\n")
    else:
        file.write(
            "最大完成差异产品："
            + highest_difference_product
            + "，差异："
            + str(highest_completion_difference)
            + "\n"
        )

        file.write(
            "最小完成差异产品："
            + lowest_difference_product
            + "，差异："
            + str(lowest_completion_difference)
            + "\n"
        )

    file.write("\n产品分类明细\n")
    file.write("------------------------------\n")
    file.write(
        "超额完成产品："
        + str(over_completed_product_list)
        + "\n"
    )
    file.write(
        "按计划完成产品："
        + str(completed_as_planned_list)
        + "\n"
    )
    file.write(
        "未完成产品："
        + str(unfinished_product_list)
        + "\n"
    )

    file.write("\n无效数据明细\n")
    file.write("------------------------------\n")

    if len(invalid_reason_list) == 0:
        file.write("无\n")
    else:
        for invalid_reason in invalid_reason_list:
            file.write(invalid_reason + "\n")

    file.write("\n最终业务结论\n")
    file.write("------------------------------\n")
    file.write(business_conclusion + "\n")


print("\ncleaned CSV 已生成：", cleaned_file_path)
print("TXT 报告已生成：", report_file_path)
print("最终业务结论：", business_conclusion)
