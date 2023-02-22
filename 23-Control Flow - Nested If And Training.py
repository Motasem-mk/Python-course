##--------------------------------------------------------##
##------- Control Flow - Nested If And Training ----------##
##--------------------------------------------------------##

uName = input("Enter your name : ").strip().capitalize()
country = input ("Where are you from ? ").strip().capitalize()  #"Egypt".strip().capitalize()
isStudent= input("Are you a student ? enter Yes/Y").strip().capitalize()
courseName = "Python course"
coursePrice = 100
Cdiscount = 30
Cdiscount_world = 20

if country== "Egypt":
    if isStudent=="Yes" or isStudent=="Y" :
            print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}\nbut becasue you are from {country}")

            print(f" and because you are a Student youve got an extra discount of $60 ")
            print(f"the course price is {coursePrice-60}")
    else :    
            print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}\nbut becasue you are from {country}")

            print(f" you have got a discount of {Cdiscount} , the course price now is {coursePrice-Cdiscount} ")
elif country == "Saudi Arabia" or country=="Algeria" :
     print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}")
     print(f"but becasue you are from {country}\n you have got a discount of 40 , the course price now is {coursePrice-40} ")

else:
    
    print(f"Hello {uName} the course is : \"{courseName}\" price is : {coursePrice}\n nbut becasue you are from {country}")
    print(f"you have got a discount of {Cdiscount} , the course price now is {coursePrice-Cdiscount} ")