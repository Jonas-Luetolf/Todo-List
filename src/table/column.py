import math
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
        ret=f"{'-'*math.ceil((x_len+1-len(self.name))/2)}{self.name}{'-'*(math.ceil((x_len-len(self.name))/2)+1)}\n"
        for i in self.lines:
            ret+=f"|{i}{' '*(x_len-len(i))}|\n"

        return ret+"-"*(x_len+2)
