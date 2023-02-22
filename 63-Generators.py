# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():
    
    yield 1
    yield 2
    yield 3
    yield 4

print(myGenerator())  # <generator object myGenerator at 0x108f31d90>
myGenerator() # it will not work automatically 

myGen = myGenerator()

print(next(myGen))
print("Hello ")
print(next(myGen))
# print(next(myGen))
# print(next(myGen))
print("^"*30)

for number in myGen: #here it will not give anything because i called all the yield from the next()
    print(number)      # but if i remove two print(next()) i will have two more number to come from the loop 
                       # it will start from where it stopped 


