
import os

import iluxaMod as ilm

database = ilm.postgreSQL_connect(user="postgres", 
    password="armageddon", 
    database="powersport", 
    host="illyashost.ddns.net")

sql = database.sql
db = database.db

ILMtools = ilm.tools()
pick = ILMtools.pick
unpick = ILMtools.unpick

FILESLIST = []

class SysFunc:
    def __init__(self):
        pass
    
    def file_not_exists(self, file_name):
        return filename not in os.listdir()
    
    def create_files(self):
        for filename in FILESLIST:
            if self.file_not_exists(filename):
                pick(filename, [])
                
    
    