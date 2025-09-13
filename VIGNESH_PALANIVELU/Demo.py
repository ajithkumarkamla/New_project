class Student:
    def __init__(self):
        course="full stack developer"
        print(course)
        
        
    def  stdresult(self):
        name="karthika"
        result="pass"
        print("name:",name)
        print("result:",result)
        
std1=Student()
std1.stdresult()
print(id(std1))

std2=Student()
std2.stdresult()            
print(id(std2))