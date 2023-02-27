# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

## import SQLite Module 

import sqlite3

# create Database and connect 
db = sqlite3.connect("app.db")


# create the table and the fields 
db.execute("create table if not exists skills(name text,progress integer,user_id integere)")

# close database 
db.close()