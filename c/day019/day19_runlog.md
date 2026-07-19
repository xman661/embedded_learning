# Day19 运行日志 — 周日复盘：循环与函数

日期：2026-07-19

## 文件清单

| 文件 | 说明 |
|------|------|
| `sum_to_n.c` | 闭卷写 sum_to_n(5)=15, sum_to_n(10)=55 |
| `independent_practice.c` | sum_even_to_n() + larger() 独立练习 |

## 今日任务完成情况

### ① 闭卷写 sum_to_n(5)
- 一次通过 ✅
- 踩坑：参数名 `n` 和局部变量名冲突导致编译报错，改为 `int sum = 0` 后修复

### ② 修改 5→10
- `sum_to_n(10) = 55` ✅

### ③ 修错练习（3 个错误）
- 边界条件：`i < n` → `i <= n` ✅
- 返回值：补充 `return sum;` ✅
- 初始值：`int sum;` → `int sum = 0;` ✅
- 未初始化时输出 garbage 值 `461267438`，演示了"声明不给值就是垃圾值"的危险

### ④ 口述：for vs do-while
- `for` 适合知道循环次数；`do-while` 至少执行一次
- 若 n=0，do-while 会错误地先加 1

### ⑤ 独立练习
- `sum_even_to_n(10) = 30` ✅
- `sum_even_to_n(100) = 2550` ✅
- `larger(5, 10) = 10` ✅
- `larger(10, 5) = 10` ✅

## 运行结果

```
sum_to_n(5) = 15
sum_to_n(10) = 55
sum_even_to_n(10) = 30
sum_even_to_n(100) = 2550
larger(5, 10) = 10
larger(10, 5) = 10
```
