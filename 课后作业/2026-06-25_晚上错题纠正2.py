high_amount_list = [120.5, 300.0, 150.0]
high_total_amount = 570.5

normal_amount_list = [80.0, 55.0, 99.9]
normal_total_amount = 234.9

low_amount_list = [35.5, 0.0, 18.8, 12.0, 45.0]
low_total_amount = 111.3

if len(high_amount_list) > 0:
    high_avg_amount = high_total_amount / len(high_amount_list)
else:
    high_avg_amount = 0

if len(normal_amount_list) > 0:
    normal_avg_amount = normal_total_amount / len(normal_amount_list)
else:
    normal_avg_amount = 0

if len(low_amount_list) > 0:
    low_avg_amount = low_total_amount / len(low_amount_list)
else:
    low_avg_amount = 0

print("高销售额平均金额:", round(high_avg_amount, 2))
print("普通销售额平均金额:", round(normal_avg_amount, 2))
print("低销售额平均金额:", round(low_avg_amount, 2))

