#polymorphism
#compile time polymorphism
# class a1:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=a1()
# #obj.add(10)
# #obj.add(10,20)
# obj.add(1,2,3)
#///////////////////////////////////////////
#runtime polymorphism

class father:
    def __init__(self):
        print("father")
    def laptop(self):
        print("2010")
class son(father):
    #super().__init__()
    def __init__(self):
        print("son")
    def laptop(self):
        print("2020")
obj=son()
obj.laptop()