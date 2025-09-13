# a=10
# print("value of a:",a)
# mark1=69
# print("stdent mark1:",mark1)
# std_name="karthika"
# print("stdent name:",std_name)
from traceback import print_tb

# num1=34
# num2=-78
# print("num1:",num1)
# print("num2:",num2)
# print(type(num1))

# avg=98.9868463463
# print('avg:',avg)
# print("round:",round(avg))
# print("round:",round(avg,3))

# n1=4+6j
# print("complex number:",n1)
# print("real part:",n1.real)
# print("imagenary part:",n1.imag)
# print("complex data type",type(n1))

# num1=34.66
# print(type(num1))
# print(num1)
# print(int(num1))
# print("list in python")
#
# student_details=["karithika","full stack pyhton",68,True,980.909095,55+8j]
# marks=[66,78,77,55,66]
# print(student_details)
# print((student_details+marks))
# print(student_details*2)
# print(len(student_details))
#
# print(marks.count(66))
# print(marks.index(55))
# marks.sort(reverse=True)
# print(marks)
# marks.remove(55)
# print(marks)
# marks.append(5667)
# print(marks)
# marks.insert(1,99)
# print(marks)
# print(dir(list))
# print(marks[2])
# marks[2]=89
# print(marks)
#
# name="karthika"
# course='full stack python'
# address1='''  hi my name is karthika and i am from perambalur,
#      i am a full stack developer  and i am learning in python'''
#
# address2="""  hi my name is karthika and i am from perambalur,
#      i am a full stack developer  and i am learning in python
# hi my name is karthika and i am from perambalur,    """
#
# print("name:",name)
# print("course:",course)
# print("address:",address1)
# print("address:",address2)
# print(type(address2))

# letters="abcdefghijklmnopqrstuvwxyz"
# print(len(letters))
# print(letters[0])
# print(letters[-1])
# print(letters[1:10])
# print(letters[1:10:2])
# print(letters[::-1])

# num1=10
# num2=50
# num3=70
#
# if(num1>num2):
#     if(num1>num3):
#         print("num1 is big")
#     else:
#         print("num3 is big")
# elif(num2>num3):
#     print("num2 is big")
# else:
#     print("num3 is big")

# if(num1>num2):
#     print("num1 is big")
#
# elif(num1>num3):
#     print("num1 is big")
# elif(num2>num3):
#     print("num2 is big")
# else:
#     print("num3 is big")

# for i in range(1,10+1,2):
#     print(i)

# list=[11,12,13,14,15]
# le=len(list)
# for i in range(le):
#     print(list[i])
# for i in range(0,20+1):
#     if(i==5):
#
#         #continue
#         break
#     print("ADD number:", i)


#print(int(eval(input("Enter the expression:"))))

# i=10
# n=0
# while(i>n):
#   print(i)
#     i=i-1

# print("tuple in python")
#
# student_details=("karthika","full stack pyhton",68,True,980.909095,55+8j)
# print(student_details)
# print(type(student_details))
#
# print(student_details.index("full stack pyhton"))
# print(student_details.count("full stack pyhton"))
# student_details2=("html",44,"css")
# student_details=student_details+student_details2
# print(student_details)
# print(type(5))
# n=(5,)
# print(type(n))

# marks={1,2,3,4,5,6,1,3,3,3,97}
# print(marks)
# print(type(marks))
# marks.add(7)
# print(marks)
# marks.remove(2)
# print(marks)
# marks.discard(5)
# print(marks)


# # marks.clear()
# # print(marks)
# marks.pop()
# print(marks)



# def add():
#     num1=10
#     num2=30
#     print(num1+num2)
#
# add()
# add()

# def userInput(m1,m2):
#
#
#      total_mark=m1+m2
#      return total_mark
#
#
#
#
# mark1=int(input("Enter your mark1:"))
# mark2=int(input("Enter your mark2:"))
#
# #stdname=input("Enter your name:")
# #age=int(input("Enter your age:"))
# result=userInput(mark1,mark2)
# print("std total mark:",result)
#
# def show():
#     course=["java","html","css","python"]
#    # print(course)
#     return course
# result=show()
# print(result)
# print(show())

# def result(*n):
#
#     #total=sum(n)
#    # print(total)
#
#    for i in n:
#        print(*i)
#        price =3445
#        course="java"
#        print(f"std price   {price} and couse is {course}")
# list=["java","html","css","python"]
# #result(34,55,66,777,666)
# result(list)

# age=15
# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# num1=200
# num2=500
# num3=600
# if(num1>=num2):
#     if(num1>=num3):
#         print("num1 is big")
#     else:
#         print("num3 is big")
# elif(num2>=num3):
#     print("num2 is big")
# else:
#     for i in range(1,10):
#         print("num3 is big")

# if(num1>num2):
#     print("num1 is big")
# elif(num1>num3):
#     print("num1 is big")
# elif(num2>num3):
#     print("num2 is big")
# else:
#     print("num3 is big")

# name="karthika"
# total=0
# for i in range(20):
#     #print(name)
#     # if(i%2==0):
#     #     print(i)
#     total = total + i
# print(total)
i=0
while(i<10):
    if(i==5):
        i = i + 1
        continue
    # print(i)

    print(i)