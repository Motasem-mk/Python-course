# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 4 --
# -----------------------------------------------------

## import sqlite3

import sqlite3

#create data base and connect 
db = sqlite3.connect("app.db")

# setting up the cursor 
cr= db.cursor()

## create table and schemma :
cr.execute("create table if not exists skills (name text,progress integer , user_id integer) ")


def commit_and_close():
    '''Commit changes and close connection to Database'''  
    db.commit() #save (commit) changes 
    db.close()   # close Database
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

    cr.execute(f"select * from skills where user_id ={uid} ")

    results = cr.fetchall()

    print(f"you have {len(results)} skills ")

    if len(results)>0:
      
      print("showing skills with progress")

    for row in results :

        print(f"skill :{(row[0]).center(7)}, progress : {(row[1])}, user_id: {row[2]} ")

    

def add_skill():

    sk = input("write skill name: ").strip().capitalize()

    cr.execute(f"select name from skills where name ='{sk}' and user_id = '{uid}'")

    results= cr.fetchone()

    if results!=None:

        print(f"{sk} is already existed in the Database, you can't add it twice")
        answer = input("would you like to update it?yes/no  ").strip().lower()
        
        if answer == "yes" :
            update_skill()
        else :
          print(" No problem ")
    
          
    else :
        
        print(f"{sk} is a new skill that will be added to your database")

        prog= input("write  skill progress: ").strip()

        cr.execute(f"insert into skills (name,progress,user_id) values ('{sk}','{prog}','{uid}')")

    #commit_and_close()

def delete_skill():
    sk = input("write skill name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = {uid} ")
    

def update_skill():
    sk = input("Enter the skill: ").strip().capitalize()
    prog = input("Eenter the progress: ")
    cr.execute(f"update skills set progress =  '{prog}' where name = '{sk}' and user_id = '{uid}'")
   

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

    commit_and_close()

else :
    print(f"Sorry this command \"{user_input}\"  is not found ")