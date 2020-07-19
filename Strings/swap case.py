def swap_case(s):
    s1=''
    for i in s:
        if(i.isupper()):
            i=i.lower()
            s1+=i
        else:
            i=i.upper()
            s1+=i    
    return s1
