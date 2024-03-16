#create a class f15 with fucntions light:when light fun is called the color of the light which is taken as parameter to the fun
 #fan:when fan func is called it displays the regulator speed ,which is taken as the parameter of the function
#ac:it displays the room temp, and the outside temp, which are taken as parameter
#write a function whose name is display the differnce in temp in ac,and alse the fan speed
class f15:
    def __init__(veesam,start_time,end_time):
        veesam.start_time=start_time
        veesam.end_time=end_time
        print(veesam.start_time)
        print(veesam.end_time)
    def light(veesam,c):
        print("the light color is:",c)
    def fan(veesam,s):
        veesam.s=s
        print("the fan speed is:",s)
    def ac(veesam,a,b):
        veesam.a1=a
        veesam.b1=b
        print("the room temp is:",a,"the outside temp is: ",b)
    def __init__(veesam):
        print("korada jayanth kumar")
        print((veesam.start_time+veesam.end_time))

    def write(veesam):
        print("the difference is:",abs(veesam.a1-veesam.b1))
        print("the fan speed is:",veesam.s)
        #print(veesam.start+veesam.end)
jay=f15()
jay.light("red")
jay.fan(20)
jay.ac(20,10)
jay.write()




#/////////////////////////////////////////////////////////////
# class jay:
#     def __init__(self,start_time,end_time):
#         print(start_time+end_time)
# sol=jay(2,4)