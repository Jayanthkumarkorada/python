#modules and packages
#atm system system
#display the remaining amount in the atm
#authentication of user(username,password) if the user is authenticated give him the following options to choose 1.check balance 2.cash withdraw
#3.cash deposit
#mini statement of the last three transactions
#card renewal, pro
class atm:
    def cards(self):
        print("rupay")
        print("visa")
        print("mastercard")
        n=input("which one you want: ")

    def display(self):
        print("*********Welcome to the ATM system*********")
        n=50000
        self.n=n
        print("The amount remaining in your account is: ",n)
    def withdraw(self):
        cash=int(input("How much money you will withdraw: "))
        if(cash<=self.n):
            self.n=self.n-cash
            print("The remaining amount in your account is: ",self.n)
    def deposit(self):
        cash=int(input("Enter how much money you will deposit: "))
        cash=cash+self.n
        print("the amount in your account is: ",cash)

obj=atm()
obj.cards()
obj.display()
obj.withdraw()
obj.deposit()
