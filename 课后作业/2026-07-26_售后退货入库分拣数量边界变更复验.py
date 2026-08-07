# 1. 文件路径
input_file = "D:/python-project/课后作业/input/after_sales_return_sorting.csv"
checked_file = "D:/python-project/课后作业/output/after_sales_return_sorting_boundary_recheck_cleaned.csv"
report_file = "D:/python-project/课后作业/output/after_sales_return_sorting_boundary_recheck_report.txt"


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
        and clean_line != "退货单号,物流状态,商品状态,原订单可退数量,申请退货数量"
    ):
        raw_record_list.append(clean_line)


# 5. 有效字段列表
valid_return_order_id_list = []
valid_logistics_status_list = []
valid_product_status_list = []
valid_returnable_quantity_list = []
valid_requested_return_quantity_list = []


# 6. 有效完整记录
cleaned_record_list = []


# 7. 无效记录和原因
invalid_record_list = []
invalid_reason_list = []


# 8. 分类列表
quantity_review_list = []                   #退货数量复核列表
logistics_rejection_follow_up_list = []     #物流拒收跟进列表
waiting_logistics_receipt_list = []         #等待物流签收列表
damage_claim_processing_list = []           #损坏索赔处理列表
pending_quality_inspection_list = []        #待质检入库列表
storable_list = []                          #可入库列表


