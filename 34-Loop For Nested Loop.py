## ----------------------- ##
## ----- Loop => For ----- ##
## ----- Nested Loop ----- ##
## ----------------------- ##

########### when you loop the dictionary it gives you the key #######

# peoples = ["Motasem","Osama","Ahmed","Sayed","Ali"]

# skills = ["HADOOP" , "HIVE", "KAFKA"]

# for name in peoples :
#     print(f"{name} skills is : ")
#     for skill in skills:
#         print(f"- {skill}")


people = {
 
    "Motasem" :  {
        "HBASE":"90%",
        "Python":"50%",
        "SQL":"90%"
        },
    
    "Ibrahim" : {
         "Html":"60%",
         "Css":"30%",
         "JS":"75%"
         },
    
    "Osama" : {
         "sql":"55%",
         "AWS":"40%",
         "apatchi":"83%"
         }

}

# print(people["Motasem"])
# print(people["Motasem"]["HBASE"])

########### when you loop the dictionary it gives you the key #######

for name in people :
    print(f"skills and progress of {name} :")
    for skill in people[name]:
       
        print(f"{skill.upper().center(8)}: {people[name][skill]}")
         
        