
##-----------------------------------##
##----------- Email slicing ---------##
##-----------------------------------##


the_Name = input("What\'s your Name ? ").strip().capitalize()
the_Email = input ('what\'s your email? ' ).strip()

print(f'Hello {the_Name} ,  your email is : {the_Email}')

position_of_at=the_Email.index("@")
#2print(f"Your user name is {the_Email[:position_of_at]} and your website  is {the_Email[ position_of_at+1:]} ")


#or like this 
user_name = the_Email[:position_of_at].strip().capitalize()
website_name = the_Email[the_Email.index("@")+1:]
print(f"Your user name is : {user_name} \nyour website  is : {website_name} ")

# email="Osama_elzero@elzero.org"
# print(email[0])
# print(email.index("@"))
# print(email[:email.index("@")])
