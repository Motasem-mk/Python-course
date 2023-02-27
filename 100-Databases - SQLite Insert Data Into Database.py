# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------


# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

#setting up the cursor 
cr = db.cursor()

#create the Tables and fields 
cr.execute("create table if not exists users(user_id integer , name text)")
cr.execute("create table if not exists skills(name text,progress integer,user_id integer)")


# inserting data 

# cr.execute("insert into users(user_id, name)values (1,'Motasem')")
# cr.execute("insert into users(user_id,name) values (2,'Osama')")
# cr.execute("insert into users (user_id,name) values (3,'Ali')")

my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]

for key ,user in enumerate( my_list,1) : 
    cr.execute (f"insert into users (user_id,name) values ({key},'{user}')")



## Save (commit) changes 
db.commit() 

#close database 
db.close()