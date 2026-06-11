#1. 创建字典
# 空字典
d = {}
# 空字典
scores = {'张三':54,'李四':74,'王五':83}
# 用 dict() 创建
d=dict(name='小明',age=20)
print(d)
#2. 增删改查
# 查
print(scores['张三'])     # 54 — key不存在会报错
print(scores.get('李'))   # None — 不存在返回None，不报错
print(scores.get('李',0)) # 不存在返回默认值0
# 增/改
scores['小红'] = 66
scores['张三'] = 77
# 删
del scores['李四']    # 删除
scores.pop('王五')    #删除并返回值
scores.clear()       # 清空
#3. 三种遍历方式
score = {"张三": 85, "李四": 92, "王五": 78}
# 只遍历key
for name in score:
    print(name)
# 只遍历value
for scoree in score.values():
    print(scoree)
# 同时遍历 key 和 value（最常用）
for name,scoree in score.items():
    print(f'{name}:{scoree}')
#4. 判断 key 是否存在
if '张三' in score:
    print('有张三的成绩')
###今日练习
#成绩字典平均分：创建一个包含5个学生成绩的字典，计算平均分、最高分、最低分
scoress = {'张三':64,'李四':43,'小明':83,'小孩':97,'布鲁斯':58}
a = list(scoress.values())
b = sum(a)/len(a)
print(f'平均成绩:{b:.2f}')
print(f'最大值{max(a)}')
print(f'最小值{min(a)}')
#字符频率统计：输入一个字符串，统计每个字符出现的次数（用字典）
c = input('')
d = {}
for e in c:
    if e in d:
        d[e] +=1
    else:
        d[e] = 1
for k,v in d.items():
    print(f'{k}:{v}')
#英汉词典：创建英-汉对照字典，输入英文查中文
dict_en_cn = {
    "apple": "苹果",
    "banana": "香蕉",
    "cat": "小猫",
    "dog": "小狗",
    "book": "书本"
}
word = input('输入英文：')
if word in dict_en_cn:
    print(f'{word}:{dict_en_cn[word]}')
else:
    print(f'字典无注释')

