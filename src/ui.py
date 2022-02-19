from src.layout.grid import Grid
from src.layout.widget import Widget
class UI:
    def __init__(self,settings)->None:
        self.settings=settings

    def print_list(self,todo_list,state=None)->str:
        temp=Widget(todo_list.name)
        for index,task in enumerate(todo_list.get_tasks(state)):
            temp[index]=self.format_task(task)

        print(temp)
    
    def format_task(self,task)->str:
        if task.state==1:
            symbol=self.settings["check_symbol"]
        else:
            symbol=self.settings["open_symbol"]
        return f"{task.name}: {task.description} {symbol}"

    @staticmethod
    def ask_task_informations()->dict:
        return {"name":input("name: "),"description":input("description: "),"state":int(input("state(default 0)")==1)}
