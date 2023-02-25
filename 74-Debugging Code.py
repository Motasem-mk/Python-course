
# --------------------
# -- Debugging Code --
# --------------------

my_list = [1, 2, 3, 4, 5]
my_dictionary = {
    "Name" : "Osama",
    "Age":36,
    "country":"Egypt"
}

for n in my_list : 
    print(n,end=" ")

for key,value in my_dictionary.items():
    print(f"\n\n{key} : {value}")

def say_hello(name):
    return f"Hello {name}"

print(say_hello("m"))