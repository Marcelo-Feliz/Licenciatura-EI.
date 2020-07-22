def espelho(str):
    s=len(str)
    x=s-1
    l=''
    while x>=0:
        l=l+str[x]
        x=x-1
    print(str+l)    
