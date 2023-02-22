## ---------------------------------- ##
## ---- Loop Advanced Dictionary ---- ##
## ---------------------------------- ##

myskills = {
    "HTML" : "80%",
    "CSS"  : "90%",
    "JS"   : "70%",
    "PHP"  : "80%"
}

# for skill in myskills :
#     print(skill , myskills[skill])

## the second method 

print(myskills.items())

for skill ,progress  in myskills.items():
    print(skill ,progress ) # instead of using the index like above myskills[skill]
                            # we can just use .items and it will divide the dict into tuples 
                            # and we reach them without the index 

print("^"*30)
## same methode with nested dictionary 

myUltimateskills = {
    "Big Data":{
        "Hadoop": 80,
        "HIVE"  : 90
                },
        "Data Science":{
            "Python" : 90,
            "Stats"  : 85,
            "BI"     : 88
                        },
            "Data Analysis":{
                "R" :77,
                "SCALA" :64
                            }
                 }

# for skill in myUltimateskills :
#     print(f"skill    : {skill} :\n")
#     for key_value in myUltimateskills[skill]:
#        print(f"{key_value.center(8).upper() } : {myUltimateskills[skill][key_value]}\n" )

# .items() method 

for key ,value in myUltimateskills.items():
     print(f"{key}:\n" )
     for child_key , child_value in value.items() :
        print(f"{child_key.center(20).upper()} : {child_value} %\n")

## advanced nested in nested dict
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

for n in employees:
    print(f"Hello {n} :\n","^"*20)
    for s in employees[n] :
       print(f"Your {s} are :\n")
       for p in employees[n][s]:
           print(f"{p.center(28).lstrip()}\n\n",f"your progress is : {employees[n][s][p]}\n\n")
      
