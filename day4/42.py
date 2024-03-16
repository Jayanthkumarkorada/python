# def check(n):
#     if n%2==0:
#         print("yes")
#     elif (n+1)%2==0:
#         print("no")
#     else:
#         print("Enter again")
# lis=[2,3,471,7,13].list(map(int,input().split()))
# print(check(lis))
#////////////////////////////////////////////////////////////
# my={1,2,5,6,7,8,5,9,5,"jayanth","kumar","korada"}
# print(my[8])
#////////////////////////////////////////////////////////////
#2,0,1024,0,40,230,0
a=[2,0,1024,0,40,230,0]
b=[]
for i in range(len(a)):
    if(a[i]!=0):
        b.append(a[i])
for i in range(len(a)):
    if(a[i]==0):
        b.append(a[i])
print(b)
# m1=0
# m2=0
# while(m1<len(a)):
#     if(a[m1]!=0):
#         temp=a[m1]
#         a[m1]=a[m2]
#         a[m2]=temp
#         m1+=1
#         m2+=1
#     else:
#         m1+=1
# print(a)
    
    