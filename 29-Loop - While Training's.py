##-----------------------------------------##
##------- Loop - While Training's ---------##
##-----------------------------------------##
#    While condition is True 
#    => Code will Run until condition becomes False

My_friends = ["Tawfiq", "Diab", "Imad", "Mohammed", "Salem", "Wisam", "Farghaly", "Ra'fat", "Mai", "Shaima"]

i =0  #index iterator 
while i < len(My_friends):
    print(f"#{str(i+1).zfill(2)}. {My_friends[i]}")
    i+=1
else :
    print("All friends printed to the screen")

