##-----------------------------------------------##
##-------- Practical Membership Control  --------##
##-----------------------------------------------##

#login 
name = input('what\'s your name? ').strip().capitalize()
admins= ["Ahmed","Motasem","Mai"]


if name in admins:
    print(f"Welcom Admin : {name} ")
    option = input("Delete or update yur name ? ").strip().capitalize()
    print(option)
    name_index=int(admins.index(name))


    if option == 'Update':
        newName = input("Enter your new name please? ").strip().capitalize()
        admins.append(newName)
        adindex=(admins.pop(name_index))
        print(f"Great your New name is : {newName} ")
        print(f"here is the list of the names of the admins :\n{admins}")
    elif option == 'Delete' or option == 'D' : 
        sure=input("Are you sure you wanna delete your name ?Yes/no ").strip().lower()
        if sure == 'yes' or sure == 'y':
            admins.pop(int(admins.index(name))) # we cann just put in adindex 
            print(f"your name is removed from admin list{admins} ")
        elif sure=='no' :
            print(f"Fine {name} you will remain as an admin :)) ")
    else :
        print("Wrong option . please write it again")

elif name not in admins :
    print(f"Hello {name} you are not an admin")
    sue=input("would you like to be added as an admin ?Yes/no ").strip().lower()
    if sue == "yes" :
             admins.append(name)
             print(f"Congrats {name} you became an admin {admins}")
    elif sue == "no" :
            print("Thank you and enjoy ")
