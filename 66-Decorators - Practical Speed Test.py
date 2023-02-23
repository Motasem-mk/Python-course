# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------


def myDecorator ( func):
    
    def nested_func(*numbers):  # unpack to have many parameter 

        for number in numbers:

            if number < 0:

                print("There is at least one number less than zero ")

        func(*numbers)

    return nested_func

@myDecorator
def calcuate (*numbers):
    total = 0
    for number in numbers :
        total+=number
    
    return print(f"Total = {total}")

calcuate(1,3,4,65,7,-1)

from time import time 
##  speed test 

def speed_test(func):

    def wrapper ():

      start = time()
       
      func()

      end=time ()

      print(f"Functionrunning time is {end-start}")
    
    return wrapper

@speed_test
def bigLoop():
    for number in range(1,20000):
        print(number)

bigLoop()