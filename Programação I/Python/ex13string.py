def rot13(str):
    ret=''
    for c in str:
        ret=ret+r13(c)
    return ret

def r13(s):
    d=ord(s)-ord('a')
    f=(d+13)%26
    return chr(ord('a')+f)
