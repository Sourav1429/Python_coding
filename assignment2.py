#wap to check whether the number is an armstrong number or not

n=int(input("Enter a number:"))
d=n
num=0
while(d!=0):
    num=num+(d%10)*(d%10)*(d%10)
    d=d//10

if(n==num):
    print("Armstrong number")
else:
    print("Not an armstrong number")
