#Copyright (c) 2022 Jonas Lütolf 
from os.path import isfile,isdir, expanduser
from os import mkdir
import yaml
DEFAULTCONFIG=f"""
check_symbol: "✓" 
open_symbol: "✗"
list_folder: "{expanduser('~')}/.todo-list/" 
"""

class InvalidSettings(Exception):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "InvalidSettings: config file is invalid"

class SettingsHandler:
    def __init__(self,path:str)->None:
        self.path=path

    def get_settings(self)->dict:
        #load config from file
        load_data=self.open_config()
        if self.valid_settings(load_data):
            pass

        #load default config
        else:
            self.set_backup_config()
            load_data=self.open_config()

        return load_data

    def open_config(self)->dict:
        if isfile(self.path):
            with open(self.path,"r") as f:
                data=yaml.load(f.read(),Loader=yaml.FullLoader)
        else:
            data=None

        return data

    def set_backup_config(self)->None:
        try:                                     
            mkdir(self.path[0:len(self.path)-(list(reversed(self.path)).index("/"))])
        except FileExistsError:                  
                pass

        f=open(self.path,'w')
        f.write(DEFAULTCONFIG)                   
        f.close()                                

    def set_settings(self,data:dict)->None:
        if self.valid_settings(data):
            with open(self.config_path,"w") as f:
                f.write(yaml.dump(data))
        else:
            raise InvalidSettings
    
    @staticmethod
    def valid_settings(data:dict)->bool:
        ret:int=0
        ret+=int(type(data["open_symbol"])==str)
        ret+=int(type(data["check_symbol"])==str)
        ret+=int(isdir(data["list_folder"]))
        return ret==3
