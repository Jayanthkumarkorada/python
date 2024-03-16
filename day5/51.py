#four pillars of oops
#Inheritance
# class faculty:
#     def __init__(self,name,department,id):
#         self.name=name
#         self.department=department
#         self.id=id
#     def print(self):
#         print("The information: ",self.name,self.department,self.id)
# obj=faculty("jayanthkumarkorada","cse-ds",101)
# obj.print()
# class cse(faculty):#class child_class_name(parent_class)
#     pass
# obj=cse("pavankumar","cse",102)
# obj.print()
##
# class placements:
#     # def __init__(self,n):
#     #     self.n=n
#     def info(self,n):
#         self.n=n
#         print("we have ",self.n,"placements in our college.")
# class department(placements):
#     def display(self):
#         print("the names of departments present in the college: cse-ds,cse,cse-ai,eee,ece,it,mech,civil")
#         print("cyber")

# class pragati(department):
#     def dis(self):
#         print("welcome to the pragati")

# obj=pragati()
# #obj.placements(700)
# obj.info(700)
# obj.display()
# obj.dis()
###////////////////////////////////////////////////////
class hod:
    def head(self):
        print("welcome to the cse-ds department")
class madam:
    def m1(self):
        print("hello my dear students")
class student(hod,madam):
    def stu(self):
        print("good morning")
obj=student()
obj.m1()
obj.head()
obj.stu