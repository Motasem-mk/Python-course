##---------------------------------------------------------##
##---- Function Packing Unpacking Arguments Training's ----##
##---------------------------------------------------------##

skill_tuple =("HIVE","HBASE","CASANDRA")
skillswithprogress={
    'Python':"80%",
    'scala' :"50%",
    'R' :"77%"
}

def show_skills(name,*skills,**skillswithprogress):
    print(f"\n\nHello {name}\n\nskills without progress are :\n")
    for skill in skills:
        print(f"-  {skill}\n")
    print("Skills with progress :\n")
    for k,v in skillswithprogress.items() : 
        print(f'{k} : {v}\n')


# show_skills("Motasem","HIVE","HBASE","CASANDRA",Hive="90%) 
show_skills("Motasem",*skill_tuple,**skillswithprogress)
## to unpack tuple , list we put one  * 
## to unpack dict we put doubt  ** 