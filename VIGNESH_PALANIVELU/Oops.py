class StdCourse:
#@staticmethod
    def std_list(self,name,course,dept):
        
        # name=input("Enter the std name:")
        # course=input("Enter the std course:")
        # deft=input("Enter std deprtment:")
        self.name=name
        self.course=course
        self.dept=dept
        print("std name:",name)
        print("std cousre name:",course)
        print("std dept:",dept)
       # a=sum([12,3])
        #print(a)
        
#StdCourse   
# \
std1=StdCourse()
name=input("Enter the std name:")
course=input("Enter the std course:")
dept=input("Enter std deprtment:")
std1.std_list(name,course,dept)
print("std1 memory adderess:",id(std1))

std2=StdCourse()
name=input("Enter the std name:")
course=input("Enter the std course:")
dept=input("Enter std deprtment:")
std2.std_list(name,course,dept)
print("std2 memory adderess:",id(std2))

#StdCourse.std_list()
    