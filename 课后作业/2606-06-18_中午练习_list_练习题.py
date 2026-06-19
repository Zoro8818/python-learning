# 第 1 题：统计列表长度和总和
num_list = [10, 20, 30, 40, 50]

len_list = len(num_list)
total = sum(num_list)

print("列表长度:", len_list)
print("数字总和:", total)


# 第 2 题：找出列表中的最大值和最小值
score_list = [88, 59, 76, 92, 45, 100, 67]

max_score = max(score_list)
min_score = min(score_list)

print("最高分:", max_score)
print("最低分:", min_score)


# 第 3 题：统计及格人数
score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71]

count = 0

for score in score_list:
    if score >= 60:
        count += 1

print("及格人数:", count)


# 第 4 题：把不及格成绩放进新列表
score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71]

fail_list = []

for score in score_list:
    if score < 60:
        fail_list.append(score)

print("不及格成绩:", fail_list)


# 第 5 题：统计优秀、及格、不及格人数
score_list = [88, 59, 76, 92, 45, 100, 67, 83, 30, 71, 60, 85]

excellent_count = 0
pass_count = 0
fail_count = 0

for score in score_list:
    if score >= 85:
        excellent_count += 1
    elif score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("优秀人数:", excellent_count)
print("及格人数:", pass_count)
print("不及格人数:", fail_count)