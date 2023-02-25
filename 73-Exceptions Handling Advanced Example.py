# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------

the_file = None
tries= 5 

while tries > 0 :
  
  try:  #try to open the file  
    print("Enter the file name with absolute path : ")
  
    print(f"You have {tries} tries left")
    print("Example : /Users/elkihale.n-abualqumboz.mk/Desktop/Elzero  ")
    file_Name_and_Path = input("Enter theFile name : ").strip()
    the_file = open(file_Name_and_Path,"r")
    print(the_file.read())
    break
  except FileNotFoundError :
    print("File not found please add the correct path ")

    tries -=1
  except:
    print("Error found")

  finally:
    if the_file is not None: 
       the_file.close()
       print("File closed")
    

else :
  
  print("All tries is done ")

######### doing the same with for instead of while 


# import os 
# print(os.getcwd())
# print(os.path.abspath(__file__))
# # myfile = open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/Motasemmk.txt","a")

# # myfile.write("\nHello this is a new line")

 
myfile = None
tries = 5 
for i in range(tries):

    if tries > 0 :

        try :
            print("Enter the link of your file to open ")
            print(f"Youe have {tries-i} tries left")
            print("Example : /Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python ")
            file = input("enter the file : ").strip()
            myfile = open(file)
            print(myfile.read())
            break 
        except FileNotFoundError:
            print("File not found error please enter the correct path ")
        except:
            print("Error ")
        
        finally :
            if myfile is not None:
               myfile.close()
               print("\nFile closed")

else:
    print("Tries finished")
