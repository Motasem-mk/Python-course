# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

def myDecorator(func) : # the parameter is a function 

    def nestedfunc():   

        print("Before") # Message from decorator 

        func()   ## excute the function that i use as a parameter

        print("After")# Message from decorator 

    return nestedfunc  ## return all data 

@myDecorator
def say_hello():
    print("Hello from say hello function ")

say_hello()


print("^"*30)


@myDecorator
def message ():
    print("Hello from message")

message()

# afterDecoration = myDecorator(say_hello)

# afterDecoration()



 