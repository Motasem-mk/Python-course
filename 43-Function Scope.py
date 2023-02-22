## -------------------------- ##
## ----- Function Scope ----- ##
## -------------------------- ##


x=1 # global scope 

print(f"Global scope x= {x}") 

def one():
    global x
    x=2
    print(f"First Function scop x= {x}")
one()

def two():
    x=4
    print(f'Second functions cope x={x}')
two()

print(f"Global scope after the change inside the first function x= {x}")
