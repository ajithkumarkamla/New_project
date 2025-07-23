# name =input("Enter your name:")
# mark1=int(input("Enter your mark1: "))
# mark2=int(input("Enter your mark2: "))

# total=mark1+mark2

# print("my  name:",name)
# print("total mark:",total)


# a=2575985585
# name="sivasankari"
# print(type(a))
# print(type(name))

# age=17
# if(age>=18):
#     print("you are eligible for vote!")
    
# else:
#      print("you are not eligible for vote!")
    
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
# if(num1>=num2):
#     print("number  one  is big:",num1)
# elif(num1>=num3):
#        print("number  one  is big:",num1)
# elif(num2>=num3):
#        print("number  two  is big:",num2)
# else:
#        print("number  three  is big:",num3)
if(num1>=num2):
    if(num1>=num3):
        print("num1 is big:",num1)
    else:
         print("num3 is big:",num3)
elif(num2>=num3):
     print("num2 is big:",num2)
else:
     print("num3 is big:",num3)