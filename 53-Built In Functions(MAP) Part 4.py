## --------------------------------- ##
## --- Built In Functions => Map ----##
## --------------------------------- ##

# [1] Map take a Function + iterator
# [2] Map called Map because it Map the Function on every element 
# [3] The Function can be predefined function or Lambda Function
# ----------------------------------------------------------------------

# Use Map with predefined Function

def format_text (text):
    return f"- {text} -"

mytexts= [" Osama ", " Motasem ", " Naima "]

# map(function , iterable or iterator )

myformatedtext = map(format_text,mytexts)

print(myformatedtext) # <map object at 0x10d0078b0>

for n in map(format_text,mytexts):

    print(n) # result : -  Osama  -
             #          -  Motasem  -
             #          -  Naima  -

print("^"*30)
# or 
for name in myformatedtext :
    print(name)
print("^"*30)

## use map with lambda function
## i can make it list 

for name in  list(map( lambda mytexts  : f" - {mytexts} - " ,mytexts)):
    print(name)

