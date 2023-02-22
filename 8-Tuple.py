##------------------##
##---- Tuples ------##
##------------------##
#[1] Tuple items are enclosed in parentheses 
#[2] Wecan remove the parentheses if we want 
#[3] Tuples are ordered tu use index to access items
#[4] Tuples are immutable => you can't add or delete 
#[5] Tuple items are not uniqe
#[6] Tuple can have anydifferent data type
#[7] Operators used in string and list are available in tuple 

myAwesomeTuple = ("Motasem","Mai","Shaima")
print(type(myAwesomeTuple))
myTuple = "Motasem","Mai","Shaima"
print(type(myTuple))

# Tuple indexing 

print(myAwesomeTuple[0])

Tuple2 = (1,2,3,4,5)
print(Tuple2[-3])
print(Tuple2[2])

# Tupple Assign values 

Tuple4 = (1,2,3,4,5)
#Tuple4[2]="Three"
#print(Tuple4)

#Tuple items 

Tuple5=("Motasem","Mohammed",1,2,3,100.5,True)
print(Tuple5[0])
print(Tuple5[-1])

# Tuple with one element 

myT1 = ("Motasem",) # we add , to make it tuple 
myT2 = "Motasem",
print(type(myT1))  
print(type(myT2))  
print(len(myT1))

a= (1,2,3,4,5)
b=(6,7,8,9,10)
 
c=a+b
d=a+("A", "b",True)+b
print(c)
print(d)

#Tuple,list,string Repeat (*)

myString = "Motasem"
myList = [1,2]
myTuple = ("A","B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Mthods => count()
print(Tuple5.count("Motasem"))

#Methods => index()
B=(1,2,3,4,5,6,7,8,9)
print(f"the position of {B.index(5)}")

#Tuple destruct

k = ("A","B",4,"C")
x,y,_,z=k 
print(x)
print(y)
print(z)

