##--------------------------------------##
##-------- Membership Operators --------##
##--------------------------------------##
#----------------------------------------#
             # --- in ---# 
             # - not in -#
             #-----------#

name = "motasem"

print("m" in name)
print("s" in name)
print("z"in name)
print("^"*30)

friends = ["motasem", "Ali", "Sara", "Mai"]

print("Sara" in friends )
print("IMAM" in friends)
print("Mahmoud" not in friends)
print("motasem" not in friends)
print("^"*30)

## Using in & not in with If condition 
countries1=["EGYPT","KSA","BAHRAIN","KUWAIT","OMAN"]
discount1=80

countries2= ["USA", "UK", "FRANCE", "ITALY","SPAIN"]
discount2= 50
country = input('what\'s your country ? :  ').strip().upper() 
if country in countries1:
    print("Your course price is $ 100 ")
    print(f"But because you are from {country} you've  got a discount of ${discount1}") 
elif country in countries2 : 
    print("Your course price is $ 100 ")
    print(f"But because you are from {country} you've  got a discount of ${discount2}")

else :
    print("Your course price is $ 100 ")
    print(f"But because you are from {country} you've no discount ")
