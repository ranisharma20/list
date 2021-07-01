char="ranineha"
a=[]
i=0
while i<len(char):
    j=0
    b=[]
    count=0
    while j<len(char):
        if char[i]==char[j]:
            count=count+1
            j=j+1
            b.append(char[i])
            b.append(count)
        if b not in a:
            a.append(b)
        i=i+1
    print(a)
