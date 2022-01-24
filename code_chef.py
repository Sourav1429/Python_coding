import numpy as np
def sub_val(height,l,u):
    val=0;
    while(l<u):
        val=val+height[l];
        l+=1;
    return val;
def max_water(height):
    length=len(height);
    i=0;j=length-1;
    left=-1;right=-1;water=0;
    while(i<length):
        if(height[i]>0):
            if(left==-1):
                left=i;
            else:
                if(height[i]>=height[left]):
                    right=i;
                    water=water+min(height[left],height[right])*(left-right-1)-sub_val(height,left+1,right-1);
                    left=-1;
                    right=-1;
                    i-=1;
                '''else:
                    right=i;
                    water=water+min(height[left],height[right])*(left-right-1)-sub_val(height,left,right);
                    left=-1;
                    right=-1;
                    i-=1;  '''
        i+=1;
    return water;
print(max_water([0,1,0,2,1,0,1,3,2,1,2,1]));
                
