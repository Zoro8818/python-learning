# 1. 文件路径

input_file = "D:/python-project/课后作业/input/product_profit.csv"

cleaned_file = "D:/python-project/课后作业/output/product_profit_cleaned.csv"

report_file = "D:/python-project/课后作业/output/product_profit_report.txt"

# 2. 读取原始 CSV
with open(input_file, "r", encoding="utf-8") as f:
    csv_text = f.read()


# 3. 按行拆分

lines = csv_text.splitlines()

# 4. 准备列表和统计变量

raw_record_list = []

product_name_list = []          # 有效商品名称列表
purchase_amount_list = []       # 有效采购金额列表
sales_amount_list = []          # 有效销售金额列表
profit_amount_list = []         # 有效利润金额列表

profit_product_list = []        # 盈利商品列表
break_even_product_list = []    # 持平商品列表
loss_product_list = []          # 亏损商品列表

invalid_reason_list = []        # 无效原因列表
cleaned_record_list = []        # 清洗后 CSV 内容

invalid_count = 0


# 5. 清洗后 CSV 表头

cleaned_record_list.append(
    "商品名称,采购金额,销售金额,利润金额,利润分类"
)

# 第一层：只清理文件行，排除表头和空行；它们不属于业务无效数据。
for line in lines:
    clean_line = line.strip()

    if clean_line != "" and clean_line != "商品名称,采购金额,销售金额":
        raw_record_list.append(clean_line)

# 第二层：逐条处理业务记录，先校验，再保存有效数据并分类。
for record in raw_record_list:
    parts = record.split(",")

    # 必须先确认字段数量，才能安全读取 parts[0]、parts[1] 和 parts[2]。
    if len(parts) != 3:
        invalid_count += 1
        invalid_reason_list.append("字段数量错误，原始记录：" + record)

    else:
        product_name = parts[0].strip()
        purchase_amount_text = parts[1].strip()
        sales_amount_text = parts[2].strip()

        # 字段为空和金额不合法都在这里隔离，不能进入后续统计。
        if product_name == "" or purchase_amount_text == "" or sales_amount_text == "":
            invalid_count += 1
            invalid_reason_list.append("字段为空，原始记录：" + record)

        elif (
                not purchase_amount_text.replace(".", "", 1).isdigit()
                or not sales_amount_text.replace(".", "", 1).isdigit()
        ):
            invalid_count += 1
            invalid_reason_list.append("金额不是数字，原始记录：" + record)

        else:
            # 两个金额都合法后才转换、计算利润并同步保存到有效列表。
            purchase_amount = float(purchase_amount_text)
            sales_amount = float(sales_amount_text)
            profit_amount = sales_amount - purchase_amount

            product_name_list.append(product_name)
            purchase_amount_list.append(purchase_amount)
            sales_amount_list.append(sales_amount)
            profit_amount_list.append(profit_amount)

            # 先保存各分类名单，后面的数量统计直接基于这些列表。
            if profit_amount > 0:
                profit_product_list.append(product_name)

            elif profit_amount == 0:
                break_even_product_list.append(product_name)

            else:
                loss_product_list.append(product_name)

            # 为 cleaned CSV 生成当前记录的利润分类文字。
            if profit_amount > 0:
                profit_category = "盈利"

            elif profit_amount == 0:
                profit_category = "持平"

            else:
                profit_category = "亏损"

            cleaned_record_list.append(
                product_name + ","
                + str(purchase_amount) + ","
                + str(sales_amount) + ","
                + str(profit_amount) + ","
                + profit_category
            )

# 7. 根据各结果列表统一统计数量

raw_count = len(raw_record_list)
valid_count = len(product_name_list)

profit_product_count = len(profit_product_list)
break_even_product_count = len(break_even_product_list)
loss_product_count = len(loss_product_list)


# 8. 分别计算采购、销售和利润合计

total_purchase_amount = 0

for purchase_amount in purchase_amount_list:
    total_purchase_amount += purchase_amount


total_sales_amount = 0

for sales_amount in sales_amount_list:
    total_sales_amount += sales_amount


total_profit_amount = 0

for profit_amount in profit_amount_list:
    total_profit_amount += profit_amount

# 最高/最低名称和利润通过相同索引保持同步。
profit_count = len(profit_amount_list)
if profit_count > 0:
    max_profit_name = product_name_list[0]
    max_profit_amount = profit_amount_list[0]

    min_profit_name = product_name_list[0]
    min_profit_amount = profit_amount_list[0]

    for i in range(1, profit_count):
        if profit_amount_list[i] > max_profit_amount:
            max_profit_name = product_name_list[i]
            max_profit_amount = profit_amount_list[i]

        if profit_amount_list[i] < min_profit_amount:
            min_profit_name = product_name_list[i]
            min_profit_amount = profit_amount_list[i]

else:
    max_profit_name = ""
    max_profit_amount = 0
    min_profit_name = ""
    min_profit_amount = 0


# 业务结论优先提示无效数据，避免统计结果被误当成最终可用结论。
business_conclusion = ""

if invalid_count > 0:
    business_conclusion = "存在无效数据，当前利润统计仅供参考，需要修正后重新核算"

elif total_profit_amount > 0:
    business_conclusion = "有效商品整体盈利"

elif total_profit_amount == 0:
    business_conclusion = "有效商品整体持平"

else:
    business_conclusion = "有效商品整体亏损"

# 9. 输出所有有效记录的 cleaned CSV

with open(cleaned_file, "w", encoding="utf-8") as f:
    for cleaned_record in cleaned_record_list:
        f.write(cleaned_record + "\n")


# 10. 输出 TXT 统计报告和无效数据明细

with open(report_file, "w", encoding="utf-8") as f:
    f.write("商品利润数据清洗统计报告\n")
    f.write("====================\n")

    f.write("原始数据数量：" + str(raw_count) + "\n")
    f.write("有效数据数量：" + str(valid_count) + "\n")
    f.write("无效数据数量：" + str(invalid_count) + "\n")

    f.write("盈利商品数量：" + str(profit_product_count) + "\n")
    f.write("持平商品数量：" + str(break_even_product_count) + "\n")
    f.write("亏损商品数量：" + str(loss_product_count) + "\n")

    f.write("采购金额合计：" + str(total_purchase_amount) + "\n")
    f.write("销售金额合计：" + str(total_sales_amount) + "\n")
    f.write("利润金额合计：" + str(total_profit_amount) + "\n")

    f.write("最高利润商品：" + max_profit_name + "\n")
    f.write("最高利润金额：" + str(max_profit_amount) + "\n")

    f.write("最低利润商品：" + min_profit_name + "\n")
    f.write("最低利润金额：" + str(min_profit_amount) + "\n")

    f.write("\n无效数据明细：\n")

    for invalid_reason in invalid_reason_list:
        f.write(invalid_reason + "\n")

    f.write("\n业务结论：" + business_conclusion + "\n")
