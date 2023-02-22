##- - - - - - - - - - - - -  - - - - - - ##
##  - - -  Dictionary methods 1  - - - -  ##
##- - - - - - - - - - - - -  - - - - - - ##

# .clear()
user = {
    "name":"Motasem",
    "Age":40
}
print(user)
user.clear()
print(user)
print("^"*30)

#update
member  = {
    "name":"Motasem"
     }

print(member)

# to update 
member["AGE"]=40
print(member)
print("^"*30)

# another way to update 
member.update({"Skills":{"Languages":["HIVE","HADOOP","KAFKA"],"Tools":["AWS","AZUR"]}})
print(member)

# copy 

b=member.copy()
print(f"New copied {b}")
print("^"*30)
member.update({"country":"Palestine"})
print("^"*30)
print(member)
print("^"*30)
print(b) # shallow copy 
print("^"*30)
# keys and values 

print(member.keys())
print(member.values())
print("Skills :Langugae :: ",member["Skills"]["Languages"])