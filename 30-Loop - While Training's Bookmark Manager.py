## -------------------------------- ##
## ---- Loop => While Training ---- ##
## ---- Simple Bookmark Manage ---- ##
## -------------------------------- ##


# Empty list of Bookmark to fill later 
myFavWebsites=[]

# Maximum allowed 
maxWebs = 5

while maxWebs > 0 :
    web = input("Enter your website :https://").capitalize().lower()
    myFavWebsites.append(web)
    maxWebs-=1
    print(f"https://{web} is added")
    print(f"you have {maxWebs} left\n{myFavWebsites}")
else :
 ("your Bookmark list is Full ")


if len(myFavWebsites)>0 :
    myFavWebsites.sort()
    index = 0 
    while index < len(myFavWebsites):
            print(myFavWebsites[index])
            index+=1
            
