 
def translate(phrase):
     t = ""
     for letter in phrase:
         #if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":
            if letter.isupper():
             t = t+"G"
            else:
             t = t+"g"
        else:
             t = t+letter
     return t

print(translate(input("Enter a phrase :")))

