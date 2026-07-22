# Day24 运行日志 — 函数处理数组

日期：2026-07-22

## 文件清单

| 文件 | 说明 |
|------|------|
| `example.c` | 基础示例：print_array、sum_array、max_array、average_array |
| `independent_practice.c` | 独立练习：print_array、count_even、min_array |

## 运行结果

### example.c

```
[10] [20] [30] [40] [50] 
总和：150
最大值：50
平均值：30.00
```

### independent_practice.c

```
[13] [-14] [34] [22] [29] [-29] 
偶数个数：3
最小值：-29
```

## 已掌握

| 函数 | 返回类型 | 作用 |
|------|---------|------|
| `print_array(arr, size)` | `void` | 遍历打印数组每个元素，格式 `[%d]` |
| `sum_array(arr, size)` | `int` | 累加所有元素返回总和 |
| `max_array(arr, size)` | `int` | 找最大值（从 `arr[0]` 开始比较） |
| `min_array(arr, size)` | `int` | 找最小值（与 max_array 对称） |
| `average_array(arr, size)` | `double` | 返回平均值，需要 `(double)` 强转避免整数除法 |
| `count_even(arr, size)` | `int` | 统计偶数个数（用 `% 2 == 0`） |

## 关键理解

- 数组传到函数里**退化为指针**，函数内 `sizeof(arr)` 是 8（指针大小），不是数组大小 ✅
- 因此**必须传 `size`**，函数才能知道遍历边界 ✅
- 遍历条件必须是 `i < size`，写成 `i <= size` 会越界访问 ✅
- `void` 函数只执行操作，不返回值；`int`/`double` 函数用 `return` 返回结果 ✅
- 函数定义在 `main` **上面**，参数列表用**逗号**分隔，不是分号 ✅
- `return` 要在循环**外面**，全部处理完才返回，不能在循环内部提前返回 ✅
- 数组数据只有一份，函数参数 `arr[]` 指向 `main` 中间一内存块，修改会互相影响 ✅
- `int / int` 结果为整数，要转 `double` 保留小数 ✅
