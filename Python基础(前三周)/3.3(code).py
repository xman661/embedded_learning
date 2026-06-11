#一、join() — 高效拼接字符串
# 错误做法：用 + 在循环里拼接（慢！）
result = ''
for s in ['Hello', 'World', 'Python']:
    result += s + ' '
    print(result)

# 正确做法：用 join()（快！）
words = ["Hello", "World", "Python"]
results = ' '.join(words)               # 用空格连接
print(results)
results = ', '.join(words)              # 用逗号+空格连接
print(results)
results =''.join(words)
print(results)                          # 直接拼一起

#二、split() 高级用法
# 基本 split
text = 'a,b,c,d,e'
print(text.split(','))
# 指定分割次数
print(text.split(',',2))
# 按换行分割
text = "第一行\n第二行\n第三行"
print(text)
print(text.split('\n'))
# splitlines() — 专门按换行分（自动处理不同换行符）
print(text.splitlines())
#三、str.format() — 旧式格式化
name = '张三'
score = 85.5
# format() 方式（f-string出现前的主流方式）
print('姓名：{},分数：{}'.format(name,score))
print('姓名：{n},分数：{s}'.format(n = name,s = score))  # 指定名字
# 控制格式
pi = 3.14159265
print('{:.2f}'.format(pi))
print('{:>10}'.format('右对齐'))
print('{:<10}'.format('左对齐'))
#四、正则表达式 re 模块
import re
# 1. re.search() — 搜索第一个匹配
text = "我的电话是138-1234-5678，邮箱是zhangsan@email.com"
phone = re.search(r'\d{3}-\d{4}-\d{4}',text)
if phone:
    print(phone.group())
# 2. re.findall() — 找所有匹配
numbers = re.findall(r'\d+',text)
print(numbers)
# 3. re.sub() — 替换
result = re.sub(r'\d{3}-\d{4}-\d{4}','***-****-****',text)
print(result)
'''
常用正则符号速查：
符号	     含义	                   例子
\d	     数字	               \d{3} = 3个数字
\w	     字母/数字/下划线	       \w+ = 一个单词
\s	     空白符（空格/Tab/换行）  \s+ = 连续空白
.	     任意字符	           a.b 匹配 a开头的3个字符
+	     1次或多次	           \d+ = 连续数字
*	     0次或多次	           \d* = 有没有数字都行
{n}	     恰好n次	               \d{11} = 11位数字
[abc]	 a/b/c中的任一个	        [0-9] 等价于 \d
^	     开头	               ^\d = 以数字开头
$	     结尾	               \d$ = 以数字结尾
'''
###练习
#练习1：提取文本中的所有数字
import re
text = "商品价格：苹果5元，香蕉3元，橘子4.5元"
number = re.findall(r'\d+\.?\d*',text)
print(number)
#练习2：邮箱格式验证
import re
def is_valid_email(email):
    pattern = r'^\w+@\w+\.\w+$'
    return re.search(pattern, email) is not None
print(is_valid_email('zhangsan@email.com'))
print(is_valid_email('1234@qqcom'))
print(is_valid_email("hello world@email.com"))




