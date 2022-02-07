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
        return self.data
        
class TodoHandler:
    def __init__(self):
        self.lists=[]

    def add_list(self,path):
        self.lists.append(ListHandler(path))

    def get_task(self,list_name,name):
        for i in self.lists:
            if i.name==list_name:
                return i.get_by_name(name)











def main():
    h=TodoHandler()
    h.add_list("test.json")
    print(h.get_task("test","test"))

if __name__ == "__main__":
    main()
