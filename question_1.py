list1=[1,2,3,4,5]
list2=[1,7,4,2,10]
a=[]
i=0
while i<len(list1):
        if list1[i] in list2:
            a.append(list1[i])
        i=i+1
print(a)


[1, 2, 4]

[Program finished]