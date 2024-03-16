# #factorial of a number
# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# #fibonacci of a number
# def fab(n):
#     if n<1:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# print(fab(5))

#reverse digits using recursion
# def rec(n):
#     if(n==0):
#         return 
#     else:
#         print(n%10)
#         rec(n//10)
# rec(12345)

#write the recursive function to count the no.of digits of a number

# def rec(n):
#     if(n==0):
#         return 0
#     else:
#         return 1+rec(n//10)
# print(rec(123405))


#sum of digits using recursion
#def rec(n):
#     if(n==0):
#         return 0
#     else:
#         return n%10+rec(n//10)
# print(rec(123405))

#armstrong number in recursion
def arm(n):
    if(n==0):
        return 0
    else:
        return 1+arm(n//10)
    
#print(arm(153))
def asd(s,p):
    if(s==0):
        return 0
    else:
        return (s%10)**p+asd(s//10,p)
print(asd(153,arm(153)))
