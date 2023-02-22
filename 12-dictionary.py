## ---------------------- ##
## ----- Dictionary ----- ##
## ---------------------- ##
# - - - - - - - - - - - - - 
# [1] Dict items are enclosed in curly Braces 
# [2] Dict items are Contains Key : value
# [3] Dict key need to be immutable = > ( Numbers , String, Tuple) list Not Allowed
# [4] Dict valuse can have any Data Type 
# [5] Dict Key Nedds to be unique 
# [6] Dict not ordered you access , You Access its elements with Key 
# - - - - - - - - - - - - - 

# Dictionary 

user = {                 # we can ass list in a dict .. but a tuple is fine 
 "name" : "Osama",
 "age" : 36,
 "country" :"Egypt",
 "Skils" : ["Hive","HADOOP","KAFKA"],
 "Rating": 10.5 
}
print(user)
print(user["country"]) # Egypt 
print(user.get("country"))

# print all keys 
print(user.keys())
#print all values 
print(user.values()) 

# Two dimentional dictionary (Nested dict) 
langaugaes ={
    "first":{
        "name":"hive",
        "progress":"90%"
    },
    "second":{
        "name":"Hadoop",
        "progress": " 905"
    },
    "third":{
        "name":"Kafka",
        "progress": " 80%"
    }
}

print(langaugaes['first']["name"]) #Hive
print(f"First :  {langaugaes['first']}")
#dictionary length 
print(len(langaugaes))
print(len(langaugaes["third"]))

# create Dictionary from variables 

frameworkOne= {
    "name":"Vuejs",
    "progress":"805"
}

frameworkTwo={
    "name": "Angular",
    "progress":"70%"

}

frameworkThree={
    "name":"reactjs",
    "progress":"905"
}

allframework = {
    "one":frameworkOne,
    "two":frameworkTwo,
    "three":frameworkThree
}
print(f"All Frame Works : {allframework}")