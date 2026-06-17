#题目 1：找出所有偶数
num_list = [12, 55, 44, 68, 71, 64, 1, 34, 57, 91, 592]
new_list = []
for num in num_list:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)

#题目 2：找出所有大于 60 的数字
score_list = [55, 80, 72, 35, 60, 123, 54, 29, 91, 66]
new_list = []
for num in score_list:
    if num > 60:
        new_list.append(num)

print(new_list)

#题目 3：合并两个列表并去重
result_list = []
list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
new_list = list1 + list2
print(new_list)

for num in new_list:
    if num not in result_list:
        result_list.append(num)

print(result_list)



#题目 4：统计最大值、最小值、平均值
num_list = [88, 76, 92, 65, 100, 43, 59, 71]
print("最大值为: ", max(num_list))
print("最小值为: ", min(num_list))
print("平均值为: ", sum(num_list) / len(num_list))

#题目 5：把列表里的数字平方后生成新列表
#方法1
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []
for i in num_list:
    new_list.append(i**2)

print(new_list)

#方法2
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [i**2 for i in num_list]
print(new_list)


