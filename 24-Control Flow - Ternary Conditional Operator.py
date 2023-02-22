## --------------------------------------------------------------##
## ------- Control Flow - Ternary Conditional Operator ----------##
## --------------------------------------------------------------##

country = "Egypt"

if country == "Egypt":
    print(f"The weather in {country} is 15 c ")
elif country == "Saudi Arabia":
    print(f"The weather in {country} is 30 c ")
else:
    print(f"{country} is not in the list ")

# Short if
movieRate= 18
age =16

if age<movieRate:
    print("Movie  is not good for you ") # If condition is True 
else :
    print("Movie is good for you")    # If condition is False 

#Ternary Conditional Operator => we can write in one sentence 

print(" this movie is not  good for you " if age <movieRate else "Thos movie is good for you ")

# condition if  True | if condition | else | condition if is dalse 