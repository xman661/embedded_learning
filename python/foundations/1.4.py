###一、for 循环
fruits =['苹果','香蕉','西瓜','梨子']
for f in fruits:
    print(f)
# 遍历字符串
for ch in 'Python':
    print(ch)
# range(stop)      — 0 到 stop-1
A=range(1,5)
print(list(A))
A=range(5)
print(A)
for i in range(5):
    print(i)
# range(start, stop) — start 到 stop-1
for e in range(2,5):
    print(e)
# range(start, stop, step) — 带步长
for m in range(1,10,2):
    print(m)
#三、while 循环
count = 0
while count < 5:
    print(count)
    count += 1
#四、break 和 continue
# break — 立即终止整个循环
for x in range(10):
    if x == 5:
        break
    print(x)
# continue — 跳过当前这次，继续下一次
for m in range(-2,4):
    if m ==-1:
        continue
    print(m)
###练习1：整除打印
# 打印1-100中所有能被3整除的数
for a in range(1,101):
    if a %3 !=0:
        continue
    print(a,end=' ')
print( )
for b in range(1,101):
    if b %3 ==0:
     print(b,end=' ')
print( )
#练习2：阶乘计算
c =int(input('输入整数：'))
d=1
for g in range(1,c+1):
    d *= g
print(f'{c}! = {d}')
#练习3：猜数字游戏
import random
target = random.randint(1,100)
guess =-1
while guess != target:
    guess = int(input('输入一个整数:'))
    if guess>target:
        print('大了')
    elif  guess<target:
        print('小了')
print('猜对了')


