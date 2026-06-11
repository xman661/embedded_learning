#一、f-string 复习
name1='小明'
score=95.5
print(f'学生:{name1},成绩:{score}')
a,b=10,20
print(f'{a}+{b}={a+b}')
print(f'圆周率={3.14159265:.2f}')
#二、字符串方法
text=' Hello World '
# 转大写
print(text.upper())
# 转小写
print(text.lower())
# 去两端空格
print(text.strip())
# 替换
print(text.replace('World','Robort'))
# 分割 → 变成列表
csv_line='张三,45,345,53'
parts=csv_line.split(',')
print(parts)
print(parts[0])
#三、len() 和 索引/切片
s ='Python'
#长度
print(len(s))
# 索引（从0开始）
print(s[0])
print(s[1])
print(s[-1])
## 切片 [起点:终点]
print(s[0:3])
print(s[2:5])
print(s[:4])
print(s[2:])
print(s[-2:])   #切片规则：[起点:终点]，包含起点，不包含终点。
#练习1：大小写转换
# 用户输入一个单词，输出大写版、小写版、首字母大写版
word=input('单词:')
print(f'大写版：{word.upper()}')
print(f'小写版:{word.lower()}')
print(f'首字母大写版:{word.capitalize()}')
#练习2：逗号分隔解析
# 输入："苹果,香蕉,橘子,西瓜"
# 输出每种水果一行
data=input('请输入水果名称，逗号分隔：')
fruits=data.split(',')
print(f'共有{len(fruits)}种水果')
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
#练习3：f-string信息卡
#用f - string格式化输出一个名片
name=input('名片:')
age=int(input('年龄:'))
city=input('城市:')
print(f'姓名:{name}')
print(f'年龄：{age}')
c=print(f'年龄：{age}')
print(f'城市：{city}')
print(type(c))