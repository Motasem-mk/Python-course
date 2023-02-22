
##-------------------------------##
##----- Function and return -----##
##-------------------------------##

#[1] A Function is a reusable block of code that does a task 
#[2] A Function run when you call it
#[3] A Function accept elements to deal with called [Parameteres]
#[4] A Function can do the task without returning data 
#[5] A Function Can return data after job is fininshed 
#[6] A Function create to prevent DRY ( Don't Repeat Yourself )
#[7] A Function accept elements when you call it called [Arguments]
#[8] there's a built-in Functions and user define functions 
#[9] A Function is for all team and all apps 
# -----------------------------------------------------------------

def function_name ():
    print("Hello This is from inside a function") 

# it doesn't return data  but it does its function in printing this message 

function_name() 
 
## return data 
def fun_return_data ():
    return "Hello This is from inside a function \"Return Data\" "

Data_from_Function = fun_return_data()
print(Data_from_Function)