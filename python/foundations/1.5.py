###创建
fruits=['苹果','香蕉','西瓜',]
nu=['1','2','3','4']
mixed=['hello',42,True,3.14]
# 增
fruits.append('葡萄')
# 删
fruits.remove('香蕉')# 删除指定元素
fruits.pop()        # 删除最后一个
del fruits[0]       # 删除指定位置
# 改
fruits[0] = '龙眼'
# 查
print(fruits[0])
print(fruits[-1])
#二、列表常用操作
numms=[3,1,4,6,8,9,5,]
len(numms)       # 长度
max(numms)       # 最大值
min(numms)       # 最小值

numms.sort()      # 原地排序
sorted(numms)     # 返回新排序列表（不改变原列表）

# 索引和切片（和字符串一样）
numms[1]           # 第一个
numms[1:4]         #[3,4,5]
numms[::-1]      #[9, 8, 6, 5, 4, 3, 1]
#三、元组 tuple — 不可变列表
# 元组用 ()，创建后不能修改
point=(10,20)
print(point[0])
#point[0] = 30        # ❌ 报错！元组不可修改

# 元组常用于函数返回多个值
def get_position():
    return 100,200,300       # x, y, z
x,y,z = get_position()         # 解包
###练习1：动态列表统计
# 不断输入数字，输入0结束，最后输出总和和平均值
num=[]
while True:
    a = int(input('输入零时停止：'))
    if a == 0:
        print('结束')
        break
    num.append(a)
print(f'长度为：{len(num)}')
print(f'总和{sum(num)}')
print(f'平均值：{sum(num)/len(num)}')
#练习2：找最大值
nums=[2,3,11,7,9,-1,43]
max_num=nums[0]
for n in nums:
    if n > max_num:
        max_num = n
print(max_num)
#练习3：列表去重
# 输入一堆数字，去掉重复后输出
data = [1, 3, 2, 3, 1, 5, 2, 4, 3]
unique = []
for b in data:
    if b not in unique:
        unique.append(b)
unique.sort()
print(f'去重：{unique}')


