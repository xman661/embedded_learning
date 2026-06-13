#关键点： plt.subplots() 多子图布局，plt.hist() 看数据分布，savefig() 保存图片。三者组合 = 可发表的数据可视化报告。
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
#一、subplots — 多子图布局
fig,axes = plt.subplots(2,2,figsize=(10,8))
x = np.linspace(0,10,100)
axes[0,0].plot(x,np.sin(x),'r-')
axes[0,0].set_title('sin(x)')

axes[0,1].plot(x,np.cos(x),'b-')
axes[0,1].set_title('cos(x)')

axes[1,0].plot(x,x**2,'g-')
axes[1,0].set_title('x^2')

axes[1,1].plot(x,np.exp(x/5),'m-')
axes[1,1].set_title('exp(x/5)')

plt.tight_layout()                    # 自动调间距，防标签重叠
plt.show()

#二、直方图 plt.hist()
data = np.random.randn(1000)
plt.figure(figsize=(10,5))
plt.hist(data,
         bins=30,
         alpha=0.7,
         color='steelblue',
         edgecolor='black')
plt.grid(True,alpha=0.3)
plt.show()
print(f'均值: {np.mean(data):.3f}')      # 应接近0
print(f'标准差:{np.std(data):.3f}')        # 应接近1

#三、savefig — 保存图片
x = np.array([1,2,3,4,5])
y = np.array([5,4,3,2,1])
plt.figure(figsize=(8,5))
plt.plot(x,y,'bo--',linewidth=2,markersize=8)
plt.title('保存示例')
plt.savefig(r"D:\wearhouse\保存示例\Day 4 — subplots + savefig + 直方图.png",dpi=150,bbox_inches='tight') ## ← 在show之前
plt.show()
#💡 先 savefig 后 show！ show() 会清空画布，顺序反了存的是空白图。
'''
✍️ 编程练习题

《1》 2行1列 subplots：第一行柱状图（品牌 A/B/C，销量 30/55/42），第二行折线图（星期1-7，步数 random 4000-12000），用 tight_layout()
《2》 np.random.randn(500) 画直方图(bins=20)，图上标注均值和标准差，保存为r"D:\wearhouse\保存示例\编程练习题《2》.png"
'''
#1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
fig,axes = plt.subplots(2,1,figsize=(10,8))
a = np.array(['A','B','C'])
b = np.array([30,55,42])
c = np.array([1,2,3,4,5,6,7])
d = np.random.randint(4000,12000,size=7)
axes[0].bar(a,b,color=['r','b','g'])
axes[0].set_title('品牌销量')
axes[0].set_xlabel('品牌')
axes[0].set_ylabel('销量')

axes[1].plot(c,d,'yo-')
axes[1].set_title('每周步数')
axes[1].set_xlabel('星期1-7')
axes[1].set_ylabel('步数')

plt.tight_layout()
plt.show()

#2import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
x = np.random.randn(500)
plt.figure(figsize=(10,8))
plt.hist(x,
         bins=20,
         alpha=0.7,
         color='steelblue',
         edgecolor='black'
         )
plt.title('标准正态分布直方图（500样本）')
plt.xlabel('数值区间')
plt.ylabel('频次')
plt.grid(True,alpha=0.3)
plt.text(0.05,0.90,
         f'均值：{np.mean(x):.3f} \n标准差:{np.std(x):.3f}',
         transform = plt.gca().transAxes,
         fontsize=12,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.savefig(r"D:\wearhouse\保存示例\编程练习题《2》.png",dpi=150,bbox_inches='tight')
plt.show()

print(f'均值：{np.mean(x):.3f}')
print(f'标准差：{np.std(x):.3f}')
'''
📝 盲打默写

# 1. 创建2×2的subplots
fig, axes = plt.subplots(2,2,figsize=(10,8))       # subplots

# 2. 在第1行第1列子图画折线
axes[0, 0].plot(x,y)                               # plot

# 3. 设置子图标题
axes[0, 0].set_title('')                           # set_title

# 4. 画直方图（data，20个区间）
plt.hist(data,
          bins=20)                                 # hist

# 5. 保存为 chart.png，dpi=150
plt.savefig('output/chart.png',dpi=150)             # savefig
'''









