import sqlite3

def get_all_info():

    try :
        # connect to database 

        db=sqlite3.connect("app.db")
        print("successfully connected to database")
        cr=db.cursor()

         #fetchall
        cr.execute("select * from users")
        
        result =  cr.fetchall()

        for user in result : 
            print(f"Id({user[0]}) name: {user[1]}")
  
        db.commit()
    except sqlite3.Error as er:
        print(f"error reading Data {er}")

        print("error")
    finally:
      db.close()
      print("database closed")


get_all_info()