# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class Skill :
    def __init__(self) :
        self.skills = ["Html", "Css", 'JS']
    

    def __str__(self):
        return f"This is my skills : {self.skills}"
    
    def __len__(self):
        return len(self.skills)
    
    def all_skills (self):
        return self.skills

profile = Skill()

print(profile)
print(len(profile))


profile.skills.append("PHP")
profile.skills.append("MYSQL")

print(len(profile))


my_string= "Osama"

print(profile.__class__)
print(my_string.__class__)


# print(dir(int))

# # print(dir(str))
# print(dir(int))

# print(str.upper(my_string))