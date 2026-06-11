#基本捕获语法1.9
'''
try:
    f = open('2.2(hei ma)1','r',encoding = 'utf-8')
except:
    print(f'出现了异常，因为文件不存在，我将open的模式，改为w模式去打开')
    f = open('2.2(hei ma)1', 'w', encoding='utf-8')
#捕获指定异常
try:
    print(name)
    #1/0
except NameError as e:
    print('出现了变量未定义的异常')
    print(e)           # 把异常定义为e
#捕获多个异常
try:
    1/0
    print(name)
except (NameError,ZeroDivisionError) as e:
    print('出现了变量未定义 或 除以0的异常错误')
'''
#捕获所有异常
try:
    print(1)
except Exception as e:
    print('出现了异常')
else:
    print('好高兴，没有出现异常')
print('-------------------------------------')
#finally的语法
try:
    f = open('2.2(hei ma)2','r',encoding = 'utf-8')
except Exception as e:
    print('出现了异常')
    f = open('2.2(hei ma)2', 'w', encoding='utf-8')
else:
    print('好高兴，没有出现异常')
finally:
    print('我是finally，不管出不出现异常我都要运行')
    f.close()
print('-------------------------------')
#异常的传递性
#定义一个出现异常的方法
def func1():
    print('func1 开始执行')
    num = 1 / 0
    print('func1 结束执行')
#定义一个无异常的方法，调用上面的方法

def func2():
    print('func2 开始执行')
    func1()
    print('func2 结束执行')
#定义一个方法,调用上面的方法

def main():
    try:
        func2()
    except Exception as e:
        print(f'出现异常了，异常是：{e}')

main()