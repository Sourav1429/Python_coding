#wap which takes as input 2 numbers and return their lcm

a=int(input("Enter an integer:"))
b=int(input("Enter an integer:"))

while(a!=0):
    n=b%a
    b=a
    a=n
print(b);
