# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------


class Member :
    def __init__(self,name):
        self.__name=name

    def say_hello(self):
        return f"Hello {self.__name}"

    def get_name(self):
        return self.__name
    
    def set_name (self,new_name):
       self.__name = new_name
       return f"Your new name is :{self.__name}"


one = Member("Ahmed")
print(one.say_hello() )

# print(one._Member__name)
# one._Member__name = "Motasem"
# print(one.say_hello() )

print(one.get_name())

print(one.set_name("Naima"))

print(one.get_name())