#Abstraction
#create a class ticket which will be the abstract class,inside that create a function book ticket which will be the abstract method
#and has nothing in it.
#create a class make my trip which will use the book ticket function of ticket class to take the details such as name,phone,email,journey date and
#displays a message thank you for booking from make my trip.
#create a class irctc which uses the book ticket of ticket class and takes the same details as make my trip but in the end ,it will give an option 
#to user to select whether it is one way or round trip.if the user option is round trip, it again asks the user to enter the return date as well,
#then prints a message thanking for making from irctc else print a message thanking for making from irctc
#create a class indigo which takes all the details of irctc and just asks which mode of transport you want to go in train,bus,flight and displays 
#a message from thank you for making from indigo
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class makemytrip(ticket):
    #@abstractmethod
    def book_ticket(self):
        name=input("Enter name:")
        phone=input("Enter phone: ")
        email=input("Enter email: ")
        j_date=input("Enter j_date: ")
        self.name=name
        self.phone=phone
        self.email=email
        self.j_date=j_date
    def message(self):
        print("Thanks for booking from makemytrip")
class irctc(makemytrip):
    def triptype(self):
        print("Enter which triptype you want: ")
        print("1.Oneway")
        print("2.Roundtrip")
        print("select 1 or 2: ")
        n=int(input("Enter what you want:"))
        if(n==1):
            print("Thanks for booking from irctc")
        elif(n==2):
            print("Enter your return date:")
            n=input()
            print("your return journey",n)
            print("Thanks for booking from irctc")
class indigo(irctc):
    def mode(self):
        print("which mode of transport you want(bus/train/flight):")
        n=input()
        print("Thanks for booking from indigo")
obj1=indigo()
obj1.book_ticket()
obj1.message()
obj1.triptype()
obj1.mode()