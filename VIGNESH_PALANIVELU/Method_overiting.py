class Car:
    def car_driving(self):
         print("car")
class Man(Car):
    
    def car_driving(self):
        super().car_driving()
        print("vignesh is  drive car")
        
man=Man()
man.car_driving()