import numpy as np
def STH(i,arr):
    '''for j in range(i+1,10):
        if(i+k<=j):
            di=1;
        else:
            di=0;
        for k in range(i+1,j):
            fn[i][j]=fn[i][j]+fn[k][j];
        fn[i][j]+=di;'''
    row=i-1;
    for j in range(i+1,9):
        row+=1;
        column=j;
        if(row+arr[row]<=j):
            di=1;
        else:
            di=0;
        for k in range(row+1,j):
            fn[row][column]=fn[row][column]+fn[k][j];
        fn[row][column]+=di;
def main():
    N=10;
    global fn;
    fn=np.zeros((N,N));
    arr=input().split();
    arr=[int(x) for x in arr]
    for i in range(0,N-1):
        STH(i,arr);
    print(fn);
fn=[];
main();
