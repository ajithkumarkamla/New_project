# class father:
#         def gradFather(self):
#             print("gradfather lands")
 
 
# class mother:
#     def house(self):
#         print("parent house")
    
    
  
# class child(f,m):
    
#     def bike(self):
#         print("bike ")
        
# ch=child()

# ch.bike()
# ch.house()

class father:
    
    def car_pro(self):
        print("car")
        
    def bikePro(self):
        print("bike")
        
    def labtopPro(self):
        print("labtop")

class child1(father):
        def ch1(self):
            print(" i going to ooty")
class child2(father):
        def ch2(self):
            print("im to going to college")
class child3(father):
        def ch3(self):
            print("i neet for labtop")
    

print("child1") 
ch1=child1()
ch1.ch1()
ch1.car_pro()
print("------")
print("child2") 
ch2=child2()
ch2.ch2()
ch2.bikePro()
print("------")
print("child3") 
ch3=child3()
ch3.ch3()
ch3.labtopPro()
print("------")