##---------------------------------------------------##
##-------- Practical - Your Age Full Details --------##
##---------------------------------------------------##

# Input Age
age = int(input('what\'s your age : ').strip()) # string if i didn't put int 
print(age)
print(type(age))  

# Get age in all time units 

print(f"Your age is {age} years\n{age*12} months\n{age*360} days\n{age*12*4} weeks\n{age*360*60:,} hours\n{age*360*60*60:,} minutes\n{age*360*60*60*60:,} seconds")
