##---------------------------------------------------------##
##---- Function packing, Unpacking arguments ** KWArgs ----##
##---------------------------------------------------------##
myskills = {
    "HTML" : "80%",
    "CSS"  : "90%",
    "JS"   : "70%",
    "PHP"  : "80%"
}
### have to add ** to unpack the dictionary 
def skills(**myskills):
 
  for s in myskills:
    print(f'{s} : {myskills[s]}')

skills(**myskills)

employees ={
    "Motasem" : {
    "Skills" :{
    "Hive":90,
   "Hadoop": 80,
    "Python": 90
    }
    },
    "OSAMA" : {
    "Skills" :{
    "Hive":100,
   "Hadoop": 99,
    "Python": 100
      }
    },
     "Elzero" : {
    "Skills" :{
    "Hive":30,
   "Hadoop": 40,
    "Python": 100
      }
    }
}

# for n in employees:
#     print(f"Hello {n} :\n","^"*20)
#     for s in employees[n] :
#        print(f"Your {s} are :\n")
#        for p in employees[n][s]:
#            print(f"{p.center(28).lstrip()}\n",f"your progress is : {employees[n][s][p]}\n\n")
      

#print(*employees) # it will give us the keys 

def employees_skills (**employees):
   for n in employees:
    print(f"Hello {n} :\n","^"*20)
    for s in employees[n] :
       print(f"Your {s} are :\n")
       for p in employees[n][s]:
           print(f"{p.center(28).lstrip()}\n",f"your progress is : {employees[n][s][p]}\n\n")



employees_skills(**employees)  
## it worked 
## i have to add ** double astr
def unpack_dict (** employees):
    for key,value in employees.items():
       print(f'## {key} :' )
       for subkey,subvalue in employees[key].items():
           print(f'{subkey} : ')
           for subkey,subvalue in employees[key][subkey].items():
               print(f'-{subkey} : {subvalue}')
unpack_dict(**employees)

