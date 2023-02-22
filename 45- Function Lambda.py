## ---------------------------- ##
## ---- Function => Lambda ---- ##
## --- Anonymous Function ----- ##
## ---------------------------- ##

# [1] It has no name 
# [2] You can call it inline without defining it 
# [3] You can use it in Return Data from another function
# [4] [ Lambda ] is used for simple functions and [ def function ] handle the large tasks 
# [5] Lambda function is one single expression not a block of code 
# [6] Lambda Type is function
# ----------------------------------------------------------


def say_hello(name,age ):return f"Hello {name} your age is {age}"

Hello = lambda name,age : f"Lambda Hello {name} your age is {age}"


print(say_hello ("Motasem",16))
print(Hello("Motasem ",40))

print(say_hello.__name__) # its name is say_hello
print(Hello.__name__)     # its name is <lambda> annynomous
print(type(Hello))


area = lambda  radius  :  f" area = {3.14 * radius**2} "

print(area(radius=10))
