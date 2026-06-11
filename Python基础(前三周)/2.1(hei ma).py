###文件1.8
import time
#f = open(r"D:\token\新建 文本文档.txt",'r',encoding='utf-8')
#print(type(f))
#print(f'读取10个字节的结果：{f.read(10)}')
#print(f'read的读取全部内容的结果：{f.read()}')
print('-----------------------------------------------------------')
#lines = f.readlines()       #读取文件的全部行，封装到列表中
#print(f'lines对象的类型{type(lines)}')
#print(f'lines对象的内容是：{lines}')
#line1 = f.readline()
#line2 = f.readline()
#line3 = f.readline()
#print(f'第1行的数据内容是：{line1}')
#print(f'第2行的数据内容是：{line2}')
#print(f'第3行的数据内容是：{line3}')
# for循环
#for line in f:
    #print(f'每一行的数据是：{line}')

#暂停
#time.sleep(50000000)   #暂停50000000秒

#文件的关闭
#f.close()

#with open 语法操作文件
with open (r"D:\token\新建 文本文档.txt",'r',encoding='utf-8') as f:
    for line in f:
        print(f'每一行的数据是：{line}')
#with open   自动包含文件的关闭

#time.sleep(5000000)

fr = open(r"D:\py1\2.1(hei ma)公司个人工资去向(测试).txt", 'r', encoding ='utf-8')

fw = open(r'D:/2.1(hei ma)公司个人工资去向(正式).txt', 'w', encoding ='utf-8')
for line in fr:
    line = line.strip()
    if line.split(' ')[4] == '测试':
        continue
    fw.write(line)
    fw.write('\n')
fw.flush
fw.close()