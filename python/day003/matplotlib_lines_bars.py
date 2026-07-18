import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
#一、折线图 plt.plot()
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
plt.figure(figsize=(8,5))            # 创建画布
plt.plot(x,y,marker='o',linestyle='-',color='b',label='y=2x')
plt.title('折线图示例')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.grid(True,alpha=0.3)
plt.legend()
plt.show()
#二、柱状图 plt.bar()
categories = np.array(['苹果', '香蕉', '橘子', '葡萄'])
sales = [120, 85, 200, 150]
plt.figure(figsize=(8,5))
bars = plt.bar(categories, sales,color=['red','yellow','orange','purple'])
plt.title('水果销量统计')
for bar in bars:
    height = bar.get_height()
    plt.text(
        x = bar.get_x() + bar.get_width()/2,
        y = height + 2,
        s = str(height),
        ha='center',
        va='bottom'
    )
plt.show()
#三、一图多线
x = np.linspace(1,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(10,5))
plt.plot(x,y1,'r-',label='sin(x)')
plt.plot(x,y2,'b--',label='cos(x)')
plt.legend(loc='best')
plt.grid(True,alpha=0.3)
plt.show()
'''
四、常用 marker/linestyle/color 速查

参数	选项示例	含义
marker	'o' '^' 's' 'x' '.'	圆形/三角/方块/叉/点
linestyle	'-' '--' ':' '-.'	实线/虚线/点线/点划线
color	'r' 'g' 'b' 'k' '#FF0000'	红/绿/蓝/黑/十六进制
快捷格式串：'ro--' = 红色圆圈虚线，等价于 color='r', marker='o', linestyle='--'
'''
print('--------------------------------------------------------------------------')
'''
✍️ 编程练习题

用 np.arange(1,13) 生成1-12月，np.random.randint(20, 40, 12) 生成温度，画折线图展示全年温度变化
数据：['Python', 'C', 'Java', 'C++'] 对应 [90, 70, 85, 65]，画柱状图并标数值，标题"编程语言热度"
'''
#1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.arange(1,13)
y = np.random.randint(20,40,12)
plt.figure(figsize=(10,5))
plt.plot(x,y,'ro-',label='度数')
plt.title('全年温度变化')
plt.xlabel('月份')
plt.ylabel('温度')
plt.grid(True,alpha=0.3)
plt.show()
#2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.array(['Python', 'C', 'Java', 'C++'])
y = [90, 70, 85, 65]
plt.figure(figsize=(10,7))
bars = plt.bar(x,y,color=['r','g','b','y'])
plt.title('编程语言热度')
plt.xlabel('类型')
plt.ylabel('热度')
for bar in bars:
    height = bar.get_height()
    plt.text(
        x = bar.get_x() + bar.get_width()/2,
        y = height +2,
        s = str(height),
        ha='center',
        va='bottom'
    )
plt.show()
print('----------------------------------------------------')
'''
📝 盲打默写
x = np.array([1, 2, 3, 4])
y = np.array([3, 7, 2, 9])

plt.______figure(figsize=(10,5))       # figure  ← 创建画布
plt.______plot(x,y,'ro-')             # plot    ← 画折线
plt.______title('标题')                # title   ← 标题
plt.______xlabel('')                  # xlabel  ← X轴标签
plt.______ylabel('')                  # ylabel  ← Y轴标签
plt.______legend()                    # legend  ← 图例
plt.______grid(True,alpha=0.3)       # grid    ← 网格
plt.______show()                      # show    ← 显示
'''







