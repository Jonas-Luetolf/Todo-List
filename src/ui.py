import os
class UI:
    def __init__(self,settings)->None:
        self.settings=settings

    def print_list(self,todo_data:dict)->str:
        ret=""
        for i in todo_data:
            ret+=self.format_task(i)

        print(ret)
    
    def format_task(self,task):
        if task.state==1:
            symbol=self.settings["check_symbol"]
        else:
            symbol=self.settings["open_symbol"]
        return f"{task.name}: {task.description} {symbol}\n"
