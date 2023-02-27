# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food : ## Base Class 

    def __init__(self,name,price) :

        self.name=name
        self.price=price
        print(f"{self.name} is created from Base class its price is {self.price}")


    def eat(self):
        print("Eat method from Base class ")


class Apple(Food) :  # Derived Class
    
    def __init__(self,name,price,amount):
      

      #Food.__init__(self,name)  ## create instance from Base class

      super().__init__(name,price)

      self.amount = amount

      print(f"{self.name}Apple is created from derived class and price is {self.price} its amount is {amount}")

    
    def get_from_tree (self):
        print("Get from Tree from Derived Class")

    
    def eat(self):   ## overriding the method 
        print("Eat method from Derived class ")


food_one =  Food("Pizaa",150)
food_two = Apple("Pizza",120,300)
food_one.eat()
food_two.eat()
food_two.get_from_tree()

