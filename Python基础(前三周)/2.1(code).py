###1. 写文件
# 写入模式 'w' — 会覆盖原文件！
with open(r"D:\No Abandon\train.txt",'w',encoding = 'utf-8') as f:
    f.write('hello\n')
    f.write('world\n')
# 追加模式 'a' — 在文件末尾添加
with open(r"D:\No Abandon\train.txt",'a',encoding = 'utf-8') as f:
    f.write('追加一行\n')
#2. 读文件
# 一次读完
with open(r"D:\No Abandon\train.txt",'r',encoding = 'utf-8') as f:
    content = f.read()
    print(content)
# 逐行读取（常用）
with open(r"D:\No Abandon\train.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
# 读取到列表
with open(r"D:\No Abandon\train.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()    # 每行作为列表的一个元素

'''
3. 为什么用 with？


不用 with 要手动关闭
f = open('test.txt', 'w')
f.write('hello')
f.close()  容易忘记！

用 with 自动关
with open('test.txt', 'w') as f:
    f.write('hello')
    缩进结束自动关闭
'''
###今日练习
#1.写文件 + 读文件：创建一个 txt，写入3行文字，再读出来打印
with open('2.1(code)1.txt', 'w', encoding ='utf-8') as m:
    m.write('你好\n')
    m.write('请问有什么要帮助的吗？\n')
    m.write('没有\n')
with open('2.1(code)1.txt', 'r', encoding='utf-8') as n:
    print(n.read())

#逐行处理：创建一份"成绩单"txt（每行一个姓名和分数，用逗号隔开），读取并算出平均分
with open('2.1(code)成绩单.txt', 'w', encoding ='utf-8') as o:
    o.write('小明，60\n')
    o.write('小红，50\n')
    o.write('张三，63\n')
    o.write('李四，94\n')
    o.write('李黑，73\n')
    o.write('王五，80\n')
with open('2.1(code)成绩单.txt', 'r', encoding ='utf-8') as p:
      lines1 = p.readlines()
total = 0
count = 0
for line in lines1:
    parts = line.strip().split('，')
    name = parts[0]
    score = int(parts[1])
    total += score
    count += 1
avg = total / count
print(avg)



