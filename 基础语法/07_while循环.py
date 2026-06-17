# i = 0
# while i < 10:
#     print("人生苦短, 我玩魔兽")
#     i += 1
# else:
#     print("循环正常结束")


#案例1 求1~100所有偶数之和
total = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

print(f"1~100所有偶数之和为: {total}")