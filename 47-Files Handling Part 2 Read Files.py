## ---------------------------------------- ##
## ------ File Handling => Read file ------ ##
## ---------------------------------------- ##

# import os 

# print(os.getcwd()) 

myfile = open("osamaElzero.txt","r") ## "r" is the default i don't need to write it 

print(myfile ) ## it will give us File Data Object 
               ## such as:  name , mode , encoding 

print(myfile.name) # osamaElzero.txt
print(myfile.mode) # r == read 
print(myfile.encoding) ## UTF-8

#print(myfile.read()) ## it will read everything 
print("^"*30,"\n")
#print(myfile.read(5)) ## it will read the first 5 characters 
print("^"*30)
# print(myfile.readline(3)) # it will read the first line  only 3 chars 
# print(myfile.readline()) # it will read the next line , but will start from the fourth chars in the first line 
# print(myfile.readline()) 

# #print(myfile.readlines())# ['Hello World\n', "I'm MOtasem \n", 'From the text \n', 'Thank you']
# print(myfile.readlines(25)) # will return 25 chars 
# print(type(myfile.readlines())) ## <class 'list'>

for line in myfile : ## it will read all lines in the file 
    print(line)

## if i want to read few lines not all lines 
    if line.startswith("F"): # It will read until the line starts with F
        break
    