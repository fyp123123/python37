import os
from utlis_存放路径.handle_path import *
from configparser import ConfigParser

class Handle_conf(ConfigParser):
    def __init__(self,filename):
        super(Handle_conf,self).__init__()
        self.filename=filename
        self.read(self.filename)
    def get_value(self,section,option):
        value=self.get(section,option)
        return value

conf_ini_path=os.path.join(conf_path,"conf.ini")
Conf=Handle_conf(conf_ini_path)
print(Conf.get_value("project","headers"))




