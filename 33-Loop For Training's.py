## -------------------- ##
## --- Loop => For ---- ##
## ---- Training's ---- ##
## -------------------- ##

# #Range
# myrange = range(1,101) #built in  function 

# for number in myrange :
#     print(number)


### Dictionary
print("My skills  : My Progress ")
myskills = {
    'HIVE': 90,
    "HADOOP" : 99,
    'KAFKA' : 80,
    'HBASE' : 30
}

# print(myskills["KAFKA"])
# print(myskills.get("HBASE"))

# for skill in myskills : 
#     print(skill) 
i=0
for skill in myskills:
    i+=1 # for sequence number 
    print(f"{i}-{skill.center(6, )}   : {myskills[skill]}")
                                       # myskills.get(skill)
    
