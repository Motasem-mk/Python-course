# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator (func):
    def nested_func (num1,num2):
        if num1<0 or num2<0:
            print("Be aware one of the numbers are less than zero")
        func(num1,num2)
    return nested_func

def myDecorator2 (func):
    def nested_func (num1,num2):
       
        print("coming from decorator 2 ")
        func(num1,num2)
    return nested_func



@myDecorator
@myDecorator2
def summ (n1,n2):
    print(n1+n2)
    return

summ(-1,3)