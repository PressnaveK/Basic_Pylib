from _datetime import datetime as td
from time import sleep as t

import sqlite3
#if Db.db already exist , it will be overwritten . Else it will be created
connection = sqlite3.connect('Db.db')

#Creating Db implementor
c = connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Sample( Time_stamp TEXT  , num INT)')
connection.commit()

num = 0

while(num < 6):
    num += 1
    current_Time = td.now()
    t(2)
    c = connection.cursor()
    c.execute("INSERT INTO Sample VALUES (?, ?)",(current_Time,num))
    connection.commit()

print("Entered Sucessfully")
connection.close()




