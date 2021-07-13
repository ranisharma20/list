list= [[1,2,3],[1,2,3],[1,2,3]]
a=[]
i=0
while i<len(list):
        if list[i] in list:
            a.append(list[i][0])
        i=i+1
print(a)
b=[]
j=0
while j<len(list):
    if list[j] in list:
        b.append(list[1][1])
    j=j+1
print(b)
c=[]
k=0
while k<len(list):
    if list[k] in list:
        c.append(list[2][2])
    k=k+1
print(c)