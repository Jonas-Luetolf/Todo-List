import src.ArgummentParser.argummentparser as argummentparser
import sys
def main():
    arg_parser=argummentparser.ArgummentParser(["show"])
    arg_parser.add_flag("l",1)
    print(arg_parser.parse(sys.argv[1:]))

main()
