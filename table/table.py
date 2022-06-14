from table.edge import Edge
class Table:
    def __init__(self)->None:
        self.columns=[]

    def add_column(self,column)->None:
        self.columns.append(column)
    
    def clear(self)->None:
        self.columns=[]
    
    def __str__(self)->str:
        x_lens=list(i.get_x_len()+2 for i in self.columns)
        lines=[]
        anz_columns=0
        for i in self.columns:      
            for index,line in enumerate(i):
                tabs=""                
                if index>=len(lines):
                    lines+=(list("" for i in range(0,index+1-len(lines))))
                    tabs="".join(list(" "*i for i in x_lens[0:anz_columns]))
                
                if anz_columns!=0: 
                    line=line.replace(Edge.LEFTTOP,Edge.TOPMIDDLE)
                    line=line.replace(Edge.LEFTBOTTOM,Edge.BOTTOMMIDDLE)

                lines[index]=lines[index][:-1]+"".join(tabs+line)
            anz_columns+=1
        ret=""
        for line in lines:
            ret+="".join(line)
            ret+="\n"
        return ret[:-1]
