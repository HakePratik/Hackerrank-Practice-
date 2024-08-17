n = int(input("Enter the number of elements in the array: "))
ar = list(map(int, input(f"Enter {n} space-separated integers: ").strip().split()))
n=len(ar)
def aVeryBigSum(ar):
   return sum(ar)
   if 1<=n<=10:
        print ('n is available range')
        for i in ar:
          if (0<=ar[i]<=10**10):
               print ('....')
result = aVeryBigSum(ar)
print(result)  
