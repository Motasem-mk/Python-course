# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

my_search = re.search(r"[A-Z]{2}","OOsamaEElzero")
print(my_search)
#print(dir(my_search)) 

print(my_search.start())
print(my_search.string)
print(my_search.span())
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)","os@osama.com")

if is_email :
    print("this is a valid email")
else : 
    print("this is not a valid email")


print(is_email.span())
print(is_email.string)
print(is_email.group())

email_input = input("please write your email : ")

search =re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info",email_input)

email_list = []

if search != [] : 
    email_list.append(search)
    print("Email added")

else :
    print("Invalid email")

for email in email_list:
    print(email)

