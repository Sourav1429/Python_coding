#WAP to find the factorial of a number using recursion

n=int(input("Enter a number"))
def fact(n,facto=1):
    if(n>0):
        facto=facto*n
        fact(n-1,facto)
    else:
        print(facto)

fact(n)
