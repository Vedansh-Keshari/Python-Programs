

male = True
tall = True

if male and tall :
    print("You are a tall male")
elif male and not(tall) :
    print("You are a short male")
elif not(male) and tall :
    print("You are not a male but are tall")
else :
    print("You are not a male and not tall")


#                 All Strings are treated as True
#                 Only empty Strings are considered as False