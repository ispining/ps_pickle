import iluxaMod as ilm

database = ilm.postgreSQL_connect(user="postgres", 
    password="armageddon", 
    database="powersport", 
    host="illyashost.ddns.net")

sql = database.sql
db = database.db


