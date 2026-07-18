###第一部分：函数
#关键点： return 终止函数、参数默认值的陷阱、函数的复用思想
#1. 定义和调用函数
def greet(name):
    print(f'你好{name}')
greet('小明')                # 调用
#2. return — 返回值
def add(a, b):
    return a + b
    print('这行不会执行')   # return 之后函数就结束了
result = add(3,4)   # result = 7
print(result)     #return 会立即终止函数，后面的代码不执行。没有 return 的函数返回 None。
#3. 参数默认值（注意陷阱！）
# 正确用法
def power(base,exp=2):
    return base ** exp
print(power(3))             # 9（3²）
print(power(2,3)) # 8
# ⚠️ 陷阱：默认参数不要用可变对象（列表/字典）
def ad_student(name,student=[]):
    student.append(name)
    return student
print(ad_student("张三"))  # ['张三']
print(ad_student("李四"))  # ['张三', '李四']  — 两次用了同一个列表！
# ✅ 正确写法
def add_student(name,studens=None):
    if studens is None:
        students = []
        students.append(name)
        return students
print(add_student('张三'))
print(add_student('李四'))
###4. 练习：
# 练习1：判断素数
def a(n):
    if n < 2:
        return False
    for c in range(2,n):
        if n % c ==0:
            return False
    return True
# 练习2：斐波那契数列
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a,end='')
        a, b = b, a +b
fibonacci(5)
# 练习3：四则运算计算器
def calc(a,b,op):
    if op == '+':
        return a + b
    if op == '-':
        return a-b
    if op == '*':
        return a * b
    if op == '/':
        if b != 0:
            return a / b
    else:
        return('除数不能为0')

