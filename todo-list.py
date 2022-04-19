#Copyright (C) 2022 Jonas Lütolf
#imports from src
from src.argummentparser import ArgummentParser
from src.listhandler import ListHandler
from src.ui import UI
from src.settingshandler import SettingsHandler

#imports from std libary
from os.path import expanduser
from sys import argv

#exceptions
class NoCommandError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"NoCommandError no command found in the call"

class FlagNotFound(Exception):
    def __init__(self,flag_name):
        super().__init__()
        self.flag_name=flag_name

    def __str__(self):
        return f"FlagNotFound: falg {self.flag_name} not found"


def parse_args()->tuple:
    arg_parser=ArgummentParser(["show","add-task","delete-task","change-state"])
    arg_parser.add_flag("list",1,"l")       
    arg_parser.add_flag("state",1,"s")      
    arg_parser.add_flag("folder",1,"f")     
    arg_parser.add_flag("task",1,"t")   
    return arg_parser.parse(argv[1:])

def main()->None:
    command,flags=parse_args()

    #load settings
    settings_handler=SettingsHandler(f"{expanduser('~')}/.todo-list/config.yaml")
    settings=settings_handler.get_settings()
    
    #make ui
    ui=UI(settings)
    
    if command==None:
        raise NoCommandError()
    
    #set folder path
    if "--folder" in flags:
        folder=flags["--folder"][0]
    else:
        folder=settings["list_folder"]
    
    #open list
    if "--list" in flags:
        list_handler=ListHandler(flags["--list"][0],folder)
    else:
        raise FlagNotFound("--list")
    
    #execute command
    match command:
        case "show":
            #set state
            if "--state" in flags:
                state=int(flags["--state"][0])        
            else:
                state=None

            ui.print_list(list_handler,state)

        case "add-task":
            new_task_data=ui.ask_task_informations()
            list_handler.add_task(new_task_data["name"],new_task_data["description"],new_task_data["state"])
        
        case "delete-task":
            list_handler.delete_task(flags["--task"][0])

        case "change-state":
            if "--state" in flags:
                state=int(flags["--state"][0])
            else:
                state=1
                
            if "--task" in flags:
                list_handler.change_state(flags["--task"][0],state)
            else:
                raise FlagNotFound("--task")
    
    #write list
    list_handler.write()   

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print(exc)
