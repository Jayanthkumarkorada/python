#If the number is divisible by sum of numbers  
n=int(input("n: "))
res=0
sum=0
n1=n
while(n>0):
    res=n%10
    sum=sum+res
    n=n//10
if(n1%sum == 0):
    print("divisible")
else:
    print("Not divisible")
