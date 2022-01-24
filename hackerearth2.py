import numpy as np
def STH(r,k,N):
    global fm;
    end=0;
    if(r+k+1>=N):
        end=N;
    else:
        end=r+k+1
    for i in range(r+1,end):
        fm[r][i]=(fm[r][i]+1);
def main():
    N=int(input());
    global fm;
    fm=np.zeros((N,N));
    #print(fm);
    #print("=============================");
    arr=input().split();
    for i in range(N):
        STH(i,int(arr[i]),N);
    sum=0;
    print(fm);
    '''for i in range(N):
        sum=(sum+fm[i][-1])%1000000007;
    print(int(sum));'''
fm=[];
main();
