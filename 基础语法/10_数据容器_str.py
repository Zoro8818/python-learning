#字符串 基本操作--->不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"
print(s[4])#正向索引
print(s[-8])#反向索引

for i in s:
    print(i)


#切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])
#步长--> 正数:从前往后截取;负数:从后往前截取
print(s[-1:-7:-1])
print(s[::-1])

#案例1:邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正晚(包含一个司和至少一个.)，如果输入正确，输出”邮箱格式正确”，否则输出”邮箱格式错误”。
#1.接收用户输入的邮箱
mail = input("请输入邮箱: ")

#2.判断邮箱的格式
if mail.count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail}为邮箱格式正确")
else:
    print(f"{mail}为邮箱格式错误")


#知识限制，只支持这样表达,我懂逻辑是错误的,输入内容只要有@.就能成功.其实病不对
#方式二:in 运算符--->判断子串是否存在字符串中，存在，返回True;否则，返回False
mail = input("请输入邮箱: ")

#2.判断邮箱的格式
if mail.count("@") == 1 and "." in mail:
    print(f"{mail}为邮箱格式正确")
else:
    print(f"{mail}为邮箱格式错误")

#1.输入一个字符串，判断该字符串是否是回文(两边对称)
#黄山落叶松叶落山黄
#上海自来水来自海上
#方法1
text = input("请输入字符串:")

if text == text[::-1]:
    print("是回文")
else:
    print("不是回文")


#2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
result_list = []

for i in range(10):  #循环10次
    text = input("请输入字符串:")

    new_text = text[::-1].upper()

    result_list.append(new_text)

for item in result_list:
    print(item)
