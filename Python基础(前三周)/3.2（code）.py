#一、列表推导式 — 用一行代替 for 循环
# 老方法：for循环
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

# 列表推导式：一行搞定
square = [i * i for i in range(10)]
print(square)
#格式：[表达式 for 变量 in 可迭代对象]

#二、带条件的列表推导式
# 只保留偶数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [n for n in nums if n % 2 == 0]
print(evens)

# 对数据做转换
temps_c = [0,10,20,30,40]
temps_f = [c * 9 / 5 + 32 for c in temps_c]
print(temps_f)

#三、字典推导式
# 字典推导式
names = ['张三','李四','niko']
score_dict = {name: 0 for name in names}
print(score_dict)

# 实际场景：从两个列表合成字典
students = ['张三','李四','niko']
score = [85, 92, 78]
result ={students[i] : score[i] for i in range(len(students))}
print(result)

#四、常用内置函数
#enumerate() — 遍历时带索引
fruits = ["苹果", "香蕉", "橘子"]
for i,fruits in enumerate(fruits):
    print(f'{i+1}.{fruits}')

#zip() — 把两个列表"拉链"到一起
names = ['张三','李四','niko']
scores = [85, 92, 78]
for name,score in zip(names,scores):
    print(f'{name}:{score}分')

# zip 成字典
info = dict(zip(names,scores))
print(info)

#map() — 统一转换
num = [1, 2, 3, 4, 5,6]
doubled =list(map(lambda x: x*2,num))    #注：lambda x: x * 2 就是匿名函数，等价于 def double(x): return x * 2，只是写在一行。
print(doubled)
doubleds =[i * 2 for i in num]
print(doubleds)

#filter() — 过滤
evens = list(filter(lambda x: x % 2 == 0, num))
print(evens)
even = [n for n in num if n % 2 ==0]
print(even)
#练习1：用推导式完成数据过滤
# 有一组温度数据，从中找出0°C以下的天数
temperatures = [12, -3, 5, -1, 8, -7, 3, 0, -2, 6]
temperature = list(filter(lambda x: x < 0 , temperatures))
print(temperature)
temperaturess = [i for i in temperatures if i <0]
print(temperaturess)

#练习2：用 zip 合并两个列表
# 用 zip 把课程名和成绩对应起来，打印每门课的成绩
subjects = ["语文", "数学", "英语", "物理"]
scores = [85, 92, 78, 88]
for sub,score in zip(subjects, scores):
    print(f'{sub}:{score}')

#练习3：推导式进阶
# 请用一行列表推导式完成：
# 1. 找出1-50中能被3或5整除的数
# 2. 把这些数乘以2
result = [i * 2 for i in range(1,51) if i % 3 ==0 or i % 5 ==0]
print(result)