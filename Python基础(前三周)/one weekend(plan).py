'''
本周验收项目，把所有知识串起来：字典 + 函数 + 循环菜单

需求：一个命令行成绩管理系统
 功能：
  1. 添加学生和成绩
   2. 查看所有学生
  3. 查询单个学生成绩
  4. 统计平均分/最高分/最低分
   5. 退出系统

 例如：
 {"张三": 85, "李四": 92}
要求：

用字典存储数据
每个功能封装成函数
用 while True 循环显示菜单
用 if-elif-else 处理用户选择
先试试自己写，写不出来再看下面的参考框架（别一上来就看完整代码）：

<details> <summary>参考框架（先自己试着写！）</summary>
'''
scores = {}
def show_menu():
    print('==== 学生管理系统 ====')
    print('1.添加学生')
    print('2.查看全部')
    print('3查询单个学生成绩')
    print('4.统计信息')
    print('5.退出')
    print('====================')

def add_student():                   #1. 添加学生和成绩
    name = input('输入姓名：')
    score = int(input('输入成绩：'))
    scores[name] = score
    print(f'已添加{name}:{score}分')

def show_all():                       #2. 查看所有学生
    if not scores:
        print('还没有学生数据')
        return
    for name in scores:
        print(f'姓名{name}:{scores[name]}分')

def look_student():                    #3.查询单个学生成绩
    name = input('输入学生姓名：')
    if name not in scores:
        print('无此学生数据')
    else:
        print(f'成绩：{scores[name]}')

def show_stats():                                    #4.统计信息
        a = list(scores.values())
        b = sum(a) / len(a)
        print(f'平均分：{b}')
        print(f'最高分：{max(a)}')
        print(f'最低分：{min(a)}')

while True:                   #5. 退出系统
    show_menu()
    choice = input('请输入1—5')
    if choice == '1':
        add_student()
    elif choice == '2':
        show_all()
    elif choice == '3':
        look_student()
    elif choice == '4':
        show_stats()
    elif choice == '5':
        print('再见！')
        break

