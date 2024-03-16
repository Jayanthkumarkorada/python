# #positional arguments----by the position of a arguments
# def typecast(a,b):
#     c=int(b)
#     d=a*c
#     print(d%10)
# typecast(8,3.3)

# #keyword arguments---by passing the argumentd we mention the parameter
# def keyword(a,b):
#     print(a,"hello",b)
# keyword(b=10,a=5)

# #default arguments---
# def city(name="ram",place="abc"):
#     print("my name is",name,"place",place)
# city()
# city("jayanth","srikakulam")
# #unknown arguments--
# def func(**name):
#     print("my name is ",name["lname"])
# func(fname="jayanth",lname="kumar")
#write a function to calculate the sum of first and last digit of a number
def sum(a):
    a1=a
    b=a%10
    a=b
    while(a1>0):
        rem=a1%10
        a1//=10
        last=rem
    print(a+last)
sum(785)

