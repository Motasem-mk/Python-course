# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group())
print(search.groups())

for i in search.groups():
    print(i)


print(f"protocol    : {search.group(1)}")
print(f"subdomain   : {search.group(2) }")
print(f"domain name : {search.group(3)}")
print(f"Top level doamin: {search.group(4) }")
print(f"port : {search.group(5)}")
print(f"Query string : {search.group(6)}")