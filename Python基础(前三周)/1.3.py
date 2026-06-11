#  一、if/elif/else 基础
score1=int(input('输入成绩：'))
if score1>=95:
    print('优秀')
elif score1>=95:
    print('一般')
elif score1>=60:
    print('菜逼')
else:
    print('废物')
'''
二、比较运算符
a==b
a!=b
a>b
a<b
a>=b
a<=b
'''
#三、逻辑运算符
# and — 两个都成立才为True
age=20
has_id=True
if age>=18 and has_id:
    print('可以进入')
# or — 一个成立就为True
is_weekend=True
is_holiday=False
if is_weekend or is_holiday:
    print('不用上班')
# not — 取反
is_rainy=False
if not is_rainy:
    print('不用带伞')
else:
    print('带伞')
# in — 是否在列表
fruits=['苹果','香蕉','西瓜']
if '西瓜'in fruits:
    print('有西瓜')
#练习1：正负判断
num=int(input('输入数字：'))
if num>0:
    print('正数')
elif num<0:
    print('负数')
else:
    print(0)
#练习2：成绩等级
score=int(input('输入成绩(0-100)：'))
if score>100 or score<0:
    print('成绩无效')
elif score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('E')
# 闰年规则：能被4整除但不能被100整除，或者能被400整除
is_year=int(input('输入年份：'))
if (is_year % 4 == 0 and is_year % 100 != 0) or (is_year % 400 == 0):
    print('是闰年')
else:
    print('不是闰年')
#盲打
'''
在周五下午，小明上完课离开学校，探究小明去哪了。
天气晴朗为A,下雨为B。
步行为C，乘车为D。
回家为E，去外婆家为F
'''
weather=input('输入天气情况：')
method=input('输入离校方式：')
home=input('输入目的地：')
if weather=='A':
    print('天气晴朗')
else:
    print('下雨')
if method =='C':
    print('步行')
else:
    print('乘车')
if home=='E':
        print('回家')
else:
    print('去外婆家')






















