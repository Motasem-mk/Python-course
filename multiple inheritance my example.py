
class Tomatoe :

   def __init__(self,first_name,middle_name,last_name,age):
       
       self.fname=first_name
       self.mname= middle_name
       self.lname=last_name
       self.ag =age
       print("Hello from Base class")

   def full_name(self):
       return f"{self.fname} , your full name is {self.fname} {self.mname} {self.lname} "
   
   def your_age(self):
       return f" Hello {self.full_name()} your age is {self.ag}"
   
class Potatoe (Tomatoe):
    def __init__(self,first_name,middle_name,last_name,age,gender):
       super().__init__(first_name,middle_name,last_name,age)
      
       self.gender = gender
       print("Hello from potatoes main class ")

    def your_age(self):
       return f" Hello {self.fname} your age is {self.ag}"

class Copy_classes(Potatoe):
   def __intit__(self,first_name,middle_name,last_name,age,gender):
       super().__init__(first_name,middle_name,last_name,age)
       self.gender=gender
   def full_info (self):    
       if self.gender == "Male":
           return f"Hello Mr. {self.full_name()}\n{self.your_age()}"
       elif self.gender == "Female":
           return f"Hello Miss {self.full_name()}\n{self.your_age()}"
       else :
          return f"Hello {self.full_name()}\n{self.your_age()}"    


food_two = Tomatoe("Naima", "El Regrage", "Elkihake", 46)
food_one = Potatoe("Motasem", "Mohammed", "Abu Alqumboz",40,"Male")

my_inheritence_one = Copy_classes("Motasem", "Mohammed", "Abu Alqumboz",40,"Male")
my_inheritence_two = Copy_classes("Yusra", "Kamel", "Abu Alqumboz", 74,"Female")
my_inheritence_three = Copy_classes("Arwa", "Mohammed", "Abu Alqumboz", 47,None)


print(my_inheritence_one.full_name())
print(my_inheritence_three.full_info())
print(my_inheritence_one.full_info())
