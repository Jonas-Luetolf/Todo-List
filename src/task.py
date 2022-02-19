class Task:
    def __init__(self,name:str,description:str,state:int):
        self.name = name
        self.description = description
        self.state = state

    def set_state(self,state:str=1)->None:
        self.state = state

    def get_raw(self)->dict:
        return {self.name:[self.description,self.state]}
