#一、import — 导入模块
# 导入整个模块
import math
print(math.sqrt(16))
print(math.pi)
# 导入模块里的特定函数
from math import sqrt,pi
print(sqrt(25))
print(pi)
# 导入所有（不推荐，容易命名冲突）
from math import *
print(sin(0))
# 起别名
#import pandas as pd
#import number as np
import time
import random
name =  ["张三", "李四", "王五", "赵六"]
winner = random.choice(name)
print(f'获胜的是:{winner}')
delay =random.randint(1,5)
print(f'等待{delay}秒')
time.sleep(delay)
print('继续执行')
#二、__name__ == '__main__' 是什么？
#看my_tools.py与main.py
#三、pip — Python 包管理器
# 查看已安装的包
import requests
url = "https://api.github.com/users/octocat"
response = requests.get(url,verify=False)
if response.status_code == 200:
    data = response.json()
    print(f"用户名：{data['login']}")
    print(f"仓库数：{data['public_repos']}")
    print(f"粉丝数：{data['followers']}")
else:
    print(f'请求失败，状态码：{response.status_code}')
###练习1：用 random 模拟掷骰子
import random
def roll_dice():
    return random.randint(1,6)
counts = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for _ in range(1000):
    total = roll_dice() + roll_dice()
    counts[total] += 1

for total,count in counts.items():
    print(f'点数：{total} 出现次数：{count}')

#练习2：自定义模块 + __name__ 测试



