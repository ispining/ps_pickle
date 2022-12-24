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

for filename in FILESLIST:
    pass
    
    