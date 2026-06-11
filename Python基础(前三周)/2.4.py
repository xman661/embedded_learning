#一、继承 — 子类复用父类
# 父类（基类）
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f'{self.name}发出声音')

class Dog(Animal):
    def speak(self):
        print(f'{self.name}:汪汪')

class Cat(Animal):
    def speak(self):
        print(f'{self.name}:喵喵')

d = Dog('来福')
c = Cat('小花')
d.speak()
c.speak()

#二、super() — 调用父类方法
#子类的 __init__ 里用 super() 调用父类的 __init__，避免重复写父类的初始化代码。
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

    def info(self):
        print(f'{self.name},{self.age}岁,品种：{self.breed}')

d = Dog("来福", 3, "金毛")
d.info()

#三、私有属性 __ — 封装
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount >0:
            self.__balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('余额不足')

    def get_balance(self):
        return self.__balance

acc = BankAccount('niko',1000)
acc.deposit(1000)
print(acc.get_balance())
acc.withdraw(500)
print(acc.get_balance())
acc.withdraw(5000)
print(acc.get_balance())            # ❌ 报错！不能在外部直接访问私有属性
#print(acc.__balance)

#四、__str__ — 打印对象的显示
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Student({self.name},{self.age})'

s = Student('niko',32)
print(s)

#五、多态 — 同一接口不同行为
class S:
    def area(self):
        pass

class C(S):
    def __init__(self,r):
        self.r = r
    def area(self):
        return print(self.r * 3.14 * self.r)

class R(S):
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return print( self.w * self.h)

shapes =[C(5),R(4,3)]
for s in shapes:
    s.area()

###练习
#练习：Animal→Dog/Cat 继承链
'''
animals = [Dog("来福", "金毛"), Cat("小花", "橘"), Dog("旺财", "柴犬")]
'''
class Animal:
    def __init__(self,name):
        self.name = name
    def an(self):
        print(f'{self.name}发出声音')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def an(self):
        print(f'{self.name}（{self.breed}):汪汪')

    def fetch(self):
        print(f'{self.name}去捡球')

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def an(self):
        print(f'{self.name}（{self.color}):喵喵')

    def fetch(self):
        print(f'{self.name}去爬树了')

animals = [Dog('来福', "金毛"), Cat("小花", "橘"), Dog("旺财", "柴犬")]
for a in animals:
    a.an(),a.fetch()



