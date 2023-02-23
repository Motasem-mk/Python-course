# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B","C"]
tuple1 = ("Man", "Woman", "Boy", "Girl")
dict1= {"Name":"Osama", "Age":36, "Country":"Egypt"}



##########################################################
# ultimateList = zip(list1,list2)
# print(ultimateList)  # <zip object at 0x1013761c0>

# for item in ultimateList:
#     print(item)  #(1, 'A')
#                  #(2, 'B')
#                  #(3, 'C')
# # its length is the length of the lowest object whichh it list2 

##########################################################

## only three items will be printed out of the loop 
## because the lowest is the dictionary ... it has three items 

for item1 , item2,item3 ,item4 in zip(list1,list2,tuple1,dict1):
    print("list1 items  : ",item1)
    print("list2 items  : ",item2)
    print("tuple1 items : ",item3)
    print("dict1 items  : ",item4,":",dict1[item4])