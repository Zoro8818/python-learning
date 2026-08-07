input_file = "D:/python-project/课后作业/input/sales_order_inventory_quality_release_review.csv"

cleaned_file = "D:/python-project/课后作业/output/sales_order_inventory_quality_release_review_cleaned.csv"

report_file = "D:/python-project/课后作业/output/sales_order_inventory_quality_release_review_report.txt"


with open(input_file, "r", encoding="utf-8") as file:
    csv_text = file.read()


lines = csv_text.splitlines()


# 原始记录列表
raw_record_list = []

for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "订单编号,订单确认状态,库存锁定状态,质检状态,申请数量,实际分配数量":
        raw_record_list.append(clean_line)


# 有效、无效记录
valid_record_list = []
invalid_record_list = []
invalid_reason_list = []


# 有效记录分类
allocation_quantity_review_list = []       # 分配数量复核
waiting_order_confirmation_list = []       # 等待订单确认
waiting_inventory_lock_list = []           # 等待库存锁定
waiting_inventory_allocation_list = []     # 等待库存分配
waiting_quality_inspection_list = []       # 等待质检
quality_isolation_list = []                # 质量隔离
allowed_shipping_list = []                 # 允许发货


for raw_record in raw_record_list:

    fields = raw_record.split(",")

    # 1. 字段数量检查
    if len(fields) != 6:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段数量错误，原始记录：" + raw_record)
        continue


    # 字段清洗
    order_id = fields[0].strip()
    order_confirmation_status = fields[1].strip()
    inventory_lock_status = fields[2].strip()
    quality_inspection_status = fields[3].strip()
    requested_quantity_text = fields[4].strip()
    allocated_quantity_text = fields[5].strip()


    # 从这里开始写核心无效判断和分类逻辑
    if (
        order_id == ""
        or order_confirmation_status == ""
        or inventory_lock_status == ""
        or quality_inspection_status == ""
        or requested_quantity_text == ""
        or allocated_quantity_text == ""
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("字段为空, 原始记录: " + raw_record)
        continue

    if order_confirmation_status != "已确认" and order_confirmation_status != "未确认":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("订单确认状态不合法, 原始记录: " + raw_record)
        continue

    if inventory_lock_status != "已锁定" and inventory_lock_status != "未锁定":
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("库存锁定状态不合法, 原始记录: " + raw_record)
        continue

    if (
        quality_inspection_status != "合格"
        and quality_inspection_status != "待检"
        and quality_inspection_status != "不合格"
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("质检状态不合法, 原始记录: " + raw_record)
        continue

    if (
        not requested_quantity_text.removeprefix("-").isdigit()
        or not allocated_quantity_text.removeprefix("-").isdigit()
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("申请数量或实际分配数量不合法, 原始记录: " + raw_record)
        continue

    requested_quantity = int(requested_quantity_text)
    allocated_quantity = int(allocated_quantity_text)

    if requested_quantity < 1 or requested_quantity > 5000:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("申请数量必须是1—5000 的整数, 原始记录: " + raw_record)
        continue

    if allocated_quantity < 0 or allocated_quantity > 5000:
        invalid_record_list.append(raw_record)
        invalid_reason_list.append("实际分配数量必须是0—5000 的整数, 原始记录: " + raw_record)
        continue

    if order_confirmation_status == "未确认":

        if (
            inventory_lock_status != "未锁定"
            or quality_inspection_status != "待检"
        ):
            invalid_record_list.append(raw_record)
            invalid_reason_list.append("状态组合不合理, 原始记录: " + raw_record)
            continue

    elif order_confirmation_status == "已确认":

        if (
            inventory_lock_status == "未锁定"
            and quality_inspection_status != "待检"
        ):
            invalid_record_list.append(raw_record)
            invalid_reason_list.append("状态组合不合理, 原始记录: " + raw_record)
            continue


    if (
            order_confirmation_status == "未确认"
            and allocated_quantity != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "未确认订单的实际分配数量必须等于0, 原始记录: " + raw_record
        )
        continue

    elif (
            order_confirmation_status == "已确认"
            and inventory_lock_status == "未锁定"
            and allocated_quantity != 0
    ):
        invalid_record_list.append(raw_record)
        invalid_reason_list.append(
            "未锁定订单的实际分配数量必须等于0, 原始记录: " + raw_record
        )
        continue

    clean_record = (
        order_id
        + ","
        + order_confirmation_status
        + ","
        + inventory_lock_status
        + ","
        + quality_inspection_status
        + ","
        + str(requested_quantity)
        + ","
        + str(allocated_quantity)
    )

    valid_record_list.append(clean_record)

    if allocated_quantity > requested_quantity:
        allocation_quantity_review_list.append(order_id)
    elif (
        order_confirmation_status == "未确认"
        and inventory_lock_status == "未锁定"
        and quality_inspection_status == "待检"
        and allocated_quantity == 0
    ):
        waiting_order_confirmation_list.append(order_id)
    elif (
        order_confirmation_status == "已确认"
        and inventory_lock_status == "未锁定"
        and quality_inspection_status == "待检"
        and allocated_quantity == 0
    ):
        waiting_inventory_lock_list.append(order_id)
    elif (
        order_confirmation_status == "已确认"
        and inventory_lock_status == "已锁定"
        and allocated_quantity == 0
    ):
        waiting_inventory_allocation_list.append(order_id)
    elif (
        order_confirmation_status == "已确认"
        and inventory_lock_status == "已锁定"
        and quality_inspection_status == "待检"
        and allocated_quantity > 0
    ):
        waiting_quality_inspection_list.append(order_id)
    elif (
        order_confirmation_status == "已确认"
        and inventory_lock_status == "已锁定"
        and quality_inspection_status == "不合格"
        and allocated_quantity > 0
    ):
        quality_isolation_list.append(order_id)
    else:
        allowed_shipping_list.append(order_id)

raw_record_count = len(raw_record_list)
valid_record_count = len(valid_record_list)
invalid_record_count = len(invalid_record_list)

allocation_quantity_review_count = len(allocation_quantity_review_list)
waiting_order_confirmation_count = len(waiting_order_confirmation_list)
waiting_inventory_lock_count = len(waiting_inventory_lock_list)
waiting_inventory_allocation_count = len(waiting_inventory_allocation_list)
waiting_quality_inspection_count = len(waiting_quality_inspection_list)
quality_isolation_count = len(quality_isolation_list)
allowed_shipping_count = len(allowed_shipping_list)

review_conclusion = ""

if invalid_record_count > 0:
    review_conclusion = "当前审核结果仅供参考，需要修正无效数据后重新审核"
elif allocation_quantity_review_count > 0:
    review_conclusion = "存在超申请数量分配，需要完成数量复核后再放行"
elif quality_isolation_count > 0:
    review_conclusion = "存在质检不合格订单，需要隔离处理"
elif (
    waiting_order_confirmation_count > 0
    or waiting_inventory_lock_count > 0
    or waiting_inventory_allocation_count > 0
    or waiting_quality_inspection_count > 0
):
    review_conclusion = "部分订单尚未完成确认、锁库、分配或质检"
else:
    review_conclusion = "当前订单满足发货放行条件"

# 控制台输出

print("销售订单锁库与质量放行审核报告")
print("=" * 40)

print("原始记录数量:", raw_record_count)
print("有效记录数量:", valid_record_count)
print("无效记录数量:", invalid_record_count)

print()

print("分配数量复核数量:", allocation_quantity_review_count)
print("等待订单确认数量:", waiting_order_confirmation_count)
print("等待库存锁定数量:", waiting_inventory_lock_count)
print("等待库存分配数量:", waiting_inventory_allocation_count)
print("等待质检数量:", waiting_quality_inspection_count)
print("质量隔离数量:", quality_isolation_count)
print("允许发货数量:", allowed_shipping_count)

print()

print("分配数量复核订单:", allocation_quantity_review_list)
print("等待订单确认订单:", waiting_order_confirmation_list)
print("等待库存锁定订单:", waiting_inventory_lock_list)
print("等待库存分配订单:", waiting_inventory_allocation_list)
print("等待质检订单:", waiting_quality_inspection_list)
print("质量隔离订单:", quality_isolation_list)
print("允许发货订单:", allowed_shipping_list)

print()

print("最终审核结论:")
print(review_conclusion)

print()

print("无效记录:")

for invalid_reason in invalid_reason_list:
    print(invalid_reason)


# 写入 cleaned CSV

with open(cleaned_file, "w", encoding="utf-8") as file:

    file.write(
        "订单编号,订单确认状态,库存锁定状态,质检状态,申请数量,实际分配数量\n"
    )

    for valid_record in valid_record_list:
        file.write(valid_record + "\n")


# 写入 TXT 报告

with open(report_file, "w", encoding="utf-8") as file:

    file.write("销售订单锁库与质量放行审核报告\n")
    file.write("=" * 40 + "\n")

    file.write("原始记录数量: " + str(raw_record_count) + "\n")
    file.write("有效记录数量: " + str(valid_record_count) + "\n")
    file.write("无效记录数量: " + str(invalid_record_count) + "\n")

    file.write("\n")

    file.write(
        "分配数量复核数量: "
        + str(allocation_quantity_review_count)
        + "\n"
    )

    file.write(
        "等待订单确认数量: "
        + str(waiting_order_confirmation_count)
        + "\n"
    )

    file.write(
        "等待库存锁定数量: "
        + str(waiting_inventory_lock_count)
        + "\n"
    )

    file.write(
        "等待库存分配数量: "
        + str(waiting_inventory_allocation_count)
        + "\n"
    )

    file.write(
        "等待质检数量: "
        + str(waiting_quality_inspection_count)
        + "\n"
    )

    file.write(
        "质量隔离数量: "
        + str(quality_isolation_count)
        + "\n"
    )

    file.write(
        "允许发货数量: "
        + str(allowed_shipping_count)
        + "\n"
    )

    file.write("\n")

    file.write(
        "分配数量复核订单: "
        + str(allocation_quantity_review_list)
        + "\n"
    )

    file.write(
        "等待订单确认订单: "
        + str(waiting_order_confirmation_list)
        + "\n"
    )

    file.write(
        "等待库存锁定订单: "
        + str(waiting_inventory_lock_list)
        + "\n"
    )

    file.write(
        "等待库存分配订单: "
        + str(waiting_inventory_allocation_list)
        + "\n"
    )

    file.write(
        "等待质检订单: "
        + str(waiting_quality_inspection_list)
        + "\n"
    )

    file.write(
        "质量隔离订单: "
        + str(quality_isolation_list)
        + "\n"
    )

    file.write(
        "允许发货订单: "
        + str(allowed_shipping_list)
        + "\n"
    )

    file.write("\n")

    file.write("最终审核结论:\n")
    file.write(review_conclusion + "\n")

    file.write("\n")

    file.write("无效记录:\n")

    for invalid_reason in invalid_reason_list:
        file.write(invalid_reason + "\n")