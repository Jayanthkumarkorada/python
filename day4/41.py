lis=[22,-1,42,65,1,-4,6]
min1=lis[0]
min2=lis[0]
l=[]
for i in lis:
    if i<min1:
        min1=i
for i in lis:
    if i>min1 and i<min2:
        min2=i
print(min2)


####################################################################################
# m1=999
# m2=999
# for i in lis:
#     if(i<m1):
#         m2=m1
#         m1=i
#     elif(m2>i and m2>m1):
#         m2=i
# print(m2)
