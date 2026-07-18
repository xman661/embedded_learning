###1. try/except 基本结构
try:
    num = int(input('请输入数字：'))
    print(f'你输入了：{num}')
except:
    print('你输的不是数字')

print("\n===== 分割线 =====\n")

#2. 捕获特定异常
try:
    num1 = int(input('请输入数字：'))
    result = 10 / num1
    print(f'10 ÷ {num1} = {result} ')
except ValueError:
    print('❌ 输入的不是数字')
except ZeroDivisionError:
    print('❌ 不能除以0！')

#3. else 和 finally
#else — try没有异常时才执行
#finally — 不管有没有异常都执行（用于关文件、释放资源）
try:
    f = open('data.txt','r',encoding = 'utf-8')
    context = f.read()
except FileNotFoundError:
    print('文件不存在')
else:
    print('文件读取成功')
    print(context)
finally:
    print('无论是否成功，都会执行')
    #f.close()

#4. 最推荐：with + try
try:
    with open('data.txt','r',encoding = 'utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('文件不存在，请检查路径')

print("\n===== 分割线 =====\n")

###练习1：安全除法器
def safe_divide():
    try:
        a = float(input('被除数'))
        b = float(input('除数'))
        c = a / b
    except ZeroDivisionError:
        print('❌ 不能除以0')
    except ValueError:
        print('❌ 输入的不是数字')
    else:
        print('能正常运行')
        print(c)
    finally:
        print('-----计算结束-----')

safe_divide()

print("\n===== 分割线 =====\n")

#练习2：文件读取健壮版
def read_safe(filename):
    try:
        with open(filename,'r',encoding = 'utf-8') as f:
            data = f.read()
            numbers = [int(x.strip()) for x in data.strip().split(',')]
            print(f'数字：{numbers}，总和:{sum(numbers)}')
    except FileNotFoundError:
        print(f'文件{filename}不存在')
    except ValueError:
        print(f"❌ 文件内容格式错误，需要逗号分隔的数字")












