my_dict={'2':['a','b','c'],
'3':['d','e','f'],
'4':['g','h','i'],
'5':['j','k','l'],
'6':['m','n','o'],
'7':['p','q','r','s'],
'8':['t','u','v'],
'9':['w','x','y','z']}
def numbers(a):
    ret=[];ret_val=[];flag=1;
    for i in a:
        ret=my_dict[i]
        if(flag):
            ret_val=ret;
            flag=0;
        else:
            l=len(ret_val);
            l2=len(ret)
            for j in range(l):
                for k in range(l2):
                    s=ret_val[j]+ret[k];
                    print(s);
                    ret_val.remove(ret_val[j]);
                    ret_val.append(s);
    return ret_val;
print(numbers("237"));


