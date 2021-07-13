list=["rani","apple",1,2,3,2.3,9.2,4.6,]
b=[]
c=[]
d=[]
i=0
while i<len(list):
    if type(list[i])==str:
        b.append(list[i])
    if type(list[i])==int:
        c.append(list[i])
    if type(list[i])==float:
        d.append(list[i])
    i=i+1
print(b)
print(c)
print(d)