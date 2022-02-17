from src.argummentparser import ArgummentParser
from sys import argv
from src.listhandler import ListHandler
from src.ui import UI
from src.settingshandler import SettingsHandler
from os.path import expanduser

def main():
    arg_parser=ArgummentParser(["show","add"])
    arg_parser.add_flag("list",1)
    arg_parser.add_flag("state",1)
    
    settings_handler=SettingsHandler(f"{expanduser('~')}/.todo-list/config.yaml")
    command,flags=arg_parser.parse(argv[1:])
    settings=settings_handler.get_settings()

    ui=UI(settings)
    match command:
        case "show":
            if "--state" in flags:
                state=int(flags["--state"][0])
            
            else:
                state=None
            list_handler=ListHandler(flags["--list"][0],settings["list_folder"])
            ui.print_list(list_handler.get_tasks(state))
    

if __name__=="__main__":
    main()
