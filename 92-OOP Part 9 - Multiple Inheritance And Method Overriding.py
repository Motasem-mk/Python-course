
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

    def __init__(self):
        print("Base One")

    def func_one(self):
        print("One")

class BaseTwo:
       
       def __init__(self):
        print("Base Two")

       def func_two(self): 
         print("Two")
 


class Derived(BaseOne,BaseTwo) :
    pass


My_Var = Derived()

#print(Derived.mro()) ## method resolution order 

print(My_Var.func_one)
print(My_Var.func_two)

My_Var.func_one()
My_Var.func_two()


class Base:
    pass

class DerivedOne(Base):

    pass

class DerivedTwo(DerivedOne):
    pass