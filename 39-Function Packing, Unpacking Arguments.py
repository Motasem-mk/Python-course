## ----------------------------------------------------------- ##
## -------Function Packing, Unpacking Arguments *Args -------- ##
## ----------------------------------------------------------- ##

print(1,2,3,4)
a=[1, 2, 3, 4]
print(a) 
# to unpack the list * before 
print(*a)

def say_hello (n1,n2,n3,n4) : 
    peoples = [n1,n2,n3,n4]
    for name in peoples :
        print(f"Hello {name}")

say_hello("Motasem", "Ahmed", "Osama", "Khaled")
print("^"*30)

# now if we add a fifth argument it will give us an error 
# because only four parameteres in the function 
# say_hello("Motasem", "Ahmed", "Osama", "Khaled","Ali")
# TypeError: say_hello() takes 4 positional arguments but 5 were given
# most of the times i don't know the numbers of names in list 
# to solve that we use the * to unpack 

def say_hello_unpack_method (*peoples) :
    for name in peoples :
        print(f'Hello {name}')

 
say_hello_unpack_method("Motasem", "Ali", "Ahmed", "Naima", "Hanaa", "Aminas")

print("^"*30)
# or a list 
students = ["Motasem", "Ali", "Ahmed", "Naima", "Hanaa", "Aminas"]
say_hello_unpack_method(*students)


def show_details(name,*skills):
   
      print(f'Hello {name} your skills is : ')
      for  s in  skills :
          print(s)

#skills = ["HADOOP", "HIVE" ,"KAFKA"]

show_details("Motasem","HADOOP", "HIVE" ,"KAFKA","HBASE")

