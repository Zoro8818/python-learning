# 第 27 节小结：match...case 语句

这一节学习了 Python 3.10 版本中的新语法：`match...case`。

## 1. match...case 语法

`match...case` 可以根据某个表达式的值，匹配不同的分支并执行对应代码。

```python
match 表达式:
    case 值1:
        操作1
    case 值2 if 条件表达式:
        操作2
    case 值3 | 值4:
        操作3
    case _:
        默认操作
```

## 2. 常见写法

### 匹配固定值

```python
match num:
    case 1:
        print("星期一")
```

### 匹配固定值并添加条件

```python
match num:
    case 2 if num > 0:
        print("匹配到 2，并且满足条件")
```

### 一次匹配多个值

```python
match num:
    case 3 | 4:
        print("匹配到 3 或 4")
```

### 默认情况

```python
match num:
    case _:
        print("其他情况")
```

## 3. 应用场景

- `match...case`：适合基于某个变量的多个固定值进行分支判断，可以理解为“模式匹配”。
- `if`：适合复杂逻辑判断，例如范围比较、组合条件、多个表达式混合判断。

## 4. 注意事项

1. `match...case` 是 Python 3.10 版本中的新语法。
2. `case _:` 表示默认情况，类似 `else`。
3. `case 值3 | 值4:` 表示匹配值3或值4。
4. 如果判断涉及复杂范围、多个条件组合，优先使用 `if...elif...else` 更清楚。

## 5. 本节核心

`match...case` 适合“一个变量对应多个固定值”的分支判断；复杂条件判断仍然更适合使用 `if`。
