# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class Member :
    
    not_allowed_names = ["Hell", "Shit","Baloot"]
    users_num = 0 

    def __init__(self,first_name,middle_name,last_name,gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_num+=1


    def full_name(self) :
        if self.fname in Member.not_allowed_names:
          raise ValueError("Name Not Allowed")
        else :
          return f"{self.fname} {self.mname} {self.lname}"
    
    def name_with_title(self):
        if self.gender == "Male" :
            return f"Hello Mr. {self.fname}"
        elif self.gender=="Female":
            return f"Hello Miss {self.fname}"
        
        else :
            return f"{self.fname}"
        
    def get_all_info(self):
        return f"{self.name_with_title()} , you full name is : {self.full_name()}"
    
    def delete_user(self):
        Member.users_num-=1
        return f"User {self.fname} id deleted "


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")

memeber_two = Member("Ahmed", "Ali", "Mahmoud", "Male")

member_three = Member("Mona", "Ali", "Mahmoud", "Female")

member_four = Member("Shit", "Hell", "Metal", "DD")


# print(member_one.full_name())

# print(member_three.name_with_title())

#print(member_one.get_all_info())

#print(member_four.get_all_info()) #V alueError: Name Not Allowed

# print(dir(Member))

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)
