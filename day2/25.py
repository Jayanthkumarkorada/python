#calculate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers
#n=int(input("n: "))
max=0
min=0
i=0
while(i<=30):
    if(i%6==0):
        max=max+i
    elif(i%6!=0):
        min=min+i
    i=i+1
print(min-max)