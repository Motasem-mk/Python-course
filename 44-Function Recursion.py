## --------------------------- ##
## -----Function Recursion --- ##
## --------------------------- ##

## ----------------------------------------------------------------------- ##
## ----To understand Recursion, you need to first understand Recursion --- ##
## ----------------------------------------------------------------------- ##


def recursion_funcion(word):

    if len(word) == 1:
        return word
    
    print(f"Start Function: {word}")
    if word[0] == word[1] :
      
        print(f"Before condition: {word}")


        return recursion_funcion(word[1:]) # woorrrlldd
        
        
    print(f"before return : {word}")
    return word[0] + recursion_funcion(word[1:])

    # stash [worl]
   
print(recursion_funcion("wwwoorrrlldd"))
 