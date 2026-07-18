import json
import os
class Note:
    def __init__(self,title,content):
        self.title = title
        self.content = content

class Notebook:
    def __init__(self,filename = 'notes.json'):
        self.filename = filename
        self.notes = []
        self.load()

    def add(self,title,content):
        note = Note(title,content)
        self.notes.append(note)
        print(f'✅ 笔记《{note.title}》已添加')

    def list_all(self):
        if not self.notes:
            print("📭 暂无笔记")
            return
        print(f'\n📒一共有{len(self.notes)}条')
        for i,note in enumerate(self.notes):
            print(f'{i + 1}.{note.title}')
    def show(self,index):
        if 0 <= index < len(self.notes):
            print(f'\n 【{self.notes[index].title}】')
            print(self.notes[index].content)
        else:
            print('❌ 无效索引')

    def delete(self,index):
        if 0 <= index < len(self.notes):
            remove = self.notes.pop(index)
            print(f'🗑️ 已删除《{remove.title}》')
        else:
            print('❌ 无效索引')

    def save(self):
        data = [{'title':n.title,'content':n.content} for n in self.notes]
        with open(self.filename,'w',encoding = 'utf-8') as f:
            json.dump(data,f,ensure_ascii=False, indent=2)
        print("💾 已保存")

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename,'r',encoding = 'utf-8') as f:
            data = json.load(f)
            self.notes = [Note(item['title'],item['content']) for item in data]
            print(f"📂 已加载 {len(self.notes)} 条笔记")

    def main(self):
        notebook = Notebook()

        while True:
            print('\n' + '=' *30)
            print('  命令行记事本')
            print('=' *30)
            print("1. 查看所有笔记")
            print("2. 查看单条笔记")
            print("3. 添加笔记")
            print("4. 删除笔记")
            print("5. 保存并退出")
            print("=" * 30)

            choice = input('请选择（1-5）：').strip()
            if choice == '1':
                notebook.list_all()
            elif choice == '2':
                notebook.list_all()
                if notebook.notes:
                    try:
                        idx = int(input("请输入笔记编号："))
                        notebook.show(idx)
                    except ValueError:
                        print("❌ 请输入数字")
            elif choice == '3':
                title = input('笔记标题:').strip()
                if not title:
                    print('❌标题不能为空')
                    continue
                print('请输入内容（输入 /end 结束）：')
                lines = []
                while True:
                    line =input()
                    if line == '/end':
                        break
                    lines.append(line)
                content ='\n'.join(lines)
                notebook.add(title,content)
                notebook.save()
            elif choice == '4':
                notebook.list_all()
                if notebook.notes:
                    try:
                        idx = int(input("请输入要删除的笔记编号：")) - 1
                        notebook.delete(idx)
                        notebook.save()
                    except ValueError:
                        print('❌ 请输入数字')

            elif choice == '5':
                notebook.save()
                print('👋 再见！')
                break

            else:
                print('❌ 无效选择，请输入1-5')

if __name__ == '__main__':
    nb = Notebook()
    nb.main()


