from src.table.column import Column
from src.table.table import Table
class UI:
    def __init__(self,settings)->None:
        self.settings=settings

    def print_list(self,todo_list,state=None)->str:
        #make table
        name_column=Column("Name")
        description_column=Column("Description")
        state_column=Column("State")
        table=Table()
        
        for index,task in enumerate(todo_list.get_tasks(state)):
            name_column[index]=task.name
            description_column[index]=task.description
            state_column[index]={1:self.settings["check_symbol"],0:self.settings["open_symbol"]}[task.state]
        table.add_column(name_column)
        table.add_column(description_column)
        table.add_column(state_column)
        print(table)
    
    @staticmethod
    def ask_task_informations()->dict:
        return {"name":input("name: "),"description":input("description: "),"state":int(input("state(default 0)")==1)}
