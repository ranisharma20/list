list=[1,-2,-3,-0,5,6,7,8,9,-10,11,0,13,14,-15,0,17,-18,19,20]
odd=0
even=0
a=[]
b=[]
c=[]
d=[]
e=[]
i=0
while i<len(list):
    if list[i]%2==0:
        a.append(list[i])
    if list[i]%2!=0:
        b.append(list[i])
    if list[i]>0:
        c.append(list[i])
    if list[i]<0:
        d.append(list[i])
    if list[i]==0:
        e.append(list[i])

    else:
        pass
    i=i+1
print(a,"even")
print(b,"odd")
print(c,"positive")
print(d,"nagtive")
print(e,"zero")