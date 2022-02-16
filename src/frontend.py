import os
class UI:
    def __init__(self)->None:
        pass

    def format_list(self,todo_data:dict)->str:
        ret=""
        for i in todo_data:
            ret+=f"{i}: {i[0]}{i[1]}\n"
        
        return ret

    def clean(self)->None:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