# 9. 逐条处理记录
for raw_record in raw_record_list:
    parts = raw_record.split(",")

    # 从这里开始编写核心处理逻辑
    if len(parts) != 5:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误, 原始记录: " + raw_record)
        continue

    return_order_id = parts[0].strip()
    logistics_status = parts[1].strip()
    product_status = parts[2].strip()
    returnable_quantity_text = parts[3].strip()
    requested_return_quantity_text = parts[4].strip()

    if (
        return_order_id == ""
        or logistics_status == ""
        or product_status == ""
        or returnable_quantity_text == ""
        or requested_return_quantity_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if (
        logistics_status != "已签收"
        and logistics_status != "运输中"
        and logistics_status != "拒收"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("物流状态不合法, 原始记录: " + raw_record)
        continue

    if (
        product_status != "完好"
        and product_status != "损坏"
        and product_status != "待检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("商品状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not returnable_quantity_text.removeprefix("-").isdigit()
        or not requested_return_quantity_text.removeprefix("-").isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("原订单可退数量或申请退货数量不是合法整数, 原始记录: " + raw_record)
        continue

    returnable_quantity = int(returnable_quantity_text)
    requested_return_quantity = int(requested_return_quantity_text)

    if (
        returnable_quantity <= 0
        or requested_return_quantity <= 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("原订单可退数量或申请退货数量必须大于 0, 原始记录: " + raw_record)
        continue

    if (
        logistics_status == "运输中"
        and product_status != "待检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    if (
        logistics_status == "拒收"
        and product_status != "待检"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("无效组合, 原始记录: " + raw_record)
        continue

    valid_return_order_id_list.append(return_order_id)
    valid_logistics_status_list.append(logistics_status)
    valid_product_status_list.append(product_status)
    valid_returnable_quantity_list.append(returnable_quantity)
    valid_requested_return_quantity_list.append(requested_return_quantity)

    cleaned_record_list.append(
        return_order_id
        + ","
        + logistics_status
        + ","
        + product_status
        + ","
        + str(returnable_quantity)
        + ","
        + str(requested_return_quantity)
    )

    if requested_return_quantity >= returnable_quantity:
        quantity_review_list.append(return_order_id)
    elif logistics_status == "拒收":
        logistics_rejection_follow_up_list.append(return_order_id)
    elif logistics_status == "运输中":
        waiting_logistics_receipt_list.append(return_order_id)
    elif product_status == "损坏":
        damage_claim_processing_list.append(return_order_id)
    elif product_status == "待检":
        pending_quality_inspection_list.append(return_order_id)
    else:
        storable_list.append(return_order_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(cleaned_record_list)
invalid_record_count = len(invalid_record_list)

quantity_review_count = len(quantity_review_list)
logistics_rejection_follow_up_count = len(logistics_rejection_follow_up_list)
waiting_logistics_receipt_count = len(waiting_logistics_receipt_list)
damage_claim_processing_count = len(damage_claim_processing_list)
pending_quality_inspection_count = len(pending_quality_inspection_list)
storable_count = len(storable_list)

final_conclusion = ""
if invalid_record_count > 0:
    final_conclusion = "无效数据"
elif quantity_review_count > 0:
    final_conclusion = "退货数量复核"
elif logistics_rejection_follow_up_count > 0:
    final_conclusion = "物流拒收跟进"
elif damage_claim_processing_count > 0:
    final_conclusion = "损坏索赔处理"
elif waiting_logistics_receipt_count > 0:
    final_conclusion = "等待物流签收"
elif pending_quality_inspection_count > 0:
    final_conclusion = "待质检入库"
else:
    final_conclusion = "可入库"

# 10. 控制台输出
print("售后退货入库分拣审核报告")
print("=" * 30)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)
print()

print("退货数量复核数量:", quantity_review_count)
print("物流拒收跟进数量:", logistics_rejection_follow_up_count)
print("等待物流签收数量:", waiting_logistics_receipt_count)
print("损坏索赔处理数量:", damage_claim_processing_count)
print("待质检入库数量:", pending_quality_inspection_count)
print("可入库数量:", storable_count)
print()

print("退货数量复核退货单:", quantity_review_list)
print("物流拒收跟进退货单:", logistics_rejection_follow_up_list)
print("等待物流签收退货单:", waiting_logistics_receipt_list)
print("损坏索赔处理退货单:", damage_claim_processing_list)
print("待质检入库退货单:", pending_quality_inspection_list)
print("可入库退货单:", storable_list)
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
with open(checked_file, "w", encoding="utf-8") as f:
    f.write("退货单号,物流状态,商品状态,原订单可退数量,申请退货数量\n")

    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 12. 输出 TXT 报告
with open(report_file, "w", encoding="utf-8") as f:
    f.write("售后退货入库分拣审核报告\n")
    f.write("=" * 30 + "\n")

    f.write("原始记录数量: " + str(raw_record_count) + "\n")
    f.write("有效记录数量: " + str(valid_record_count) + "\n")
    f.write("无效记录数量: " + str(invalid_record_count) + "\n\n")

    f.write("退货数量复核数量: " + str(quantity_review_count) + "\n")
    f.write(
        "物流拒收跟进数量: "
        + str(logistics_rejection_follow_up_count)
        + "\n"
    )
    f.write(
        "等待物流签收数量: "
        + str(waiting_logistics_receipt_count)
        + "\n"
    )
    f.write(
        "损坏索赔处理数量: "
        + str(damage_claim_processing_count)
        + "\n"
    )
    f.write(
        "待质检入库数量: "
        + str(pending_quality_inspection_count)
        + "\n"
    )
    f.write("可入库数量: " + str(storable_count) + "\n\n")

    f.write("退货数量复核退货单: " + str(quantity_review_list) + "\n")
    f.write(
        "物流拒收跟进退货单: "
        + str(logistics_rejection_follow_up_list)
        + "\n"
    )
    f.write(
        "等待物流签收退货单: "
        + str(waiting_logistics_receipt_list)
        + "\n"
    )
    f.write(
        "损坏索赔处理退货单: "
        + str(damage_claim_processing_list)
        + "\n"
    )
    f.write(
        "待质检入库退货单: "
        + str(pending_quality_inspection_list)
        + "\n"
    )
    f.write("可入库退货单: " + str(storable_list) + "\n\n")

    f.write("无效记录:\n")
    for invalid_record in invalid_record_list:
        f.write(invalid_record + "\n")

    f.write("\n无效原因:\n")
    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n最终结论: " + final_conclusion + "\n")