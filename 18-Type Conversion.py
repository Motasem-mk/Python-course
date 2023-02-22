## -------------------------- ##
## ---- Type Conversion ----- ##
## -------------------------- ##

# str()

a= 10.0
print(type(a))
print(type(str(a)))

# tuple()
c= "osama" # string
d = [1,2,3,4,5] #list 
e = {"A","B","C"} #set  # random 
f = {"A":1,"B":2} #dict
print("^"*30)
print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
#print(tuple(500)) # TypeError: 'int' object is not iterable
print("^"*30)

# list()
tupl=(1,2,"M")
print(list(c))   #['o', 's', 'a', 'm', 'a']
print(c.split()) # ['osama']
print(list(e))
print(list(f))
print(list(tupl)) 

# set()
print("^"*30)
print(set(c))
print(set(d))
print(set(f))
print(set(tupl))

# dict()  
print("^"*30)

# string cant be converted into a dict because there is no values 
# # gave me error ValueError: dictionary update sequence element #0 has length 1; 2 is required
# because it needs keys and values 
# print("^"*30)
# print(dict(c))
# print(set(d))
# print(set(e))
# print(set(tupl))

# list 
# can be converted into a dict if there is nested lists contains two elements 
nestedlist=[["one",1],["two",2],["three",3]]
print(dict(nestedlist))
# tuple
# can be converted into a dict if there is nested tuples contains(key&value)
 
nestedtuple=(("A",1),("B",2),("C",3))

print(dict(nestedtuple))

nestedset= {{"one",1},{2,3},{4,"four"}}
#print(dict(nestedset)) #TypeError: unhashable type: 'set'



