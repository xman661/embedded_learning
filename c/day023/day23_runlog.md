# Day23 运行日志 — 常用字符串函数与安全边界

日期：2026-07-20

## 文件清单

| 文件 | 说明 |
|------|------|
| `example.c` | 基础示例：strlen、strcpy、strcat、strcmp |
| `independent_practice.c` | 独立练习："Zhang" + "San" → "Zhang San" |

## 运行结果

### example.c

```
'first'的长度：5
copy : Hello
'first' : Hello World
字符串相同
```

### independent_practice.c

```
'full_name' : Zhang San
'full_name'的长度：9
姓名相同
```

## 已掌握

| 函数 | 作用 | 注意事项 |
|------|------|---------|
| `strlen(s)` | 返回字符串长度（不含 `\0`） | 运行时计算，格式符用 `%zu` |
| `strcpy(d, s)` | 复制字符串到目标 | 目标必须有足够空间 |
| `strcat(d, s)` | 拼接字符串到目标末尾 | 目标必须有足够空间 |
| `strcmp(a, b)` | 比较字符串内容 | 返回 0 表示相同 |

## 关键理解

- `strlen` 和 `sizeof` 不同：`strlen` 是不含 `\0` 的长度（运行时），`sizeof` 是数组总大小（编译时） ✅
- `==` 比较的是地址不是内容 ✅
- 目标数组空间不足时，strcpy/strcat 会缓冲区溢出（未定义行为） ✅
- "Hello World" 需要 12 个数组位置，`first[20]` 够用 ✅
- "Zhang San" 需要 10 个数组位置，`full_name[10]` 刚好 ✅
