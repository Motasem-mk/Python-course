# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 2 --
# -----------------------------------------------------

## import sqlite3

import sqlite3

#create data base and connect 
db = sqlite3.connect("app.db")

# setting up the cursor 
cr= db.cursor()

## create table and schemma :
cr.execute("create table if not exists skills (name text,progress integer , user_id integer) ")

## commit and close method 

def commit_and_close():

    #save (commit) changes 
    db.commit()

    # close Database
    db.close()
    print("Connection to Database is closed ")

## my user id 
uid = 2



## input bog message 
input_message = '''
what do you want to do ?
"s" => Show all Skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update skill progress
"q" => Quit The App
choose Option : 
'''

# Input option chosse 
user_input = input(input_message).strip().lower()

##command List : 
commands_list = ["s", "a", "d", "u", "q"] 

## defind the methods 
def show_skills():
    cr.execute("select * from skills")
    print(cr.fetchall())
    commit_and_close()

def add_skill():
    sk = input("write skill name: ").strip().capitalize()
    prog= input("write  skill progress: ").strip()
    cr.execute(f"insert into skills (name,progress,user_id) values ('{sk}','{prog}','{uid}')")

    commit_and_close()

def delete_skill():
    sk = input("write skill name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = {uid} ")
    commit_and_close()

def update_skill():
    print("Update skill progress")
    commit_and_close()

## check if command is exist 

if user_input in commands_list:

    #print(f"commands found {user_input}")

    if user_input == "s":

        show_skills()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()

    else :

        print("App is closed")

else :
    print(f"Sorry this command \"{user_input}\"  is not found ")