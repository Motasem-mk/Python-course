##-----------------------------------##
## ----- Loop - While Training ----- ##
## ----- sIMPLE password Guess ----- ##
##-----------------------------------## 


thePassword = "Palestine@1948"

tries = 3

# My way 
# while tries > 0 :
#     password = input("Enter your Password : ")

#     if thePassword != password :
#         tries-=1
#         # if tries ==1:
#         #     print("Wrong password , this is your last try")
#         # else :
#         print(f"Wrong password\nYou have {'Last' if tries ==1 else tries} tries left")
#         if tries ==0:
#             print("All tries finished , youre blocked , contact us to unblock you  ")
#     else: 
#         print("Youre logged in ") 

#         break

### Elzero way 
password = input("Enter your Password : ")


while thePassword!= password :
    tries -=1
   
    password = input("Enter your Password : ")

    print(f"wrong password , you have {tries} chance left")
    
    if tries ==0:
        print("all chances finished ,\nyou are blocked , \nplease contact us to restore your account ")
        break 
else :
    print("You're logged in")