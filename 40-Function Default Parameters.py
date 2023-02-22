##--------------------------------------##
##---- Function Default Parameters -----##
##--------------------------------------##


def say_hello(name,age,country):
    print(f"Hello {name} your age is {age} ,you are from {country}")

say_hello ("Motasem", 40,"Palestine")
say_hello ("Osama" , 38 ,"Egypt" )

# say_hello("Ali", 30) 
#  error one argument missing 
# some times i don't need all argument to be entered 
# i can use default parameters 
# the default parameter has to be the last  , if it is one default 
# we can set all parameters to default 


def say_hello_default(name = "unknown",age="unknown",country="unknown" ):
    print(f"Hello {name} your age is {age} ,you are from {country}")

say_hello_default("Mohammed", 75,"Palestine")
say_hello_default("Motasem",40)
say_hello_default("Rami")
say_hello_default(25,"KSA")
say_hello_default()
#Hello Mohammed your age is 75 ,you are from Palestine
# Hello Motasem your age is 40 ,you are from unknown
# Hello Rami your age is unknown ,you are from unknown
# Hello 25 your age is KSA ,you are from unknown
# Hello unknown your age is unknown ,you are from unknown

