import src.ArgummentParser.argummentparser as argummentparser
import sys
from src.backend import ListHandler as ListHandler
from src.frontend import UI as UI
def main():
    arg_parser=argummentparser.ArgummentParser(["show"])
    arg_parser.add_flag("list",1)
    command,flags=arg_parser.parse(sys.argv[1:])
    match command:
        case "show":
            list_handler=ListHandler(flags["--list"][0])
            ui=UI(list_handler)
            ui.start()
            

main()
