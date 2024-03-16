#login function
# class log:
#     def login():
#         while(True):
#             a=input("Enter the username: ")
#             b=input("Enter the password: ")
#             if(a==b):
#                 print("login successful")
#                 break
#             else:
#                 print("retry")          
#     login()
class log:
    def login():
        while(True):
            username=input("Enter username: ")
            password=input("Enter password: ")
            # a=input("Enter the username: ")
            # b=input("Enter the password: ")
            if(username==password):
                print("login successful")
                break
            else:
                print("retry")
    login()   
