## ---------------------------------------------- ##
## ---- Files Handling Part 4 Important Info ---- ##
## ---------------------------------------------- ##


import os
print(os.getcwd())
# myfile= open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/mk.txt","a")
# myfile.truncate(5)
# myfile= open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/mk.txt","a")
# print(myfile.tell())  #5 the position of the curser
 # i entered enter on the file and it gives me now 6 
 # enter is one char on mac os .. but in windows is 2 chars . 

myfile= open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/mk.txt","r")
myfile.seek(10) ## it will read from char num 10 
print(myfile.read()) 

#create a new file to remove it 
# create must be in write 
myfile= open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/remove.txt","w")
 

# remove file 
os.remove("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/remove.txt") # removed 