## ----------------------------------------------- ##
## --- Built In Functions Part 5 => Filter ------- ##
## ----------------------------------------------- ##

# [1] Filter Takes a Function + Iterator 
# [2] Filter Run A Function On Every Element 
# [3] The Function Can Be Pre-Defined Function or Lambda  Function
# [4] Filter Out All Elements Gor Which The Function Return True
# [5] The Function Need To Return Boolean Value
# -----------------------------------------------------------------------------#

# Example 
def check_number (num):
    if num > 10 :
        return num 
    ## i can just write return num > 10 
    ## without writing the condition 
    
myNum= [1,19,10,20,100,5]

## filter(function, iterators: list , tuples etc  )


myresult = filter(check_number,myNum)

for number in myresult :
    print(number) ## will return the numbers that are > 10 
print("^"*30)
# if i have zeros in my list 
zerolist = [0,0, 1,3,0,0,5,19,0,0,]
## the function condition is == 0 
def check_zeros (num):
    if num == 0 :
        return True   # if i [ retrun num ] , the loop will not print the zeros 
                     # because the filter return True values only 
                     #  so i have to return True , then the loop on the filter will print the zeros
for n in filter(check_zeros,zerolist):
    print(n) ## because the function returns True ,, the filter will allw the loop to print zeros

#### ---------------------------------- ####
#### --------  Advanced Example ------- ####
#### ---------------------------------- ####
print("^"*30)

## Example 2 
MyText = ["Osama" , "Omer","Omar" ,"Ali" ,"Mai","Mina", "Motasem"]

def check_name(text): 
    return text.startswith("M")

for person in filter (check_name,MyText):
    print(person)

print("^"*30)
## example 3 (Lambda)

for name in filter(lambda text : text.startswith("M"),MyText):
    print(name)
 
print("^"*30)

for name in filter(lambda text : text.startswith("O"),MyText):
    print(name)





