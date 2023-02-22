## -------------------------------- ##
## ------------ Boolean ----------- ##
## ------- Boolean Operators------- ##
## -------------------------------- ##

# [1] In programming you need to know your if code output is a True or False   
# [2] Boolean Values are the two constant objects [True and False]
# 

Name= " "
print(Name.isspace())
print("="*30)
print(100>200)
print(200<20)
print(20>3)
print("="*30)
# Built is methods bool()
# True Values
print(bool("Osama"))
print(bool(100))
print(bool([1,2,3,4]))
print(bool({"name":"Motasem","Age":39}))
print(bool( True))
print("="*30)
# False values
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(False))
print(bool(None))
print("="*30)

## -------------------------------- ##
## ------- Boolean Operators------- ##
## -------------------------------- ##
# [1] and
# [2] or 
# [3] not

# and  all conditions must be true 
age = 40 
country = "Palestine"
rank = 10

print(age>16 and country=="Palestine" and rank >2) # True
print(age>16 and country=="Egypt" and rank >2) # False
print("="*30)

# or at least has to meet one condition

print(age>16 or  country=="KSA" or rank >2)  # True
print(age>50 or  country=="KSA" or rank >20) # False
print("="*30)

# not 

print(age>16) # True
print(not age>16) # not true == false

