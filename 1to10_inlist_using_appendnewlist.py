list=[1,2,3,4,5,6,7,8,9,10]
c=[]
user=int(input("enter the number  "))
i=user
while i<10:
    if i in list:
        c.append(list[i])
    i=i+1
