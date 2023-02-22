## ----------------------------- ##
## ---- Break Continue Pass ---- ##
## ----------------------------- ##

mynumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

### Continue
for number in mynumbers :
    if number == 13 :
      continue # will stop the current iteration and skip it 
               # 13 will not be printed 
               # the loop will contune after skipping the number 13 

    print(number)


print("^"*10)

### Break
for number in mynumbers :
    if number == 13: 
        break  # it will stop the loop and wont print 13 
    print(number)

print("^"*10)

### pass 
for number in mynumbers :
    if number == 13: 
         pass   # it will pass and continue the loop  
    print(number)
