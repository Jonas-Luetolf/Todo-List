import json
class Task:
    def __init__(self,name,description,state):
        self.name = name
        self.description = description
        self.state = state

    def set_state(self,state=1):
        self.state = state

    def get_raw(self):
        return {self.name:[self.description,self.state]}
