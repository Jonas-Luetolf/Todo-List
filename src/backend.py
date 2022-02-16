import json
import os
from src.ArgummentParser.argummentparser import ArgummentParser

class ListHandler:
    def __init__(self,name,folder=f"{os.path.expanduser('~')}/.todo-list/"):
        self.name=name
        self.folder=folder
        self.open()
        
    def open(self):
        try:
            with open(f"{self.folder}{self.name}.json","r") as f:
                self.data = json.load(f)   
        except:
            print("exc1")
            try:
                os.mkdir(self.folder)
            
            except FileExistsError:
                pass

            with open(f"{self.folder}{self.name}.json","w") as f:
                f.write('{"tasks":{}}')
                self.data=json.loads('{"tasks":{}}')

    def get_task(self,name:str):
        return self.data["tasks"][name]

    def add_task(self,name:str,description:str,check=0):
        self.data["tasks"].update({name:[description,check]})

    def write(self):
        with open(f"{self.folder}{self.name}.json","w") as f:
            f.write(json.dumps(self.data))
    
    def get_tasks(self):
        return self.data["tasks"]

    def change_state(self,name:str,state=1):
        self.data["tasks"][name][1]=state
