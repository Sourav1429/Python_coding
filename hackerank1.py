'''import numpy as np
def main():
    T=int(input());
    for i in range(T):
        N=int(input());
        #output modulo 10^9+7
        1 <= T <= 60000
            1 <= N <= 1018
        arr=np.zeros((N,N));
        for i in range(N):
            for j in range(N):
                if(j-i>1):
                    arr[i][j]=1;
    return arr;
print(main());'''
def pos(arr,T,val):
    sum=0;
    #print("Entered");
    for j in range(T):
        sum+=arr[j];
        if(sum>=val):
            print(j+1);
            return;
    print(-1);
def main():
    T=int(input());
    arr=input().split();
    arr=[int(x) for x in arr]
    Q=int(input());
    for i in range(Q):
        val=int(input());
        pos(arr,T,val);
main(); 
        
        
