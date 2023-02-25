# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------

import re 

string_one = "I Love Python"

search_one = re.split(r"\s",string_one,1)

print(search_one)

print("^"*30)

string_two = "How-To_Write_A_Very_Good-Idea"

search_two = re.split(r"-|_",string_two)

print(search_two)

## Get words From URL 

for  counter, word in enumerate( search_two,1 ) :
    if len(word) == 1 : # to not print the letterd only words 
       continue 

    print(f"word number {counter} : {word.lower()}")

## sub 

my_string = "I Love Python"
print(re.sub(r"\s","-",my_string,1))
