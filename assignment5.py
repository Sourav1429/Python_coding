#WAP for developing a game of stone paper scissors
from random import randint
score={'user':0,'computer':0}
options=["stone","scissors","paper"]
def print_menu():
    global options
    print("Enter 1 for {}".format(options[0]))
    print("Enter 2 for {}".format(options[1]))
    print("Enter 3 for {}".format(options[2]))

def print_scores():
    global score
    print("---SCORES---")
    print("USER  :  ",score['user'])
    print("COMPUTER  :  ",score['computer'])

def print_won():
    global score
    if (score['user']>score['computer']):
        print("You won the match, I'll see you next time")
    else:
        print("Better luck next time")
#-----------------------------------------------------------------------
while((score['user']!=5)and(score['computer']!=5)):
    print_menu()
    a=int(input("Enter your choice:"))
    b=randint(1,3)
    print("You chose {} and computer chose {}".format(options[a-1],options[b-1]))
    if(((a==1) and (b==2))or((a==2)and(b==3))or((a==3)and(b==1))):
        print("Uggh!! I lost this round")
        score['user']=score['user']+1
        print_scores()
        input("press return key to continue")
    elif(((a==2) and (b==1))or((a==3)and(b==2))or((a==1)and(b==3))):
        print("Yes!!! I win this round")
        score['computer']=score['computer']+1
        print_scores()
        input("press return key to continue")
    else:
        print("Gosh! same symbol")
        print_scores()
        input("press return key to continue")
print_won()
