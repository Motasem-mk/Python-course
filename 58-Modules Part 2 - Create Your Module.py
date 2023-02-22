# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys

#print(sys.path)  # it will show all the paths 
# import os 

# print(os.getcwd()) 


# # i can append any path=>> /Users/elkihale.n-abualqumboz.mk/Desktop
# sys.path.append(r"/Users/elkihale.n-abualqumboz.mk/Desktop/osama.txt" )  
# print("^"*30)
# print(sys.path)

# import elzero 
# print(dir(elzero))
# elzero.say_hello("Motasem")
# elzero.say_howRu("Motasem")
####################################################

# import elzero as ee ## its an Alias .. if the name of the module is big i can shorten it 

# print(dir(ee))
#  ## these are the functions i created  [ 'say_hello', 'say_howRu']
# ee.say_hello("Motasem")
# ee.say_howRu("Motasem")
# ee.say_hello("Naima")


## we can also import a function from the module like the previous video 

# from elzero import say_hello 

# say_hello("Motasem")

## alias for the function 

from elzero import say_howRu as hru
hru("Motasem")