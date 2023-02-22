## --------------------- ##
## ---- User Input ----- ##
## --------------------- ##

first_name = input(" what\'s your first name ? ").strip().capitalize() 
middle_name = input ('what\'s your middle name ? ' ).strip().capitalize() 
last_name = input('what\'s your last name ? ' ).strip().capitalize()

print(f'Hello {first_name} {middle_name:.1s} {last_name} Happy to see you ')