# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------


import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

## print(the current time ::

print(datetime.datetime.now())

print("^"*30)

## print(the current year )

print(datetime.datetime.now().year)
print("^"*30)

## print(the current month  )

print(datetime.datetime.now().month)

print("^"*30)

## print(the current day  )

print(datetime.datetime.now().day)

## print start and end date min = start .. max == end 
print("^"*30)
print(datetime.datetime.min.max)

print("^"*30)
## print( the current time)
print(datetime.datetime.now().time())

print("^"*30)
 
## print the current time hour 
print(datetime.datetime.now().time().hour)

## print the current time Minutes  

print(datetime.datetime.now().time().minute)


## print the current time second
print(datetime.datetime.now().time().second)

print("^"*30)
## print the sart and end of the time 
print(datetime.time.min)
print(datetime.time.max)

print("^"*30)
## print specific date 

print(datetime.datetime(1983,1 ,14))

print(datetime.datetime(1983,1,14,21,54,12))

myBD =  datetime.datetime(1983,1 ,14)
dateNow = datetime.datetime.now()

print("my birth day is : ",myBD)
print("date now : ",dateNow)

print("I've lived for : ",dateNow-myBD)
print("I've lived for : ",(dateNow-myBD).days, " Days" )
