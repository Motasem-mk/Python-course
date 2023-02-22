## ----------- ##
## --- Set --- ##
## ----------- ##

# [1] Set Items are enclosed in curly Braces
# [2] Not Ordered and not indexed 
# [3] Set Indexing and Slicing can't be done 
# [4] Set Has Only Immutable Data Type (Numbers.String,Tuples) List and Dict Are Not  
# [5] Set Items Is Unique  (can't have the same items more than once 
#  for example can't have { 1,1,2} number 1 two times inside it , it will just give the item one time 
# # --------------------

# Not Ordered and Not Indexed 

mySet1 = {"Osama","Ahmed",100,"Mohammed"}
print(mySet1)
#print(mySet1[2]) error 

#Slicing can't be done

mySet2={1,2,3,4,5}
#print(mySet2[0:3]) #TypeError: 'set' object is not subscriptable

# Has Only Immutable Data Type 

#mySet3 = {"Motasem",100,102.5,True,[1,2,3,4,5]} 
#print(mySet3)  # Error unhashable type: 'list'
# doesn't accept list and dict inside the set 

mySet4 =  {"Motasem",100,102.5,True,(1,2,3,4)} 
print(mySet4)

# Set Items Is Unique 

mySet5 = {1,2,"Osama","One","Osama",1}
print(mySet5)