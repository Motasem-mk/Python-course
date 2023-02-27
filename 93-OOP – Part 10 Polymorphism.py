# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

n1= 10 
n2 = 20

print(n1+n2)
s1 = "Hello"
s2 = "python"

print(s1 +" "+ s2)
print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"key1":"1","key2":2}))




class A :
    def do_something(self):
        print("from class A")
        raise NotImplementedError("Derived class must implement this method")

class B(A) :
  def do_something(self):
        print("from class B")

class C(A):
    def do_something(self):
        print("from class C")
    pass

my_instance = C()
my_instance_two = B()
my_instance_two.do_something()
