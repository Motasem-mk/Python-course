## --------------------------------------------------- ##
## ---- File Handling => Write and Append in file ---- ##
## --------------------------------------------------- ##

# import os 
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

myfile=open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/OsamaElzero.txt","w")
myfile.write("Hello i'm coming from Python")
myfile.write("\nThis is the second line")
# myfile=open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/OsamaElzero.txt")
# print(myfile.read())

myfile=open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/motasem.txt","w")
myfile.write("Hello Python from Motasem VC idle\n"*1000)
# myfile=open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/motasem.txt","r")
# print(myfile.read())

myList= ["Motasem\n", "Tawfeeq\n", 'MAI\n', "NAIMA\n"]
myfile = open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/mk.txt","w")
myfile.writelines(myList)
## Append 
myfile = open("/Users/elkihale.n-abualqumboz.mk/Desktop/Elzero Python/mk.txt","a")
myfile.write("Ali")
 

myfile.write("Here is a new line\n")

myfile.write("Here is another new line\n\n\n\n\n")
myfile.write("Here is another test\n\n\n\n\nanother test")