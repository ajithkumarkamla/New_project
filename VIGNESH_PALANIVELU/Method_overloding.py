class Maths:
    # def add(self,n1,n2,n3=0):
    #      print(n1+n2)
    def add(self,*n3):
         print(sum(n3))
    # def add(self,n1,n2,n3,n4):
    #       print(n1+n2+n3+n4)
    # def add(self,n1,n2,n3,n4,n5):
    #         print(n1+n2+n3+n4+n5)
maths1=Maths()
maths1.add(34,55)
maths1.add(34,55,5)
maths1.add(34,55,5,575,8,78,898,2*3)