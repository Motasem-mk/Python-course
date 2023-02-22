##-------------------------------------------------------------------###
##----------- Calculate Age Advanced Version and Training -----------###
##-------------------------------------------------------------------###

name= input('What\'s your Name ? ').strip().capitalize()
age = int(input('what\'s your age ? '))
print("^"*100)
print("You can choose whether to write the full word of the time unit or just the first letter".center(100,"*"))
print("^"*100)
unit = input("choose the unit ? (Months\M ,weeks\W , days\D )").strip().lower()

months = age * 12
weeks = months * 4
days  = age * 360

if unit == "months" or unit == "m" :
    print(f"Hello {name} you are {age} years\nYouve lived {months:,} months ")

elif unit == "weeks" or unit == "w":
    print(f"Hello {name} you are {age} years\nYouve lived {weeks:,} weeks ")

elif unit == "days" or unit == "d":
    print(f"Hello {name} you are {age} years\nYouve lived {days:,}  days ")

else :
    print("not supported")
