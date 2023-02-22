#integer
print(type(100))
print(type(1))
print(type(-100))
print(type(-10))
print("#"*50)
# float
print(type(1.54))
print(type(-100.3))
print(type(.04))
print("#"*50)
#complex \
myComplexNum = 5+6j
print(type(5+6j))
print(f"this is the real number : {myComplexNum.real}")
print(f"my imaginary Number is {myComplexNum.imag}")
print("#"*50)

# convert number 
N=100
print(N)
print(float(N))
print(complex(N))
print("#"*50)

I=100.50
print(type(I))
print(int(I))
print(complex(I))

# x = 10+9j
# print(type(x))
# print(int(x))
# print(float(x))
print("#"*50)

#--- Arithmatic Operators ----#

# [+] Addition
print(10+30)
print(-2.3+4.5)
# [-] Substraction
print("#"*50)
print(-19-3)
print(-3- -2)
print("#"*50)

# Multiplication 
print(1*4)
print(1+3*2)
print((2+4)*10)
print("#"*50)
# Division
print(100/20)
print(int(100/20))
 
print("#"*50)

# Modulus
print(8%2) # 0 
print(9%2) #1
print(20%3) #2

print("#"*50)

# Exponent
print(2**5) # 32
print(2*2*2*2*2) #32

print(5**4) # 625
print(5*5*5*5)
print("#"*50)
## Floor Division
print(100//20) #5
print(110//20) #5
print(120//5) # 24 
print(123//5) #24
print(138//5) #27
print(138//5) # 27
print(139//5) #27 
print(140//5) #28

print(2.3e4) #  2.3 x 10 power 4 

food= '200.5'
bills = '120'
print(food+bills)
f=200.5
bi=120
print(f+bi)

print(type(1.2e3))
r=84
area=3.14*84**2 
print(area)
total_amount_of_water= area*1.4/1
print(f"totale amount of water = {total_amount_of_water}")

distance_crossed=490
time=7
speed=distance_crossed/time 
print(f"the speed  = {int(speed)} m\s")