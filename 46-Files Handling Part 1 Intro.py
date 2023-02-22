## --------------------- ##
## --- File Handling --- ##
## --------------------- ##

# "a" Append  Open file for appending values , Create file if not exits 
# "r" Read    [Default Value ] Open file for read and give error if file is not exists
# "w" Write   Open file for writing , create file if not exists 
# "x" Create  Create file , give errors if file exists
#---------------------------------------------------------------------------------------#
print("^"*30)
import os


print(f"Current Working Directory        : {os.getcwd()}")

print(f"Absolute Path of the opened file : {os.path.abspath(__file__)}")

print(f"Directory of the opened file     : {os.path.dirname(os.path.abspath(__file__))}")

# print(os.path.dirname(the opened file )) we get the opened file from the absolute path 
# so it will be print(os.path.dirname(os.path.abspath(__file__)))


## --- Change current working  directory --- ##
## os.chdir(directory of the opened file )
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd()) ## it will not change because i don't have c:/ and d:/ directory like windows 

## open the file from elzero course folder on desktop 
file = open("osamaElzero.txt") ## i have no problem here i don't need to add the absolute path 
                               ## because it is my current directory 


## i opend a file located on desktop so i have to provide the absolute path  
file = open("/Users/elkihale.n-abualqumboz.mk/Desktop/osama.txt")

#if i have a folder name n =>> then i have to add \n to the path 
## to avoid it considering it sequence separator \n new line .. we add r before 

file = open("/Users/elkihale.n-abualqumboz.mk/Desktop/n/n.txt")
## here it's not a \ so we won't have a problem .. but on a windows it will be 
## \n 

print(os.getcwd())

print("^"*30)