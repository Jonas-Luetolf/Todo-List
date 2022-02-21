from src.argummentparser import ArgummentParser
from sys import argv
from src.listhandler import ListHandler
from src.ui import UI
from src.settingshandler import SettingsHandler
from os.path import expanduser

def main()->None:
    #parse argumments
    arg_parser=ArgummentParser(["show","add-task"])
    arg_parser.add_flag("list",1,"l")
    arg_parser.add_flag("state",1,"s")
    arg_parser.add_flag("folder",1,"f")
    command,flags=arg_parser.parse(argv[1:])

    #load settings
    settings_handler=SettingsHandler(f"{expanduser('~')}/.todo-list/config.yaml")
    settings=settings_handler.get_settings()

    ui=UI(settings)
    if "--folder" in flags:
        folder=flags["--folder"][0]
    else:
        folder=settings["list_folder"]


    match command:
        case "show":
            if "--state" in flags:
                state=int(flags["--state"][0])        
            else:
                state=None

            list_handler=ListHandler(flags["--list"][0],folder)
            ui.print_list(list_handler,state)

        case "add-task":
            list_handler=ListHandler(flags["--list"][0],folder)
            new_task_data=ui.ask_task_informations()
            list_handler.add_task(new_task_data["name"],new_task_data["description"],new_task_data["state"])
            list_handler.write()   

if __name__=="__main__":
    main()
