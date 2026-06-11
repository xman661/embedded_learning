'''
关键点： argparse让脚本可以接受命令行参数、嵌入式中常用于测试工具

一、为什么需要 argparse？
你现在写的程序都是 input() 等着用户输入。但很多工具是运行时就传参数的：

# 比如这个
python notes.py --add "标题" --content "内容"
python notes.py --list
python notes.py --delete 3
'''
#二、argparse 基础用法
import argparse
# 1. 创建解析器
parser = argparse.ArgumentParser(description='一个简单的计算器')
# 2. 添加参数
parser.add_argument('num1',type=int,help='第一个数字')     # 位置参数
parser.add_argument('num2',type=int,help='第二个数字')     # 位置参数
parser.add_argument('--operator','-o',default='+',help='运算符')      # 可选参数
# 3. 解析参数
args = parser.parse_args()
# 4. 使用参数
if args.operator == '+':
    print(f'{args.num1}+{args.num2} = {args.num1 + args.num2}')
elif args.operator == '-':
    print(f'{args.num1}-{args.num2} = {args.num1 - args.num2}')
# 位置参数 — 按顺序传，必须传
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('filename',help='文件名')      # python script.py myfile.txt
# 可选参数 — 带 -- 前缀，可指定默认值
parser.add_argument('--output','-o',default='out.text',help='输出文件')
#python '文件名.py' myfile.text --output result.txt
#python '文件名.py' myfile.text --o result.txt
# 开关参数 — store_true 表示有就是True，没有就是False
parser.add_argument('--verbose','-v',action='store_true',help='显示详细信息')
#python '文件名.py' --verbose     → args.verbose=True
#python '文件名.py'               → args.verbose=False
args = parser.parse_args()
print(f"输入文件: {args.filename}")
print(f"输出文件: {args.output}")
print(f"详细模式: {'开启' if args.verbose else '关闭'}")
if args.verbose:
    print("\n=== 详细信息 ===")
    print(f"程序开始处理文件: {args.filename}")
    print(f"处理结果将保存到: {args.output}")
    print("处理完成！")
#四、类型指定
parser.add_argument("--age", type=int, help="年龄")       # 自动转int
parser.add_argument("--rate", type=float, help="利率")    # 自动转float
parser.add_argument("--count", type=int, default=1)       # 默认值

# 如果传了非数字，argparse会自动报错，不用自己写try/except
































