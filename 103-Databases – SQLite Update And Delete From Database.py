# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

import sqlite3

db = sqlite3.connect("app.db")

# setting up the cursor 
cr =db.cursor()


#insert data 
# cr.execute("create table if not exists  users(user_id integer,name text)")
# cr.execute("insert into users(user_id,name) values(1,'Motasem')")
# cr.execute("insert into users(user_id,name) values(2,'Naima')")
# cr.execute("insert into users(user_id,name) values(3,'Mohammed')")

## update Data

# cr.execute("update users set name =' Mahmoud' where user_id = 1 ")
# cr.execute("update users set name = 'Naima' where user_id = 2 ")
# cr.execute("update users set name = 'Mohammed' where user_id = 3  ")



#Fetch data
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

## delete data 
# cr.execute("delete from users ")
## delete all data 
cr.execute("delete from users where user_id =4")

# cr.execute("delete from users where user_id = 2")

# print(cr.fetchall())
# print(cr.fetchmany(2))
print("^"*30)




db.commit()

db.close()