## ------------------------ ##
## ----- Loop => For ------ ##
## ------------------------ ##
#----------------------------
# for items in iterable_object : 
#  Do something with itemm
#--------------------------------------------------------------------------------------#
# item is a variable you create  and call whenever you want 
# item refer to the current position and will run and visit all items to the end 
# iterable_object => sequence [ list,tuples,set ,dict,string of characters ,etc...]
#--------------------------------------------------------------------------------------#

num = [1,2,3,4,5,6,7,8,9,10]

for n in num:
    #print(n*10)
    if n%2 == 0:
        print(f"{n} is an even number ")
    else :
                print(f"{n} is an odd number ")


else:
    print("lOOP IS FINISHED")

name = "Motasem"
for letter in name : 
    print(letter)

