# 第 17 节：input 输入与类型转换（阶段小结）

归档日期：2026-06-11  
课程来源：黑马程序员 Python+AI 零基础入门到大神全套视频课程  
当前掌握进度：已学到 `int()`、`str()` 和 `float()` 类型转换

## 1. 获取用户输入

使用 `input()` 获取用户输入的数据。

```python
s = input("提示信息")
```

示例：

```python
name = input("请输入你的名字：")
print(name)
```

注意：`input()` 获取到的内容默认都是字符串类型，也就是 `str`。

## 2. 类型转换：转成 int

如果用户输入的是数字，但后续需要做数学计算，就需要把字符串转换成整数。

```python
age = int(input("请输入年龄："))
print(age + 1)
```

重点：

- `int()` 可以把符合整数格式的内容转成整数。
- 如果输入内容不是合法整数，比如 `"abc"`，会报错。

## 3. 类型转换：转成 str

其他类型可以用 `str()` 转换成字符串，常用于字符串拼接或输出展示。

```python
age = 18
message = "我的年龄是：" + str(age)
print(message)
```

重点：

- 字符串和数字不能直接用 `+` 拼接。
- 数字要先用 `str()` 转成字符串。

## 4. 类型转换：转成 float

`float()` 可以将其他类型转换为浮点数，也就是小数类型。

```python
height = float(input("请输入身高："))
print(height)
```

重点：

- `float()` 常用于需要小数的场景，例如身高、体重、价格、BMI。
- 如果输入内容不是合法数字，比如 `"abc"`，会报错。

## 5. 后续待继续学习的知识点

截图中还出现了 `bool()` 类型转换函数，后续继续学习时再补充掌握：

```python
bool(...)
```

当前先记录为：

- `bool()`：其他类型转为布尔类型，通常用于真假判断。

## 6. 当前练习建议

```python
name = input("请输入姓名：")
age = int(input("请输入年龄："))
height = float(input("请输入身高："))

print("姓名：" + name)
print("年龄：" + str(age))
print("明年年龄：" + str(age + 1))
print("身高：" + str(height))
```

今日重点：先把 `input()`、`int()`、`str()`、`float()` 练熟。
