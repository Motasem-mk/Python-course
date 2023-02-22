# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

mystring = "Osama"
mylist  = [1, 2, 3, 4, 5] 

mynum = 10 # is not iterable 
myfloat= 10.00 # is not iterable 
a=True # boolean is not iterable 
for l in mystring:
    print(l,end=" ")
for n in mylist : 
    print(n,end=" ")

## next(iterator)
## iterator = iter(iterable)

myitrator = iter(mystring) ## generated the iterator from the iterable 

print(f"\n{next(myitrator)}",end=" ") # O
print(f"{next(myitrator)}",end=" ")   # s
print(f"{next(myitrator)}",end=" ")   # a
print(f"{next(myitrator)}",end=" ")   # m
print(f"{next(myitrator)}",end=" \n")   # a
#print(f"{next(myitrator)}",end=" ")   # stopoteration  .. in for loop it stops in the back scene 

for l in iter("Elzero"):
    print(l, end=" ")





