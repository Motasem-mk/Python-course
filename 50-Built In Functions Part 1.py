## --------------------------------- ##
## --- Built In Functions Part 1 ----##
## --------------------------------- ##

# all()
# any()
# bin()
# id()


# [1] all() # iterable list , tuple , dict 

# x= [1, 2, 3, 4,[]]

# if all(x):  ## if all elements in x are true 
#     print("All element is true ")

# else :
#     print(" There's at least one element is false")


# [2]  any()
# y= [0,0,False]
# if any(y): 
#     print("there is at least one  Trure element ")

# else : 
#     print("There is no True elements .. all are false ")

# [3] bin()
## return binary number 

print(bin(100))

# [4] id()
## the id the address of the object whwre the variable stored in the memory 

a= 1
b= 2

print(id(a)) # id = 4553982192
print(id(b)) # id = 4553982224