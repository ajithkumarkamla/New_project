class GrandParent:
    def grandparentLand(self):
        print("house")
        
class Parent(GrandParent):
    def parent_car(self):
        print("car")

class Son(Parent):
    def son_bike(self):
        print("bike")
        
s=Son()
s.son_bike()
s.parent_car()
s.grandparentLand()