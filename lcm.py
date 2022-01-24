#find lcm
a=int(input("Enter a number="))
b=int(input("Enter a number="))
if (a==0 or b==0):
    print("LCM not possible:");
    

lcm=1

for i in range(1,a*b):
    if(a<=1 and b<=1):
        break
    
    if ((a%i==0)):
        lcm*=i
        a/=i
    if((b%i)==0):
        lcm*=i
        b/=i
        
    
print(lcm)   
    

