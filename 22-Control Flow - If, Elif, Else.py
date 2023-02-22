##---------------------------##
##------ Control Flow -------##
##----- If, Elif, Else ------##
##------ Make Descisions ----##
##---------------------------##


uName = input("Enter your name : ").strip().capitalize()
country = input ("Where are you from ? ").strip().capitalize()  #"Egypt".strip().capitalize()
courseName = "Python course"
coursePrice = 100
Cdiscount = 30
Cdiscount_world = 20

if country== "Egypt":
        print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}\nbut becasue you are from {country}")
        print(f" you have got a discount of {Cdiscount} , the course price now is {coursePrice-Cdiscount} ")
elif country == "Saudi Arabia" :
     print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}")
     print(f"but becasue you are from {country}\n you have got a discount of 40 , the course price now is {coursePrice-40} ")

else:
    
    print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}\n nbut becasue you are from {country}")
    print(f"you have got a discount of {Cdiscount} , the course price now is {coursePrice-Cdiscount} ")