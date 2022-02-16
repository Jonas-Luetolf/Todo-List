import json
import os
from src.ArgummentParser.argummentparser import ArgummentParser
from src.task import Task
class ListHandler:
    def __init__(self,name,folder=f"{os.path.expanduser('~')}/.todo-list/"):
        self.name=name
        self.folder=folder
        self.open()
        
    def open(self):
        if os.path.isfile(f"{self.folder}{self.name}.json"):
            with open(f"{self.folder}{self.name}.json","r") as f:
                self.data = json.load(f)   
        elif os.path.isdir(self.folder):
            os.mkdir(self.folder)
            
            with open(f"{self.folder}{self.name}.json","w") as f:
                f.write('{"tasks":{}}')
                self.data=json.loads('{"tasks":{}}')
        else:
            with open(f"{self.folder}{self.name}.json","w") as f:
                 f.write('{"tasks":{}}')
                 self.data=json.loads('{"tasks":{}}')

        self.tasks=[]
        for task in self.data["tasks"]:
            self.tasks.append(Task(task,self.data["tasks"][task][0],self.data["tasks"][task][1]))
    def get_tasks(self,state=None):
        if state != None and type(state)!=int:
            raise TypeError

        if state==None:
            return self.tasks
        else:
            ret=[]
            for task in self.tasks:
                if task.state==state:
                    ret.append(task)
            return ret
        
    def write(self):
        task_data={}
        for i in self.tasks:
            task_data.update(i.get_raw())

        raw_str=json.dumps({"name":self.name,"tasks":task_data})
        with open(f"{self.folder}{self.name}.json","w") as f:
            f.write(raw_str)
