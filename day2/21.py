
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(6-i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         if(i+j>=5):
#             print("*",end="")
#         else:
#             print(" ",end=" ")
#     print()
# r=4
# for i in range(1,r+1):
#     for s in range(1,r-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# r=5
# for i in range(1,6):
#     for s in range(1,r-i+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
for i in range(1,5):
    for j in range(1,5):
        if(i==1 or i==4 or j==1 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()