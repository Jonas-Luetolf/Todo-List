import os
class UI:
    def __init__(self)->None:
        pass

    def print_list(self,todo_data:dict)->str:
        ret=""
        for i in todo_data:
            ret+=f"{i.name}: {i.description}, {i.state}\n"
        
        print(ret)

    def clean(self)->None:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
