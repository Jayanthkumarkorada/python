n=input("Enter the type of car: ")
#lis=("Mahindra","Toyato","Mercedes")
#n=int(input("Enter the car you want: "))
class mercedes1:
    def __int__(self):
        print("Welcome to the mercedes")
class toyato1:
    def __init__(self):
        print("Welcome to the toyato")
class mahindra1:
    def __init__(self):
        print("welcome to the mahindra")
def welcome(company):
    if n=="mercedes":
        obj=mercedes1()
    #obj.mercedes1()
    elif n=="toyato":
        obj=toyato1()
    #obj.toyato1()
    elif n=="mahindra":
        obj=mahindra1()
    #obj.mahindra1()