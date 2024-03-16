#abundant #check if the sum of factors is greater than the number
n=int(input("n: "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum>n):
    print("good")
else:
    print("bad")
