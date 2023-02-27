# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

db = sqlite3.connect("app.db")

cr =db.cursor()

# cr.execute("create table if not exists  users(user_id integer,name text)")
# cr.execute("insert into users(user_id,name) values(1,'Motasem')")
# cr.execute("insert into users(user_id,name) values(2,'Naima')")
# cr.execute("insert into users(user_id,name) values(3,'Mohammed')")

cr.execute("select * from users")

print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# print(cr.fetchall())
# print(cr.fetchmany(2))




db.commit()

db.close()