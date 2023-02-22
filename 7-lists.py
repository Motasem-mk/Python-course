### -------------------####
###------- Lists ------###
### -------------------####

# [1] List items are enclosed in square brackets 
# [2] list are ordered , to use index to access item
# [3] List are Mutable => we can add , delete , edit 
# [4] list items are not unique 
# [5] list can have different data types 
# ------------------------------

MyAwesomeList = ["one", "Two","one" ,1,2.5,True]
print(MyAwesomeList) 
print(MyAwesomeList[1])
print(MyAwesomeList[-1])
print(MyAwesomeList[-3])
print(MyAwesomeList[2:5])
print(MyAwesomeList[:3])
print(MyAwesomeList[::2])
print(MyAwesomeList[-6:-2:2])

print(MyAwesomeList)
MyAwesomeList[1]=2
MyAwesomeList[-1]=False
print(MyAwesomeList)

MyAwesomeList[0:3] = ["a","b","c"]
print(MyAwesomeList)
MyAwesomeList[:3]="A"
print(MyAwesomeList)

## append()
myOldFriends=["Adibah","Shaima","Tawfiq"]
my_friends = ["ahmed","ali"]
print(my_friends)
my_friends.append("Mai")
print(my_friends)
my_friends.append(100 )
print(my_friends)
my_friends.append(True)
print(my_friends)
my_friends.append(myOldFriends)
print(my_friends)
print(my_friends[2])
print(my_friends[4])
print(my_friends[5])
print(my_friends[5][1])

#extend()
g=[1,2,3,4]
h=["a","b","c","d"]
print(g+h)
g.extend(h)
print(g)
print(" ".join(myOldFriends))
 
print(",".join(h))

# remove() by mentioning the item itself 

lis=[1,2,1,1,"ali","ahmed",'ali']
lis.remove(1) # will remove the first 1 and leave the rest 
print(lis) # [2, 1, 1, 'ali', 'ahmed', 'ali']
lis.remove("ali")
print(lis) # [2, 1, 1, 'ahmed', 'ali']

# sort ## only int. or str 
numlist = [12,4,56,235,-23,-1,0,67]
print(numlist) #[12,4,56,235,-23,-1,0,67]
numlist.sort()
print(numlist) #-23, -1, 0, 4, 12, 56, 67, 235]
numlist.sort(reverse=True)
print(numlist)

liss=["hani","haifa","ahmed","motasem"]
liss.sort()
print(liss)
ai = [34,76,12,-97,-1,0,345,"motasem",235,67984,"ali"]
ai.reverse()
print(ai) # just reversed it without sorting 
aid = [34,76,12,-97,-1,0,345,"motasem",235,67984,"ali"]

#aid.sort() #TypeError: '<' not supported between instances of 'str' and 'int'
#print(aid)

# .clear()
ass=[1,2,3,4]
ass.clear()
print(ass)

# .copy() # shallow copy 

ass.extend([1,2,3,4])
print(ass)
add=ass.copy()
print(add)
ass.append("Hi")
print(ass)
print(add)

# count()

ass.extend([1,1,2,2,2,3])
print(ass)
print(ass.count(2)) # 4 
strr="my friends are ahmed and ahemd and mai and mai"
print(strr.count("mai"))
 
# index()

print(aid.index("motasem")) #7 
print(ass.index(1)) # first index of number 1

# insert() we specify the index where to insert the new item 
# insert ([index], item)
ff = [1,2,3,4,"Python","Hadoop","Hive"]
ff.insert(4,"KAFKA")
print(ff)
ff.insert(-1,"R")
print(ff) 
ff.append("AWS")
print(ff)

# .pop() # remove and return  by the index unlike the remove 
# remove () it has to mention the item itself 
print(ff.pop(5))
print(ff)