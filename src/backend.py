import json

class ListHandler:
    def __init__(self,path):
        self.path=path
        self.open()

    def open(self):
        with open(self.path,"r") as f:
            self.data = json.load(f)
        self.name=self.data['name']   
    
    def get_by_name(self,name):
        return self.data["tasks"][name]

    def set_item(self,name,description,check=0):
        self.data["tasks"].update({name:[description,check]})

    def write(self):
        with open(self.path,"w") as f:
            f.write(json.dumps(self.data))
    
    def get_data(self):
        return self.data["tasks"]

    def change_state(self,name,state=1):
        self.data["tasks"][name][1]=state
