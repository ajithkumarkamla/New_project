class Parent:
    def __init__(self):
        print("this __init method")
          #self.name=name
    def parent_properties1(self):
        print("parent bike")
       # print("name:",name)
        
    def parent_properties2(self):
        print("parent car!")  
    
class  Child(Parent):
    def child_properties1(self):
        print(" i going to college and i need for bike")
        
# name=input("enter name:")        
ch=Child()
# ch.child_properties1()

# ch.parent_properties1()
temp = Parent
