class ParseError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "ParseError"

class Flag:
    def __init__(self,flag:str,options:int,second_flag=None,flag_symbol="-"):
        self.flag=flag
        self.second_flag=second_flag
        self.options=options
        self.symbol=flag_symbol
    
    def check(self,to_check:str)->bool:
        if to_check==self.symbol*((len(self.flag)>1)+1)+self.flag:
            return True
        elif self.second_flag!=None and to_check==self.symbol*((len(self.second_flag)>1)+1)+self.second_flag:
            return True
        else:
            return False

    def __str__(self):
        return self.symbol*((len(self.flag)>1)+1)+self.flag

class ArgummentParser:
    def __init__(self,commands:list):
        self.commands=commands
        self.flags=[]

    def add_flag(self,flag:str,options:int,second_flag=None):
            self.flags.append(Flag(flag,options,second_flag))

    def parse(self,to_parse:list):
        x=0
        ret_command=None
        ret_flags={}
        while x<len(to_parse):
            aktuell_arg=to_parse[x]
            valid=False
            if aktuell_arg in self.commands and ret_command==None:
                ret_command=aktuell_arg
                x+=1
                valid=True

            for flag in self.flags:
                if flag.check(aktuell_arg):
                    ret_flags.update({str(flag):to_parse[x+1:x+2+flag.options]})
                    x=x+1+flag.options
                    valid=True
                    break

            if valid:
                pass

            else:
                print(to_parse[x])
                raise ParseError
        return ret_command,ret_flags
