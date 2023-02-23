# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def say_hello(name):
    ''' This is a function that print( Hello to any name 
    it is a simple function 
    just to explain the difference between  documentation and commenting  '''
    print(f"Hello {name}")

say_hello("Motasem")

#print(dir(say_hello))
print(say_hello.__doc__)
print("^"*30)
help(say_hello)
