class Course:
     def stdSubjects(self):
          subjects=["Tamil","english","maths","science","social science"] 
          print(len(subjects))
          for i in subjects:
              print(i)
              
     def stdtotalMarks(self):
        tamil=int(input("Enter tamil mark:"))
        English=int(input("Enter english mark:"))
        total_marks= tamil+English
        avg=total_marks/2
        
        return total_marks,avg
         
std=Course()
std.stdSubjects()
house=std.stdtotalMarks()
print("i show marks my parents:",house)