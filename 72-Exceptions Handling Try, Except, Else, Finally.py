# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------


try : # Try the code and test the error

    number =int(input("eneter your number : "))
    print("Good this is integer from try ")

except: # Handle the error if its found 
   print("Bad this is not integer from exception")

else :  # if there  is no error 
    print("Good this is integer from else")

finally : #
    print("Print from finally whatever happened")


#####################################################



try :
#    print(10/0)
#    print(int("Hello"))
   print(x)

except ZeroDivisionError : 
 
    print("Can't be divided .. from Motasem")

except ValueError:
    print("Value error this is not integer .. from Motasem")

except NameError:
    print("name error .. identifier not found .. from Motasem")

except :
    print("Error found from Motasem ")

