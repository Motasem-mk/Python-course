# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------


## import main module 

# import random
# # print(random)

# print(f"print random float number{random.random()} ") # it will print a random number
# # random is a function 
# # .random() is a method insode the module  
# #---------------------------------------------------------------------------------------#
# # show all functions inside the module 

# print(dir(random)) 

# to import one or two functions from the module 
from random import randint ,randrange ,random # i can import more than one functions 
                                                ##from a module 
                                                
### [ from random import * ] =>> to import all the function from the module  

print(f"Print Random integer {randint(100,900)}")

print(f"Print Random range {randrange(100,900)}")

print(f"Print Random float  {random()}")


