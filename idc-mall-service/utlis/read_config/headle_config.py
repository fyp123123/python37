from configparser import ConfigParser
from utlis.project_path.item_path import *
import os

class Headle_config(ConfigParser):
    def __init__(self,filename):
        super(Headle_config,self).__init__()
        self.filename=filename
        self.read(self.filename)
    def get_value(self, section, option):
        value=self.get(section,option)
        return value
config=os.path.join(config_path,"config_ini")
# a=Headle_config(config)
# print(a.get_value("data","usename"))