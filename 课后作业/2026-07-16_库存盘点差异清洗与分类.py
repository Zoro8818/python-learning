# 库存盘点差异清洗与分类
# 库存盘点差异清洗、分类、统计及文件输出

input_file_path = r"D:\python-project\课后作业\input\inventory_check.csv"
cleaned_file_path = r"D:\python-project\课后作业\output\inventory_check_cleaned.csv"
report_file_path = r"D:\python-project\课后作业\output\inventory_check_report.txt"

raw_record_list = []

invalid_record_list = []
invalid_reason_list = []
product_name_list = []
book_inventory_list = []
actual_inventory_list = []
inventory_difference_list = []

cleaned_record_list = []

surplus_product_list = []
matched_product_list = []
shortage_product_list = []

highest_inventory_difference = 0
highest_difference_product = ""

lowest_inventory_difference = 0
lowest_difference_product = ""

total_book_inventory = 0
total_actual_inventory = 0
total_inventory_difference = 0

# 第1块：读取 CSV

with open(input_file_path, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()


# 第2块：第一个循环
# 排除空行和表头，保存真实业务记录

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "商品名称,账面库存,实盘库存":
        raw_record_list.append(clean_line)



# 第3块：第二个循环
# parts[0] → 商品名称
# parts[1] → 账面库存文字
# parts[2] → 实盘库存文字
#
# 顺序：
# 1. split(",")
# 2. 判断字段数量
# 3. strip() 清洗三个字段
# 4. 判断空字段
# 5. 判断两个库存是不是数字
# 6. 保存无效记录和无效原因
# 7. 合法库存转 int 并计算库存差异
# 8. 保存有效数据、累计库存、同步最大最小
# 9. 按盘盈、账实一致、盘亏分类

for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_record_list.append(record)
        invalid_reason_list.append("字段数量错误，原始记录：" + record)
    else:
        product_name = parts[0].strip()
        book_inventory_text = parts[1].strip()
        actual_inventory_text = parts[2].strip()

        if (
            product_name == ""
            or book_inventory_text == ""
            or actual_inventory_text == ""
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("字段为空，原始记录：" + record)
        elif (
            not book_inventory_text.isdigit()
            or not actual_inventory_text.isdigit()
        ):
            invalid_record_list.append(record)
            invalid_reason_list.append("库存不是数字，原始记录：" + record)

        else:
            book_inventory = int(book_inventory_text)
            actual_inventory = int(actual_inventory_text)

            inventory_difference = actual_inventory - book_inventory

            product_name_list.append(product_name)
            book_inventory_list.append(book_inventory)
            actual_inventory_list.append(actual_inventory)
            inventory_difference_list.append(inventory_difference)

            if len(inventory_difference_list) == 1:
                highest_inventory_difference = inventory_difference
                highest_difference_product = product_name

                lowest_inventory_difference = inventory_difference
                lowest_difference_product = product_name

            else:
                if inventory_difference > highest_inventory_difference:
                    highest_inventory_difference = inventory_difference
                    highest_difference_product = product_name

                if inventory_difference < lowest_inventory_difference:
                    lowest_inventory_difference = inventory_difference
                    lowest_difference_product = product_name

            total_book_inventory += book_inventory
            total_actual_inventory += actual_inventory
            total_inventory_difference += inventory_difference

            cleaned_record_list.append(
                product_name
                + ","
                + str(book_inventory)
                + ","
                + str(actual_inventory)
                + ","
                + str(inventory_difference)
            )

            if inventory_difference > 0:
                surplus_product_list.append(product_name)
            elif inventory_difference == 0:
                matched_product_list.append(product_name)
            else:
                shortage_product_list.append(product_name)



# 第4块：控制台检查输出

print("原始业务记录数量：", len(raw_record_list))
print("无效记录数量：", len(invalid_record_list))

print("\n无效记录：")
for invalid_record in invalid_record_list:
    print(invalid_record)

print("\n无效原因：")
for invalid_reason in invalid_reason_list:
    print(invalid_reason)

print("\n有效记录数量：", len(cleaned_record_list))

print("盘盈商品数量：", len(surplus_product_list))
print("账实一致商品数量：", len(matched_product_list))
print("盘亏商品数量：", len(shortage_product_list))

print("\n盘盈商品：", surplus_product_list)
print("账实一致商品：", matched_product_list)
print("盘亏商品：", shortage_product_list)

print("\n账面库存合计：", total_book_inventory)
print("实盘库存合计：", total_actual_inventory)
print("库存差异合计：", total_inventory_difference)

print("\n清洗后的有效记录：")
for cleaned_record in cleaned_record_list:
    print(cleaned_record)

if len(cleaned_record_list) == 0:
    print("\n没有有效数据，无法计算最大和最小库存差异")

else:
    print("\n最大库存差异商品：", highest_difference_product)
    print("最大库存差异：", highest_inventory_difference)

    print("最小库存差异商品：", lowest_difference_product)
    print("最小库存差异：", lowest_inventory_difference)

if len(invalid_record_list) > 0:
    business_conclusion = "存在无效数据，当前库存盘点统计仅供参考，需要修正后重新核算"

elif len(cleaned_record_list) == 0:
    business_conclusion = "没有有效数据，无法进行库存盘点核算"

elif total_inventory_difference > 0:
    business_conclusion = "有效商品整体存在盘盈"

elif total_inventory_difference == 0:
    business_conclusion = "有效商品账面库存与实盘库存总量一致"

else:
    business_conclusion = "有效商品整体存在盘亏"

with open(cleaned_file_path, "w", encoding="gbk") as file:
    file.write("商品名称,账面库存,实盘库存,库存差异\n")

    for cleaned_record in cleaned_record_list:
        file.write(cleaned_record + "\n")

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("库存盘点差异清洗与分类报告\n")
    file.write("==============================\n")

    file.write("原始业务记录数量：" + str(len(raw_record_list)) + "\n")
    file.write("有效记录数量：" + str(len(cleaned_record_list)) + "\n")
    file.write("无效记录数量：" + str(len(invalid_record_list)) + "\n")

    file.write("\n分类统计\n")
    file.write("------------------------------\n")
    file.write("盘盈商品数量：" + str(len(surplus_product_list)) + "\n")
    file.write("账实一致商品数量：" + str(len(matched_product_list)) + "\n")
    file.write("盘亏商品数量：" + str(len(shortage_product_list)) + "\n")

    file.write("\n库存合计\n")
    file.write("------------------------------\n")
    file.write("账面库存合计：" + str(total_book_inventory) + "\n")
    file.write("实盘库存合计：" + str(total_actual_inventory) + "\n")
    file.write("库存差异合计：" + str(total_inventory_difference) + "\n")

    file.write("\n最大和最小库存差异\n")
    file.write("------------------------------\n")

    if len(cleaned_record_list) == 0:
        file.write("没有有效数据，无法计算最大和最小库存差异\n")

    else:
        file.write(
            "最大库存差异商品："
            + highest_difference_product
            + "，差异："
            + str(highest_inventory_difference)
            + "\n"
        )

        file.write(
            "最小库存差异商品："
            + lowest_difference_product
            + "，差异："
            + str(lowest_inventory_difference)
            + "\n"
        )

    file.write("\n商品分类明细\n")
    file.write("------------------------------\n")
    file.write("盘盈商品：" + str(surplus_product_list) + "\n")
    file.write("账实一致商品：" + str(matched_product_list) + "\n")
    file.write("盘亏商品：" + str(shortage_product_list) + "\n")

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
