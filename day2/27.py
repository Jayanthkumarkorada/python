#armstrong number 153=1**3+5**3+3**3
n=int(input("n: "))
nod=0
sum=0
digit=0
n1=n
while(n>0):
    nod=nod+1
    n=n//10
org=n1
while(n1>0):
    digit=n1%10
    sum=sum+digit**nod
    n1=n1//10
if(sum==org):
    print("armstrong")
else:
    print("not armstrong")

    

