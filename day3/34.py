# lis=[1,"mani","pavan","sai","veesam"]
# lis.append(2)
# #print(lis)
# print(lis[1:5:2])
# print(lis[::-2])
# print(lis[0:3:2])
# lis.insert(2,0)
# print(lis)
# list=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# lis[1]="jayanth"
# print(lis)
# print(list)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# list=[12,42,23,96,7,18,10,133]
# min=list[0]
# max=list[0]
# min_id=0
# max_id=0
# for i in range(0,len(list)):
#     if(list[i]>max):
#         max=list[i]
#         min_id=i
#     elif(list[i]<min):
#         min=list[i]
#         max_id=i
# list[min_id]=max-min
# list[max_id]=max+min

# print(min+max)
# print(list)
#///////////////////////////////////////////////////////////////////
#Tuples
t1=(1,2,3,"hello","world")
t1=t1+("vamsi",)
print(t1)
for i in range(0,5):
    n=int(input("enter: "))
    t1=t1+(n,)
print(t1)

    