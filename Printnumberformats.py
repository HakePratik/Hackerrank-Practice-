def printformat(N):
    w=len(bin(N))-2
    for i in range (1,N+1):
        decimal=str(i)
        octal=oct(i)[2: ]
        hexadecimal=hex(i)[2: ]. upper ()
        binary=bin(i)[2: ]
        print (f"{decimal:>{w}}  {octal:>{w}}  {hexadecimal:>{w}}    {binary:>{w}}")
N=int(input("enter no upto print format:"))
print ("deci.   oct.    hexa.    bin.  ")
format=printformat (N)