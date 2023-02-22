## --------------------- ##
## --- set methods 2 --- ##
## --------------------- ##

# difference()

a = {1, 2, 3, 4}
b = {1, 2,3, "Osama", "Ahmed"} 
print(a)
print(a.difference(b)) # a - b 
print(a)
print("*" * 50)

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Motasem", "Mohammed"} 
print(c)
c.difference_update(d) # 
print(c)

print("*" * 50) 

# intersection()
e = {1, 2, 3, 4, "X"}
f = {"Motasem", "X", 2}
print(e.intersection(f)) # e & f
print(e)

# Intersection_update()
e.intersection_update(f)
print(f"the set e after update e : {e}") 
print("*" * 50) 

# symmetric_difference()

k = {1, 2, 3 , 4 , 5,"X"}
i = {"Osama","Zero", 1, 2, 4}
print(k.symmetric_difference(i)) # k ^ i

print("^" * 20)
# symmetric_difference_update()

p = {1, 2, 3 , 4 , 5,"X"}
s = {"Osama","Zero", 1, 2, 4}
p.symmetric_difference_update(s) # k ^ i
print(p)
print("^"*40)

# issuperset()
set1={1,2,3,4}
set2={1,2,3}
print(set1.issuperset(set2)) # True
print("^"*40)
#issubset() 
print(set1.issubset(set2)) # False

print(set2.issubset(set1)) # True
set3 = {1, 2, 3, 4, 5, 6}

print(set1.issubset(set3)) # True
print("^"*40)

# isdisjoint()

set4 = {"motasem", "mohammed", "Khlaed"}
set5 = {1,2,3,4}
print(set4.isdisjoint(set5)) #True
print(set5.isdisjoint(set1)) # False