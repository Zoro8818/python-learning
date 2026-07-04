# 招投标资料检查器 A++ 标准版
# 学习定位：str + list 阶段的标准模板，用于复用资料检查业务流程。
# 说明：本文件重点展示输入 list、清洗、缺失检查、关键风险和整改建议生成。
# 当前能力范围：list + for + if + strip + append + len
# 功能：资料检查 + 关键风险判断 + 整改建议生成


# =========================
# 第 1 段：输入 list
# =========================

required_list = [
    "营业执照",
    "法人身份证",
    "授权委托书",
    "报价单",
    "项目实施方案",
    "售后服务承诺",
    "纳税证明",
    "近三年业绩证明"
]

key_required_list = [
    "营业执照",
    "法人身份证",
    "报价单",
    "项目实施方案"
]

raw_submitted_list = [
    "营业执照",
    "报价单",
    "报价单",
    "公司简介",
    "",
    " 售后服务承诺 ",
    "银行开户许可证",
    "法人身份证",
    "   ",
    "公司简介",
    "纳税证明"
]


# =========================
# 第 2 段：准备结果列表
# =========================

submitted_list = []  # 有效提交资料列表
invalid_list = []  # 无效资料列表
duplicate_list = []  # 重复提交资料列表

checked_submitted_list = []  # 已确认提交的必备资料列表
missing_list = []  # 缺失资料列表
key_missing_list = []  # 缺失的关键必备资料列表
extra_list = []  # 多余资料列表

suggestion_list = []  # 整改建议列表


# =========================
# 第 3 段：清洗原始提交资料
# raw_submitted_list → submitted_list / invalid_list / duplicate_list
# =========================

for submitted_material in raw_submitted_list:
    clean_material = submitted_material.strip()

    if clean_material == "":
        invalid_list.append(submitted_material)
    elif clean_material in submitted_list:
        duplicate_list.append(clean_material)
    else:
        submitted_list.append(clean_material)


# =========================
# 第 4 段：检查必备资料
# required_list + submitted_list → checked_submitted_list / missing_list
# =========================

for required_material in required_list:
    if required_material in submitted_list:
        checked_submitted_list.append(required_material)
    else:
        missing_list.append(required_material)


# =========================
# 第 5 段：检查关键缺失资料
# missing_list + key_required_list → key_missing_list
# =========================

for missing_material in missing_list:
    if missing_material in key_required_list:
        key_missing_list.append(missing_material)


# =========================
# 第 6 段：检查多余资料
# submitted_list + required_list → extra_list
# =========================

for submitted_material in submitted_list:
    if submitted_material not in required_list:
        extra_list.append(submitted_material)


# =========================
# 第 7 段：生成整改建议
# 根据前面的结果列表 → suggestion_list
# =========================

for missing_material in missing_list:
    suggestion_list.append("请补交必备资料：" + missing_material)

for key_missing_material in key_missing_list:
    suggestion_list.append("关键资料缺失，请优先处理：" + key_missing_material)

for extra_material in extra_list:
    suggestion_list.append("请确认是否需要保留多余资料：" + extra_material)

for duplicate_material in duplicate_list:
    suggestion_list.append("请删除重复提交资料：" + duplicate_material)

if len(invalid_list) > 0:
    suggestion_list.append("请清理空白无效资料项。")


# =========================
# 第 8 段：统一统计数量
# 列表保存结果，数量最后 len()
# =========================

submitted_count = len(checked_submitted_list)
missing_count = len(missing_list)
key_missing_count = len(key_missing_list)
extra_count = len(extra_list)
invalid_count = len(invalid_list)
duplicate_count = len(duplicate_list)
suggestion_count = len(suggestion_list)


# =========================
# 第 9 段：输出检查报告
# =========================

print("本次资料检查结果如下：")
print()

print("客户已提交的必备资料包括：", checked_submitted_list)
print("目前仍缺失资料：", missing_list)
print("缺失关键必备资料包括：", key_missing_list)
print("另发现多余资料：", extra_list)
print("无效资料包括：", invalid_list)
print("重复提交资料包括：", duplicate_list)

print("已提交必备资料数量：", submitted_count)
print("缺失资料数量：", missing_count)
print("缺失关键必备资料数量：", key_missing_count)
print("多余资料数量：", extra_count)
print("无效资料数量：", invalid_count)
print("重复提交资料数量：", duplicate_count)
print("整改建议数量：", suggestion_count)

print()
print("整改建议如下：")
print(suggestion_list)

print()
print("最终结论：")

if len(missing_list) == 0:
    print("本次必备资料已提交齐全。")
else:
    print("本次资料不齐，需要补交以下资料：", missing_list)

if len(key_missing_list) == 0:
    print("本次关键必备资料已提交齐全。")
else:
    print("缺少关键资料，风险较高：", key_missing_list)
