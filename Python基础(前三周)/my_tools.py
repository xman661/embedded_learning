def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return '不能除以0'
    return a / b
def subtract(a,b):
    return a - b

if __name__ == '__main__':
    print('测试 add(3, 5) =',add(3,5))
    print('测试 multiply(4,6) =',multiply(4,6))
    print(divide(10, 3))  # 3.333...