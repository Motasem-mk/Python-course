## --------------------------------- ##
## --- Built In Functions Part 2 ----##
## --------------------------------- ##

# sum()
# round()
# range()
# print()
# ------------------------------------#

# sum(iterable, start) start is default = 0 

a= [1,10,19,40]
print(sum(a))  # sum a ,start is default = 0 
print(sum(a,40)) #it will start sum from 40 + a

# rount(number , numofdigits)
print(round(150.499)) ## it will be 150 because it is point .499 less than 0.5
print(round(150.501)) ## it will be 151... 0.501 >0.5
print(round(150.550)) ## 151
print(round(150.551,2)) ## 150.55 number of digit is 2
print(round(150.555,2)) ## 150.56 

# range(start,end,step)  ## start is default =0 , step default = 1

print(list(range(0)))  # empty list:  start=0 , end=0
print(list(range(10))) # start =0 , end =10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 20, 2))) # start =0 , end =20 steps =2 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# print()
# default separator is " " space 
# same result
print("Hello Osama How Are You ")
print("Hello","Osama","How","Are","You")  #  default separator is space 
print("Hello","Osama","How","Are","You",sep=" @ ") #Hello @ Osama @ How @ Are @ You

## default end = \n
print("First line",end=" $ ") # First line $ Second line 
print("Second line ") #First line $ Second line  
                       #Third line
print("Third line")
