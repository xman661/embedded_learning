#关键点： os.walk 是遍历目录的标准方式，递归思想在这里体现。
#今天做一个能在命令行搜索文件内容的工具，整合前面学的所有知识。
#一、核心：os.walk()
'''
os.walk() 自动递归遍历目录，返回三个值：

root：当前目录路径
dirs：当前目录下的子目录列表
files：当前目录下的文件列表
'''
import os
# 先看看 os.walk 怎么用
for root,dirs,files in os.walk('d:\\py1'):
    print(f'当前目录:{root}')
    print(f'子目录:{dirs}')
    print(f'文件:{files}')
    print('-----------')
'''
输出类似：

当前目录：d:\py1
子目录：['subfolder']
文件：['hello.py', 'notes.py']
---
当前目录：d:\py1\subfolder
子目录：[]
文件：['test.txt']
---'''
#二、文件搜索工具完整代码
import os
import argparse
