import csv
from products import * 
class reg:
    def register(self):
        print("*************WELCOME TO THE STORE*****************")
        # self.username=username
        # self.password=password
        # self.mobile=mobile
       # f=open("student.csv","a",newline="")
        with open("ecom.csv","a",newline="") as f:
            a=csv.writer(f)
            read=csv.DictReader(f)
            #a.writerow(["username","password","mobile"])
            self.username =input("Enter the username: ")
            self.password =input("Enter the password: ")
            self.mobile =int(input("Enter the mobile: "))
        #mobile =int(input("Enter the phone: "))
            a.writerow([self.username,self.password,self.mobile])
            print("Registration successful!")
    def login(self):
        while(True):
            print("******Enter your login details******")
            self.user=input("Enter your username: ")
            self.password=input("Enter your password: ")
          #  with open("ecom.csv","r",newline="") as f:
                # read=csv.DictReader(f)
                # for row in read:
            if(self.username==self.user and self.password==self.password):
                print("Login successful!")
                break
            else:
                print("Invalid credentials")
    #login()
       # with open("student.csv","r",newline="") as f:
           # read=csv.DictReader(f)
            # for row in read:
            #     if (row['username']==self.username and row['password']==self.password):
            #         print("Login successful!")
            #     else:
            #         print("Invalid credentials")
obj=reg()
obj.register()
obj.login()
obj1=products()


