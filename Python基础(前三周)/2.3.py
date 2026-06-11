###一定义类和创建对象
# 定义类 — 模板
class Student:
    def __init__(self,name,score):      # 构造方法：创建对象时自动调用
        self.name = name                # # self.xxx = 实例变量（每个对象各有一份）
        self.score = score

    def print_info(self):
        print(f'学生：{self.name},成绩：{self.score}')

# 创建对象 — 根据模板造出具体实例
s1 = Student('张三',85)
s2 = Student('李四',92)

# 调用方法
s1.print_info()
s2.print_info()

#二、实例变量 vs 方法
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name}:汪汪')

    def run(self,speed):
        self.speed = speed
        print(f'{self.name}以{self.speed}速度跑')

# 使用
dog1 = Dog('来福','金毛')
dog2 = Dog('旺财','柴犬')

dog1.bark()
dog2.bark()
dog1.run('5km/h')

print(dog1.name)

###练习1：学生类
class Studen():
    def __init__(self,name,chinese,math,english):
          self.name = name
          self.math = math
          self.english = english
          self.chinese = chinese

    def total(self):
          return self.math + self.english +self.chinese

    def average(self):
          return self.total() / 3

    def print_report(self):
          print('----------------------------------------')
          print(f'姓名：{self.name}')
          print(f'语文成绩：{self.chinese}')
          print(f'数学成绩：{self.math}')
          print(f'英语成绩：{self.english}')
          print(f'总分：{self.total()}')
          print(f'平均分：{self.average():.1f}')

d1 = Studen("张三", 85, 90, 78)
d2 = Studen("李四", 92, 88, 95)
d1.print_report()
print()
d2.print_report()

print('--------------------------------------------')

#练习2：计数器类
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def show(self):
        print(f'当前计数：{self.count}')

c = Counter()
c.show()
c.increment()
c.increment()
c.increment()
c.show()
c.reset()
c.show()
