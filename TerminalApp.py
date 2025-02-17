from Application import Application
from DerivedCommand import InsertRowCommand, InsertHeadCommand, InsertTailCommand, ListCommand
from SimpleMarkdownDoc import SimpleMarkdownDoc


class TerminalApp(Application):
    def __init__(self, cmd_capacity=50):
        super().__init__(cmd_capacity)

    def CreateDocument(self, name):
        # 创建本应用支持的文件
        return SimpleMarkdownDoc(name)

    def InsertRow(self, row_num, text):
        self._cmdManager.Execute(InsertRowCommand(self._activateDoc, row_num, text))

    def InsertHead(self, text):
        self._cmdManager.Execute(InsertHeadCommand(self._activateDoc, text))

    def InsertTail(self,text):
        self._cmdManager.Execute(InsertTailCommand(self._activateDoc, text))

    def List(self):
        self._cmdManager.Execute(ListCommand(self._activateDoc))

    def Run(self):
        while True:
            user_input = input(r"请输入命令[q\Q退出]: ")
            if user_input == 'q' or user_input == 'Q':
                break
            input_list = user_input.split()
            command = input_list[0]
            if command == 'load':
                argument = ' '.join(input_list[1:])
                self.Open(argument)
            elif command == 'save':
                self.Save()
            elif command == 'insert':
                if input_list[1].isdigit():
                    row_num = int(input_list[1])
                    argument = ' '.join(input_list[2:])
                    self.InsertRow(row_num, argument)
                else:
                    argument = ' '.join(input_list[1:])
                    self.InsertTail(argument)
            elif command == 'append-head':
                argument = ' '.join(input_list[1:])
                self.InsertHead(argument)
            elif command == 'append-tail':
                argument = ' '.join(input_list[1:])
                self.InsertTail(argument)
            elif command == 'undo':
                self.Undo()
            elif command == 'redo':
                self.Redo()
            elif command == 'list':
                self.List()
