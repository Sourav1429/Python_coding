''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
def main():

    V="coronavirus";flagbr=1;
    hash={};
    for j in range(len(V)):
        if(hash.get(V[j],None)==None):
            node=Node(j);
            hash[V[j]]=node;
        else:
            node=Node(j);
            head=hash[V[j]];
            while(head!=None):
                #print(head.dataval);
                if(head.nextval==None):
                    head.nextval=node;
                    break;
                head=head.nextval;
    #print(hash['o'].nextval.dataval);
    flagbr=1;last_index=-1;
    B="onarous";
    for j in B:
        if(hash.get(j,None)==None):
            print("1NEGATIVE");
            flagbr=0;
            break;
        else:
            head=hash[j];flag=0;a=0;
            while(head!=None):
                a=head.dataval;
                if(a>last_index):
                    flag=1;
                    break;
                head=head.nextval;
            if(flag==0):
                print("2,",j,",NEGATIVE")
                flagbr=0;
                break;
            print(a);
            last_index=a; 
    if(flagbr==1):
        print("3POSITIVE");

main()

