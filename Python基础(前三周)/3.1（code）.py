class Student:
    school = '南昌理工学院'

    def __init__(self,name):
        self.name =name

s1 = Student('张三')
s2 = Student('李四')
print(s1.school)
print(s2.school)


#2. @classmethod — 不创建对象也能调用的方法
class Utils:
    @classmethod
    def version(cls):
        return 'v1.0'
print(Utils.version())

#3. @property — 像属性一样使用方法（可加校验）
class Student:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if len(value) > 1:
            self._name = value
        else:
            print('名字太短')

s = Student('张三')
print(s.name)
s.name = '李'

#BankAccount
class BankAccount:
    bank_name = '中国银行'
    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance


    def deposit(self,amount):
        if amount >0:
            self._balance += amount
        else:
            print('金额必须大于0')

    def withdraw(self,amount):
        if 0 <amount <= self._balance:
            self._balance -= amount
        else:
            print('不能超余额')

acc = BankAccount("张三", 1000)
print(acc.balance)      # 1000
acc.deposit(500)
print(acc.balance)      # 1500
acc.withdraw(200)
print(acc.balance)      # 1300
acc.withdraw(2000)      # 不能超余额





