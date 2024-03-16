n1=0
n2=1
n3=0
d=[]
print(n1)
print(n2)
d.append(n1)
d.append(n2)
for i in range(2,10):
    n3=n1+n2
    n1=n2
    n2=n3
    d.append(n3)
    print(n3)
print(d)