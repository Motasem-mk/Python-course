
# # # indexing and slicing 
# # # [start:end]
# # # [Start:End:Steps]
# # from __future__ import print_function


# M="I Love Python"
# # print(M[1])
# # print(M[9])
# # print(M[-1])
# # print(M[-3])
# # print(M[2:8]) #Love P
# # print(M[5:11]) #e Pyth
# # print(M[3:5]) # ov
# # print(M[:10]) # If the start is not there , then it will start from 0
# #                # I Love Pyt
# # print(M[5:]) # if end is not here , it will continue to the end 
# # print(M[:]) # full data 

# # print(M[::1]) # one step I Love Python
# # print(M[::2]) # two steps 

# ####--------------------###
# ##----strings methods----##
# ###---------------------###
# print(len(M))
# B="    I Love Python    "
# print(len(B))

# #Strip() rstrip() lstrip()

# print(B.strip()) # if it is empty .. it will remove the spaces from left and right 
# print(B.rstrip())
# print(B.lstrip())
# print("#"*30)

# c = "****I Love Python****"
# print(c)
# print(c.strip("*"))
# print(c.strip("*")) # it will remove the * from left and right 
# print(c.rstrip("*"))
# print(c.lstrip("*"))
# print("#"*30)

# d= "@#@#@#I love python@#@#@#"
# print(d.strip("#@"))
# print(d.lstrip("@#"))
# print(d.rstrip("@#"))
# # .title () # will make firts letter of each word capital and also letters comes after numbers
# f= "hello my name is motasem i love 3d graphic and 5g communication mobile phone technology "
# print(f.title())  
# # .Capitalize()
# print(f.capitalize()) # will make first letter capital 

# # zfill

# h ,j,k,l= "1","11","111","1111"

# print(h.zfill(4))
# print(j.zfill(4))
# print(k.zfill(4))
# print(l.zfill(4))

# # .upper()
# # .lower()

# x="motasem"
# print(x.upper())
# print(x.lower())

# # .split()

# y= "I love python and PHP"
# print(y.split()) # it will split the string into a list , and the separator will be space if it is empty 
# print(type(y.split()))
# v = "I-love-python-and-PHP"#the separator will be - , if i didnt put in the param - it will consider it one item in the list
# print(v.split("-"))
# print(v.split("-",2)) # max split , will split only the first 2 from the left by deefault 
# print(v.rsplit("-",2)) # rsplit("-",2) from the right 
# print(v.rsplit("-",3))

# # .center()

# q="motasem"
# print(q.center(11)) #spaces 
# print(q.upper().center(15,"@"))

# # .count()
# m="I love python because python is a great language"
# print(m.count("python"))
# print(m.count("e"))
# print(m.count("e",0,6))

# #swapcase()

# n="I lOVe Python"
# z="i LovE pYThoN"
# print(n.swapcase())
# print(z.swapcase())

# startswith()
p = "I love python"
# print(p.startswith("I"))
# print(p.startswith("S"))
# print(p.startswith("i"))
# print(p.startswith("l",2,6))

# # .endswith()
# print(p.endswith("n"))
# print(p.endswith("N"))
# print(p.endswith("a"))
# print("*"*40)
# print(p.endswith("e",2,6)) #true
# print(p.endswith("e",2,5)) #false
# print(p.endswith("n",9,13)) # true