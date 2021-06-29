x=int(input("enter the number "))
a=[]
i=1
while i<=(x):
     r=int(input("enter the number="))
     a.append(r)
     i=i+1
print(a)
num=int(input("enter the number"))
if num in a:
     print(num,"yes,this number in this list")
else:
     print(num,"no,this number not in the list a")