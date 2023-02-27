# ------------------------------------------------------------
# --    Databases => SQLite => Create Skills App Part 1     --
# ------------------------------------------------------------

## input bog message 
input_message = '''
what do you want to do ?
"s" => Show all Skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update skill progress
"q" => Quit The App
choose Option : 
'''

# Input option chosse 
user_input = input(input_message).strip().lower()

##command List : 
commands_list = ["s", "a", "d", "u", "q"] 

## defind the methods 
def show_skills():
    print("Show skills")

def add_skill():
    print("Add skill")

def delete_skill():
    print("Delete skill")

def update_skill():
    print("Update skill progress")

## check if command is exist 

if user_input in commands_list:
    print("commands found ")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else :
        print("App is closed")

else :
    print(f"Sorry this command \"{user_input}\"  is not found ")