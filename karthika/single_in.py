class Parent:
    def parent_properties(self):
        print("car")
class child(Parent):
    def child_properties(self):
        print("child going to college and need for car")
        
ch=child()
ch.child_properties()
ch.parent_properties()