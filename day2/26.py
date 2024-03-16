n=1441
res=0
sum=0
n1=n
while(n>0):
    res=n%10
    sum=sum*10+res
    #sum=sum+res
    n=n//10
if(n1==sum):
    print("palindrome")
else:
    print("not a palindrome")
