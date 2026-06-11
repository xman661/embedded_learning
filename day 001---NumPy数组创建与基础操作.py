#一、创建数组的三种方式
#方式1：从列表转换
import numpy as np
arr1 = np.array([1,2,3,4,5])        # 一维 shape=(5,)
print(arr1.shape)
arr2 = np.array([[1,2,3],[4,5,6]])  # # 二维 shape=(2,3)
print(arr2.shape)
arr3 = np.array([1,2,3], dtype =np.float32)
print(arr3)
#方式2：内置函数（最常用）
zeros = np.zeros((3,4))           # 全0矩阵
print(zeros)
ones = np.ones((2,3))             # 全1矩阵
print(ones)
eye = np.eye(3)                   # 单位矩阵（对角线=1）
print(eye)
ar = np.arange(0,10,2)
print(ar)                         # [0 2 4 6 8]
lin = np.linspace(0,1,5)
print(lin)                        # [0. 0.25 0.5 0.75 1.]
full = np.full((2,3),7)
print(full)                        # 全填7
temp = np.zeros(10)
empty = np.empty((2,2))
print(empty)
#方式3：随机数组
np.random.seed(42)
rand = np.random.rand(3,3)         # 均匀分布[0,1)
print(rand)
rand = np.random.randn(3,3)        # 标准正态分布
print(rand)
randint =np.random.randint(1,10,size=(3,5))
print(randint)                     # 0~9随机整数
uniform = np.random.uniform(-1,1,size=(3,))
print(uniform)                      # [-1,1)均匀
#二、核心属性（拿到数组先看 shape 和 dtype）
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)        # (2, 3)    —— 形状（最重要）
print(a.ndim)         # 2         —— 维度数
print(a.size)         # 6         —— 元素总数
print(a.dtype)        # int64     —— 数据类型
print(a.itemsize)     # 8         —— 每元素字节数
print(a.nbytes)       # 48        —— 总字节数 = size × itemsize
#三、向量化运算（告别 for 循环）
#逐元素运算：
x = np.array([1,2,3])
y = np.array([10,20,30])
print(x+y)
print(x-y)
print(x*y)
print(x**2)
print(x%2)          #取余
#通用函数（ufunc）：
print(np.sqrt(x))     #   ← 开平方
print(np.exp(x))      #   ← e^x
print(np.sin(x))      #   ← 正弦
#聚合函数（归约为一个数）：
data = np.array([3,6,2,9,4,6])
print(np.sum(data))
print(np.mean(data))
print(np.std(data))       #  std   ← 标准差
print(np.max(data))
print(np.min(data))
print(np.argmax(data))    #   argmax       ← 最大值索引
print(np.median(data))    #    median      ← 中位数
#axis 参数（按维度聚合）：
matrix = np.array([[1,2,3],
                   [4,5,6]])
print(np.sum(matrix,axis=0))     # [5 7 9]  ← 按列求和（沿行方向压缩）

print(np.sum(matrix,axis=1))     # [6 15]   ← 按行求和（沿列方向压缩）
'''
四、dtype 深入（嵌入式视角）

dtype	          等价的C类型	        适用场景
int8/uint8	     int8_t/uint8_t	    ADC值、传感器数据
int16/uint16	 int16_t/uint16_t	编码器计数值
int32/uint32	 int32_t/uint32_t	默认整数
float32	         float	            浮点运算
float64	         double	            默认浮点
'''
arr_i8 = np.array([1,2,3],dtype = np.int8)
print(arr_i8.nbytes)
# 类型转换
arr_f64 = np.array([1,2,3],dtype=np.float64)
print(arr_f64.nbytes)
arr_i32 = arr_f64.astype(np.int32)     # 转int32
print(arr_i32.nbytes)
#💡 传感器案例： 16位ADC @ 1kHz 采样 → 每秒 2KB。用 int16 存比 float32 省一半内存。
#五、性能对比（向量化 vs for)
import time
big = np.random.rand(10_000_000)
t0 =time.time()
r1 = np.sum(big**2)     # NumPy
t1 = time.time();print(f'NumPy:{t1-t0:.4f}s')

t2 =time.time()
s = 0
for i in range(len(big)): s += big[i] ** 2    # for循环
t3 = time.time();print(f'Loop:{t3-t2:.4f}s')
# NumPy 快 30-80x
'''
✍️ 编程练习题

1.创建 5×5 全零数组，改 [2,4]=42、[0,1]=99，打印数组和 shape
2.np.arange(100) 求 sum/mean/max/min/std/median
3.3×4 随机均匀数组，按行求均值(axis=1)、按列求最大(axis=0)
4.0-255 数组分别用 uint8 / int16 / float32 存，比较 nbytes
'''
#1
a = np.zeros((5,5))
a[2,4]=42
a[0,1]=99
print(a)
print(a.shape)
#2
b = np.arange(100)
print(np.sum(b))
print(np.mean(b))
print(np.max(b))
print(np.min(b))
print(np.std(b))
print(np.median(b))
#3
c = np.random.rand(3,4)
print(np.mean(c,axis=1))
print(np.max(c,axis=0))
#4
d = np.arange(255)
d_u8 = d.astype(np.uint8)
d_i16 = d.astype(np.int16)
d_f32 = d.astype(np.float32)
print(d_u8.nbytes)
print(d_i16.nbytes)
print(d_f32.nbytes)













