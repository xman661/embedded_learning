#关键点： 本周学了三个核心技能：NumPy 数组操作、matplotlib 画图、向量化思维。今天不学新知识，全部用来复盘盲打。
#1
'''
📝 盲打检查 1：NumPy 基础
arr = np.arange(10)                            # arange     ← 0-9数组
zeros = np.zeros((3,4))                      # zeros      ← 全0矩阵
I = np.eye(4)                               # eye        ← 单位矩阵

a = np.array([[1,2,3], [4,5,6]])                  # shape(2,3)
b = np.array([[1,2], [3,4], [5,6]])               # shape(3,2)
result = a @ b                              # @          ← 矩阵乘法
'''
#2
'''
📝 盲打检查 2：布尔索引
data = np.array([23, 45, 12, 67, 34, 89, 55])
filtered = data[data > 50]                  # >         ← [67 89 55]
'''
#3
'''
📝 盲打检查 3：广播
A = np.ones((3, 4))                               # shape(3,4)
row = np.array([10, 20, 30, 40])
B = A + row                                 # +         ← 广播到3行
print(B.shape)   # (3, 4)

A.shape:(3,4)    B.shape(4,)
                        (1,4)   ----   (3,4)
([1,1,1,1]                          ([10, 20, 30, 40]
 [1,1,1,1]            +              [10, 20, 30, 40]
 [1,1,1,1])                          [10, 20, 30, 40])                       [10, 20, 30, 40]
                  ([11,21,31,41]
                  [11,21,31,41]
                  [11,21,31,41])              
'''
#4
'''
📝 盲打检查 4：matplotlib 折线
x = np.linspace(0,10,100)
y = np.sin(x)

plt.figure(figsize=(10,8))
plt.plot(x,y,'ro--',label='sin')              # plot      ← 折线图
plt.title('正弦曲线')                          # title     ← 标题
plt.grid(True,alpha=0.3)                      # grid      ← 网格
plt.legend()                                  # legend    ← 图例
plt.savefig('output/review_sin.png',dpi=150)  # savefig   ← 保存
plt.show()
'''
#5
'''
📝 盲打检查 5：subplots + 直方图
fig,axes =plt.subplots(1,2,figsize=(10,8))
data = np.random.randn(1000)

axes[0].hist(data,
             bins=30,
             alpha=0.7)
axes[0].set_title('直方图')

axes[1].plot(np.cumsum(data))
axes[1].set_title('累计和')

plt.tight_layout()
plt.show()
'''