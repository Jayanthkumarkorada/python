#write a program one single subject marks if the marks are greater than 35 print cheated if the marks are less than 35 print
a= int(input("n1: "))
if a%3==0 and a%6==0:
    print("Good number")
elif a%2==0 and a%7==0:
    print("Average number")
elif a%4==0 or a%9==0:
    print("Awesome number")
else:
    print("Bad number")
#write a program to check on road price of a bike under the condition if the price is greater than 72000 then income tax is 10% of the original price
#and insurance will be 15% of the actula price,if the price is greater than 1500000 and less than 2 lakh the tax would be 25% and the insurance
#will be 25%
#if the price is above 2lakh ,then tax will be 35% insurance will be 28%
#otherwise minimum price starts with 72000 then display enter a valid value. print the onroad price of bike actual+insurance+tax
b=int(input("n2: "))
income=0
ins=0
total=0
if b>72000 and b<150000:
    income=b*10//100
    ins=b*15//100
    total=b+income+ins
    print(total)
elif b>150000 and b<200000:
    income=b*25//100
    ins=b*20//100
    total=b+income+ins
    print(total)
elif b>200000:
    income=b*35//100
    ins=b*28//100
    total=b+income+ins
    print(total)
elif b<72000:
    print("enter valid number")

