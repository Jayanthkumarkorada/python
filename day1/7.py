n=int(input("n: "))
count=0
if(n%2==0):
    flag=1
else:
    for i in range(2,n//2):
        if n%i==0:
            count=1
            break
    if (count>=1):
        print("not prime")
    else:
        print(" prime")
       
       