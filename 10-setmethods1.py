## ---------------------- ##
## ---- Set Methods ----- ##
## -----------------------##

#  Clear()

a= {1,2,3,"Motasem"}
print(a)
a.clear()
print(a)

# Union()

b = {"One","Two","Three"}
c = {"1","2","3"}
x = {"Zero","Cool"}
print(b | c)
print(b.union(c))
print(b.union(c,x))

# add
d = {1,2,3,4}
d.add(5)
d.add(6)
print(d) 

# copy
e = {1,2,3,4}
f = e.copy()
print(e)
print(f)
e.add(5)
print(e)

# remove 

g = {1,2,3,4}
g.remove(1)
print(g)
# g.remove(7)
# print(g)   KeyError: 7
# discard()

h = {1,2,3,4,5,0}
h.discard(7)
print(h)

# pop() # because there is not indexing , it will take out random items 
j = {1,2,3,4}
j.pop()
print(j)
j.pop()
print(j)

# update()
k = {1,2,3}
v = {1, "A", "B", 2}

k.update(v)
print(k)
# i can update it with a list 
k.update(["Hive","HADOOP","KAFKA"])
print(k)