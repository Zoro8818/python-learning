raw_record_list = [
    "零件A,120,115",
    "零件B,80,90",
    "零件C,100,100",
    "零件D,60",
    "零件E,abc,50",
    " ,70,70"
]

product_name_list = []                # 有效产品名称列表
planned_quantity_list = []
completed_quantity_list = []
completion_difference_list = []       # 完成差异列表

invalid_record_list = []
invalid_reason_list = []

over_completed_product_list = []      # 超额完成产品列表
completed_as_planned_list = []        # 按计划完成产品列表
unfinished_product_list = []          # 未完成产品列表

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

print("\n最大完成差异产品：", highest_difference_product)
print("最大完成差异：", highest_completion_difference)

print("最小完成差异产品：", lowest_difference_product)
print("最小完成差异：", lowest_completion_difference)
