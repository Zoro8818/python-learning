# 第31节 range语句

## 本节主题
学习 `range()` 语句的作用和常见用法。`range()` 经常和 `for` 循环配合使用，用来生成指定规则的数字序列。

## 1. range() 语句的作用

`range()` 的作用是：生成指定规则的数字序列。

它不会一次性写出所有数字，而是按照给定规则生成一个可以被遍历的数字范围。

## 2. range() 的三种常见用法

### 1. range(end)

```python
range(end)
```

含义：从 `0` 开始，到 `end` 结束，但不包含 `end`。

示例：
```python
for i in range(5):
    print(i)
```

输出：
```text
0
1
2
3
4
```

说明：`range(5)` 生成的是 `0, 1, 2, 3, 4`，不包含 `5`。

### 2. range(start, end)

```python
range(start, end)
```

含义：从 `start` 开始，到 `end` 结束，但不包含 `end`。

示例：
```python
for i in range(2, 6):
    print(i)
```

输出：
```text
2
3
4
5
```

说明：`range(2, 6)` 从 `2` 开始，到 `6` 前一个数字结束。

### 3. range(start, end, step)

```python
range(start, end, step)
```

含义：从 `start` 开始，到 `end` 结束，但不包含 `end`，每次按 `step` 指定的步长变化。

示例：
```python
for i in range(1, 10, 2):
    print(i)
```

输出：
```text
1
3
5
7
9
```

说明：`range(1, 10, 2)` 从 `1` 开始，每次增加 `2`，到 `10` 之前停止。

## 3. 注意事项

- `range()` 生成的数字序列默认从 `0` 开始。
- 结束值 `end` 不会被包含在结果中。
- `step` 表示步长，默认是 `1`。
- `range()` 常用于控制 `for` 循环的次数。

## 4. 本节核心

`range()` 用来生成有规律的数字序列。记住一个重点：`range()` 包含开始值，不包含结束值。
