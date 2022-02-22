import json
from os import mkdir
from os.path import expanduser, isfile, isdir
from src.task import Task

class TaskNotFound(Exception):
    def __init__(self,mes:str=""):
        super().__init__()
        self.mes=mes
    
    def __str__(self):
        return f"TaskNotFound: {self.mes}"

class ListHandler:
    def __init__(self,name:str,folder:str)->None:
        self.name=name
        self.folder=folder
        self.open()
        
    def open(self)->None:
        if isfile(f"{self.folder}{self.name}.json"):
            with open(f"{self.folder}{self.name}.json","r") as f:
                self.data = json.load(f)   
        else:
            if isdir(self.folder):
                mkdir(self.folder)
            
            with open(f"{self.folder}{self.name}.json","w") as f:
                f.write('{"tasks":{}}')
                self.data=json.loads('{"tasks":{}}')

        self.tasks=[]
        for task in self.data["tasks"]:
            self.tasks.append(Task(task,self.data["tasks"][task][0],self.data["tasks"][task][1]))
    
    def get_tasks(self,state:int=None)->list:
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
        
    def write(self)->None:
        task_data={}
        for i in self.tasks:
            task_data.update(i.get_raw())

        raw_str=json.dumps({"name":self.name,"tasks":task_data})
        with open(f"{self.folder}{self.name}.json","w") as f:
            f.write(raw_str)

    def add_task(self,name:str,description:str,state:int)->None:
        self.tasks.append(Task(name,description,state))

    def delete_task(self,name:str)->None:
        for index,task in enumerate(self.tasks):
            if  task.name == name:
                del self.tasks[index]
                return None

        raise TaskNotFound(f"Task {name} not found")
