## ------------------------ ## 
## -- Built In Functions -- ##
## ------------------------ ##

# enumerate()
# help()
# reversed()
# ------------------------ ## 


# enumerate(iterable, start=0) start by  default from  zero 

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills,20)
print(type(mySkillsWithCounter)) # <class 'enumerate'>

for co , sk in mySkillsWithCounter :
    print(f"{co} : {sk} ")

print("^"*30)
for counter , skill in enumerate(mySkills): ## it will start from 0 .
    print(f"{counter}: {skill}")

# help()

# print(help(print)) 
print("^"*30)


# reversed(iterable)
 
myString = "Motasem Mohammed Abu Alqumboz"
print(f"Reversed :::  {reversed(myString)}")
print("^"*30)
for letter in reversed(myString):

  print(letter)

print("^"*30)

myTools= ["HIVE", "HADOOP", "KAFKA", "PYTHON"]
for count,t in enumerate( reversed(myTools),1):
   print(f"{count}: {t}")
print("^"*30)
for l in reversed("Motasem"):
   print(f"{l}",end="")