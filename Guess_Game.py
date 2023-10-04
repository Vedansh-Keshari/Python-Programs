

secret = "giraffe"
guess=""
c=0
limit=3
out = False

while guess!=secret and not(out):
     if c<limit:
        guess = input("Enter guess : ")
        c+=1
     else:
        out = True

if not(out):
    print("You Win !!!")
else:
    print("Out of guesses, You Lose !!!")