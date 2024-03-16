#check if the given year is leap year or not
#if the year is divisible by 4 and not divisible by 100 or if it is divisible by 400 then it is leap year
a=int(input("year: "))
if a%4==0 and a%100!=0:
    print("leap year")
elif a%400==0:
    print("leap year") 
else:
    print("not a leap year")


#if(y%4==0 and y%100!=0) or y%400==0