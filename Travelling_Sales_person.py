import numpy as np
''' below is the function for traveller salesman
Basic order of the matrix if suppose N=3 is as below
arr=[[0,a,b],
     [c,0,d],
     [e,f,0]]
==========Considering (0,0) as my starting vertex================='''
def TSP(arr,l,u):
    visited.append(l);#keep track of the vertices visited
    S=[i for i in range(u) if i not in visited];#find the unvisited vertices
    print(S);#printing the unvisited vertices in each step. Just for checking has no importance in the code
    if not S:#Base condition if we hit the last edge. 
        visited.remove(l);#removing that vertex from list or poping that value out
        return arr[l][0];#returning the final value when we have no more vertex to be visited
    min=float('inf');#defining maximum as my min value
    for i in S:#loop to consider the remaining value 
        val=arr[l][i]+TSP(arr,i,u);
        if(min>val):
            min=val;
    visited.remove(l);
    '''find the minimum value from recursion with the general formula as cost=min(C1k+g(k,S))
where k runs from 0 to N-1 and S is the set of unvisited values'''
    return min;
def main():
    N=int(input());#inputting dimensions of matrix
    print("Enter values of the matrix. But remember self loop values=0");
    arr=np.zeros((N,N));
    for i in range(N):
        for j in range(N):
            arr[i][j]=int(input());#entering the distance value keeping in mind self loop edges distance=0
    print(TSP(arr,0,N));#final display of output
visited=[];
main();#calling the main()
