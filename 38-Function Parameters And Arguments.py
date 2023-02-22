##---------------------------------------------##
##----- Function Parameters And Arguments -----##
##---------------------------------------------##


a,b,c = "Osama", "Ahmed", "Khaled"
# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                       =>   Function keyword [ define ]
# say_hellp                 =>   Function name 
# namee                     =>   Parameter
# Print(f"Hello {name}")    =>   Task
# say_hello ("ahmed")       =>   Ahmed is the argument 
    
def say_hello (name):
    print(f"hello {name} ")

say_hello("Motasem")
say_hello(a)
say_hello(b)

def addition (n1,n2) : 
   print(n1+n2)

addition(1,2)

def advanced_addition (n1,n2) :
    if type(n1) != int or type(n2)!=int:
       print("only integer allowed ")
    else:
        #print(int(n1)+int(n2))
       print(n1+n2)

advanced_addition(-3,2)
advanced_addition(2,2)
advanced_addition("100",20)
advanced_addition("Ahmed",20)


def full_name(Fname,Mname,Lname):
    print(f"Hello {Fname} {Mname[0]} {Lname}")
                          # {Mname:.1s}
  

   
Fname  = input("Enter your first name : ").strip().capitalize()
Mname = input("Enter your middle name : ").strip().capitalize()
Lname = input("Enter your last name : ").strip().capitalize()

full_name(Fname,Mname,Lname)
