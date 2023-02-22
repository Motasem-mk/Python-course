# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

mybirthday = datetime.datetime(1983,1,14)
print(mybirthday)
print(mybirthday.strftime("%d"))
print(mybirthday.strftime("%a"))
print(mybirthday.strftime("%A"))
print(mybirthday.strftime("%b"))
print(mybirthday.strftime("%B"))
print(mybirthday.strftime("%y"))
print(mybirthday.strftime("%Y"))

print(mybirthday.strftime("%a %d-%b-%Y"))

print(datetime.datetime.now().hour)

print(datetime.datetime.now().strftime("%Y %b %A"))