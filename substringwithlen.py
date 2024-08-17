def hmss(string,lenofsubstr):
    result=""
    for i in range (0,len(string),lenofsubstr):
        result+=string[i:i+lenofsubstr]+"\n"
    return result
a,b=input (),int(input ())
s=hmss(a,b)
print(s)