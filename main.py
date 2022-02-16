import src.ArgummentParser.argummentparser as argummentparser
from sys import argv
from src.backend import ListHandler as ListHandler
from src.frontend import UI as UI
def main():
    arg_parser=argummentparser.ArgummentParser(["show","add"])
    arg_parser.add_flag("list",1)

    command,flags=arg_parser.parse(argv[1:])
    ui=UI()
    match command:
        case "show":
            list_handler=ListHandler(flags["--list"][0])
            print(ui.format_list(list_handler.get_tasks()))
    










if __name__=="__main__":
    main()

