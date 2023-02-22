## --------------------------------- ##
## --- Built In Functions Part 3 ----##
## --------------------------------- ##

# abs()
# pow()
# min()
# max()
# slice()
#-------------------------------------#

# abs()

print(abs(100))     # 100
print(abs(-100))    # 100
print(abs(100.19))  # 100.19
print(abs(-100.19)) # 100.19

print("^"*30)

# pow(base,exponent,modulus) => power . exponent 
## base and exponent must be there 
# mod is not a must 

print(pow(2,0))    # 1
print(pow(2,5))    # 2*2*2*2*2 = 32
print(pow(2,5,10)) # 2  :  (2*2*2*2*2) % 10 .. 30%10 == 0 .. remain 2 
print("^"*30)
# min(item , item ,item , or iterator) 

print(min(2,3,-1,50)) # -1
print(min("a","b","z")) #a
mynum=(1,3,-1,40,-20)
print(min(mynum)) #-20
print("^"*30)
# max(item , item ,item , or iterator) 
print(max(2,3,-1,50)) # 50
print(max("a","b","z")) #z
mynum=(1,3,-1,40,-20)
print(max(mynum)) #40

#slice(start,stop,step)
a=["A", "B", "C", "D", "E", "F"]
print(a[:5])       # ['A', 'B', 'C', 'D', 'E'] not including the end as usual 
print(a[slice(5)]) # will give the same result ['A', 'B', 'C', 'D', 'E']
print(a[slice(2,5)]) # ['C', 'D', 'E']
print(a[slice(0,5,2)]) # steps =2 , ['A', 'C', 'E']
print("Hello My name is Motasem"[slice(0,26,2)]) # HloM aei oae