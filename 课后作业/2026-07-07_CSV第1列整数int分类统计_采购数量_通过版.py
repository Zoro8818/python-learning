# 第 1 块：路径设置
input_file = "D:/python-project/课后作业/input/purchase_quantity.csv"
cleaned_file = "D:/python-project/课后作业/output/purchase_quantity_cleaned.csv"
summary_file = "D:/python-project/课后作业/output/purchase_quantity_summary.txt"


# 第 2 块：读取 csv 文本
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


# 第 3 块：按行拆分
lines = text.splitlines()


# 第 4 块：去掉表头，保留真正的数据行
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "采购数量,物料名称,供应商名称":
        raw_record_list.append(clean_line)


# 第 5 块：准备结果变量
valid_purchase_quantity_list = []
valid_material_name_list = []
valid_supplier_name_list = []

invalid_count = 0
total_purchase_quantity = 0
large_purchase_count = 0
normal_purchase_count = 0
zero_purchase_count = 0


# 第 6 块：循环处理每一条采购记录
for record in raw_record_list:
    parts = record.split(",")

    if len(parts) != 3:
        invalid_count += 1
    else:
        purchase_quantity_text = parts[0].strip()
        material_name = parts[1].strip()
        supplier_name = parts[2].strip()

        if purchase_quantity_text == "" or material_name == "":
            invalid_count += 1
        elif purchase_quantity_text.isdigit():
            purchase_quantity = int(purchase_quantity_text)

            valid_purchase_quantity_list.append(purchase_quantity)
            valid_material_name_list.append(material_name)
            valid_supplier_name_list.append(supplier_name)
            total_purchase_quantity += purchase_quantity

            if purchase_quantity >= 100:
                large_purchase_count += 1
            elif purchase_quantity > 0:
                normal_purchase_count += 1
            else:
                zero_purchase_count += 1
        else:
            invalid_count += 1


# 第 7 块：统计数量和平均采购数量
raw_count = len(raw_record_list)
valid_count = len(valid_purchase_quantity_list)

if valid_count > 0:
    avg_purchase_quantity = total_purchase_quantity / valid_count

else:
    avg_purchase_quantity = 0

# 第 8 块：写入 cleaned csv
with open(cleaned_file, "w", encoding="gbk") as f:
    f.write("采购数量,物料名称,供应商名称\n")

    for i in range(valid_count):
        f.write(
            str(valid_purchase_quantity_list[i])
            + ","
            + valid_material_name_list[i]
            + ","
            + valid_supplier_name_list[i]
            + "\n"
        )

# 第 9 块：写入 summary txt
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("采购数量清洗统计报告\n")
    f.write("====================\n")
    f.write("原始记录数量：" + str(raw_count) + "\n")
    f.write("有效记录数量：" + str(valid_count) + "\n")
    f.write("无效记录数量：" + str(invalid_count) + "\n")
    f.write("总采购数量：" + str(total_purchase_quantity) + "\n")
    f.write("平均采购数量：" + str(round(avg_purchase_quantity, 2)) + "\n")
    f.write("大批量采购数量：" + str(large_purchase_count) + "\n")
    f.write("普通采购数量：" + str(normal_purchase_count) + "\n")
    f.write("零采购数量：" + str(zero_purchase_count) + "\n")
