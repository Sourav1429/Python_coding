import random
system_random = random.SystemRandom()
misses=0;
output=list();
inp=list();
def get_guess():
    global misses,output,inp;
    while(misses!=7):
        flag=0;
        c=input('Enter a character:').upper();
        if(len(c)>1):
            print("Error! \n Multiple character inputted");
            continue;
        elif(not(c.isalpha())):
            print("Error! \n Enter 1 letter only");
            continue;
        #c=c.upper();
        for i in range(len(inp)):
            if(c==inp[i]):
                if(output[i]==c):
                    print("You have already entered this character:")
                    break;
                output[i]=c;
        if(c not in output):
            misses+=1;
        for i in output:
            if(i=='-'):
                flag=0;
                break;
            flag=1;
        if(flag):
            print_game_state();
            print("Congratulation!, You have won");
            return;
        else:
            print_game_state();
    print("Sorry mate. You lost.")
    return;
def print_game_state():
    global misses,output,inp;
    print('You have made ',misses,' misses. Number of misses left:',(7-misses));
    print('Your current state:');
    print(''.join(output));
def initialize_all():
    global misses,output,inp;
    possibilities=["SUNNY"]#enter your words here
    #inp='''Enter the required word here in quotes for example check below comment'''
    inp=possibilities[system_random.randint(0, len(possibilities))];
    for i in range(len(inp)):
        output.append('-');
def one_game():
    global misses,output,inp;
    while True:
        misses=0;
        output=list();
        inp=list();
        print('Ready to play\n Let\'s rock and roll');
        print('You have 7 misses. At present number of misses allowed is 7');
        print('Your guessing word is below');
        initialize_all();
        print(''.join(output));
        get_guess();
        ch=input("Do you want to play again[y/n]");
        if(ch=='n'):
            print("Program quitting");
            break;
        elif(ch=='y'):
            continue;
        else:
            printf("Sorry wrong input\n Program quitting");
            return;    
one_game();
