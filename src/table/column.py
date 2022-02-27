import math
from src.table.edge import Edge
class Column:
    def __init__(self,name:str)->None:
        self.name = name
        self.lines=[]

    def clear(self)->None:
        self.lines=[]
    
    def __iter__(self):
        string=str(self)
        ret_list=string.split("\n")
        for i in ret_list:
            yield i

    def __setitem__(self,index:int,contend:str)->None:
        if index>=len(self.lines):
            self.lines+=("" for i in range(0,index+2-len(self.lines)-1))
        self.lines[index]=contend

    def get_x_len(self)->None:
        x_len=0
        return max(len(i) for i in self.lines+[self.name])

    def __str__(self)->str:
        x_len=self.get_x_len()
        ret=f"{Edge.LEFTTOP}{Edge.BOTTOMTOP*math.ceil((x_len-len(self.name))/2)}{self.name}{Edge.BOTTOMTOP*(math.floor((x_len-len(self.name))/2))}{Edge.RIGHTTOP}\n"
        for i in self.lines:
            ret+=f"{Edge.LEFTRIGHT}{i}{' '*(x_len-len(i))}{Edge.LEFTRIGHT}\n"

        return ret+f"{Edge.LEFTBOTTOM}{Edge.BOTTOMTOP*(x_len)}{Edge.RIGHTBOTTOM}"
