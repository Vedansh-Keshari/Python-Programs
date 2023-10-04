import random
def choose():
    words=["rainbow","program","reverse","water","power","discipline","mathematics","pocket","condition"]
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1,p2,pp1,pp2):
    print(p1,"scored",pp1)
    print(p2,"scored",pp2)
    print("Thank you",p1,"and",p2,"for playing\nHave a nice day")

def play():
    p1name=input("Player 1 : ")
    p2name=input("PLayer 2 : ")
    points1=0
    points2=0
    turn=0
    while(True):
        word=choose()
        ques=jumble(word)
        print("Question word :",ques)
        if(turn%2==0):
            print("It is your turn ",p1name)
            ans=input("Give your answer here : ")
            if(ans==word):
                points1=points1+1
                print("Score of",p1name,"is",points1,"now")
            else:
                print("Better luck next time. Correct answer was \"",word,"\"")
            c=int(input("Press 1 to continue and 0 to quit : "))
            if(c==0):
                thank(p1name,p2name,points1,points2)
                break
        else:
            print("It is your turn ",p2name)
            ans=input("Give your answer here : ")
            if(ans==word):
                points2=points2+1
                print("Score of",p2name,"is",points2,"now")
            else:
                print("Better luck next time. Correct answer was",word)
            c=int(input("Press 1 to continue and 0 to quit : "))
            if(c==0):
                thank(p1name,p2name,points1,points2)
                break
        turn=turn+1
        
play()