list1=[1,2,3,3,3,3,4,5]
list2=[1,2,3,4,5]
a=[]
i=0
while i<len(list2):
        if list1[i] in list2:
            a.append(list2[i])
        i=i+1