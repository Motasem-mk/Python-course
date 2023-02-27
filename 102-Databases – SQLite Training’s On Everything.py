# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------

import sqlite3

def get_all_data():
  
   try :
      
    #connect to database 
    db=sqlite3.connect("app.db")
    
    # print sucess message
    print("connected to database successfully ")

    # setting up the cursor 
    cr=db.cursor()

    #Fetch data from database 
    cr.execute("select * from users")

    #Assign data to variable 

    results = cr.fetchall()

    # print numbers of rows
     
    print(f"Database has {len(results)} Row")

    ## printing message 

    print("show Data")

    ## loop on results 

    for row in results :
      print(f"User_ID : {row[0]}",end=" ")
      print(f"User name : {row[1]}")


   except :
     print("error")

   finally : 
     if (db):
       db.close()
       print("Database is closed ")

get_all_data()