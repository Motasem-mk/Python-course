##- - - - - - - - - - - - -  - - - - - - ##
##  - - -  Dictionary methods 2  - - - - ##
##- - - - - - - - - - - - -  - - - - - - ##

print("^"*30)

# setdefault()
user={
    "name":"Motasem"
}
print(user)
print(user.setdefault("name","osama")) # because there is value ti the name it didnt update it 
print("^"*30)
print(user)
user.setdefault("age",36) # it will update , add the key age and its value
print(user)
print("^"*30)
user.update({"country": "Palestine"}) #.update({"country":"Palestine"})
print(user)
user.setdefault("skills") # value of skills is none 
print("^"*30)
print(f"user: {user}")
# .popitem()

print("^"*30)
print(f"popitem is : {user.popitem()}") # popitem it take out the last item from the dict 
print(user)           # unlike in list you can specify which index you wanna remove 
print("^"*30)
# .items == copy but not shallow 
student={
    "name":"Motasem",
    "age":40
}
print(student)
allitems = student.items()
print(allitems)
print("^"*30)
student.update({"country":"Palestine"})
print(student)
print("^"*30)
print(allitems)
print(type(allitems))
print("^"*30)

# from keys create dict from two variables keys and values 
a= ["name","country","age"] # we can use list here because t is an iterable and it will not be as a list in the new Dict 
b="x"
newDict=dict.fromkeys(a, b)
print(newDict)
print(type(newDict))
newDict["name"]="Motasem"
print(newDict)