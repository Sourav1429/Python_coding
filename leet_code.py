class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def traverse(a):
    while(a!=None):
        print(a.val,sep=' ');
        a=a.next;
    print("====================");
def reverseLL(head,end,prev):
    curr=head;beg=head;
    while(curr!=end):
        head=head.next;
        curr.next=prev;
        prev=curr;
        curr=head;
    beg.next=end;
    #traverse(prev);
    return prev
def separate(a):
    i=0;beg=a;prev=None;flag=0;ret_head=None;
    while(a!=None):
        i+=1;
        if(i%2==0):
            end=a.next
            head=reverseLL(beg,end,prev);
            if(flag==0):
                ret_head=head;
                flag=1;
            else:
                prev.next=head;
            prev=beg;
            a=beg;
            beg=end;
        a=a.next;
    return ret_head;
a=ListNode(1);
head=a;
new_node=ListNode(2);
a.next=new_node;
a=new_node;
new_node=ListNode(3);
a.next=new_node;
a=new_node;
new_node=ListNode(4);
a.next=new_node;
a=new_node;
new_node=ListNode(5);
a.next=new_node;
a=new_node;
new_node=ListNode(6);
a.next=new_node;
a=new_node;
new_node=ListNode(7);
a.next=new_node;
a=new_node;
new_node=ListNode(8);
a.next=new_node;
a=new_node;
#traverse(reverseLL(head,None,None));
traverse(separate(head));