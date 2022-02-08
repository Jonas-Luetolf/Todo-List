import backend
import os
class UI:
    def __init__(self,todo_list)->None:
        self.todo_list=todo_list

    def format_list(self)->str:
        todo_data=self.todo_list.get_data()
        ret=""
        for i in todo_data:
            ret+=f"{i}: {self.todo_list.get_by_name(i)[0]} {self.todo_list.get_by_name(i)[1]}\n"
        
        return ret

    def clean(self)->None:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def start(self)->None:
        while True:
            self.clean()
            print(self.format_list())
            self.input()
            self.todo_list.write()      

    def input(self):
        return input()

def main():
    ui=UI(backend.ListHandler("test.json"))
    ui.start()
main()
