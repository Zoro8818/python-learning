"""
需求:根据输入的用户名密码执行登录操作，具体要求如下:
1. 正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666
2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空!
4.登录成功:输出"登录成功，进入B站首页~"
5.登录失败:输出"用户名或密码错误，请重新输入!"
6.关键字:
break:只能够出现在循环中，表示结束、跳出循坏的含义(break跳出循坏时，while后面的else中的代码将不会执行)
continue:只能够出现在循环中，表示中断本次循环，直接进入下一次循环
"""
#1 接收用户名和密码
users = {
    "admin": "666888",
    "zhangsan": "123456",
    "taoge": "888666",
}

while True:
    username = input("请输入正确的用户名: ")
    password = input("请输入正确的密码: ")

#2 校验:输入的用户名和密码不能为空!
    if username == "" or password == "":
        print("用户名或密码错误，请重新输入")
        continue

#3 判断用户名和密码的正确性,执行登录操作
    if username in users and users[username] == password:
        print("登录成功，进入B站首页~")
        break
    else:
        print("用户名或密码错误，请重新输入!")

#需求:用户名密码登录,正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666,5次登录机会，输入错误五次，不允许再操作了。
users = {
    "admin": "666888",
    "zhangsan": "123456",
    "taoge": "888666",
}
count = 5

while count > 0:
    username = input("请输入正确的用户名: ")
    password = input("请输入正确的密码: ")
    if username in users and users[username] == password:
        print("欢迎登录")
        break
    else:
        count -= 1
        print(f"用户名或密码错误, 请重新输入!剩余次数: {count}")
if count == 0:
    print("超过输入次数,不允许在操作")