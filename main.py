import src.ArgummentParser.argummentparser as argummentparser
from sys import argv
from src.backend import ListHandler as ListHandler
from src.frontend import UI as UI
def main():
    arg_parser=argummentparser.ArgummentParser(["show","add"])
    arg_parser.add_flag("list",1)
    arg_parser.add_flag("state",1)
    command,flags=arg_parser.parse(argv[1:])
    ui=UI()
    match command:
        case "show":
            if "--state" in flags:
                state=int(flags["--state"][0])
            else:
                state=None
            list_handler=ListHandler(flags["--list"][0])
            ui.print_list(list_handler.get_tasks(state))
    










if __name__=="__main__":
    main()

