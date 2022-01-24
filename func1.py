#write a function that takes a number and checks for its equality to a global variable
var=int(input("Enter a variable:"))

def foo(c):
    global var
    if (var==c):
        print("Equal")
    else:
        print("Not equal")


