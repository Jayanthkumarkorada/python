#1578==== 1**1+5**2+7**3+8**4  reverse order
n=1578
count=0
a=n
sum=0
digit=0
while(n>0):
    count=count+1
    n=n//10
while(a>0):
    digit=a%10
    sum=sum+digit**count
    count=count-1
    a=a//10
print(sum)

