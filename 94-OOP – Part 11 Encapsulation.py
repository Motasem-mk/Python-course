# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

# class Member:
#     def __init__(self,name):
#         self.name = name

# one=Member("Ahmed")
# print(one.name)

# one.name="Motasem"
# print(one.name)

## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^##

### Protected 
# class Member:
#     def __init__(self,name): ## protected
#         self._name = name



# one=Member("Ahmed")
# print(one._name)

# one._name="Motasem"
# print(one._name)

## private 
class Member:
    def __init__(self,name): ## Private
        self.__name = name

    def say_hello(self):
        return f"Hello {self.__name}"



one=Member("Ahmed")
#print(one.__name)

print(one.say_hello())

print(one._Member__name)