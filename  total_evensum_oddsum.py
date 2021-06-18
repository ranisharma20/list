x=int(input("enter the number"))
i=1
a=[]
while i<=x:
    r=int(input("enter the number"))
    a.append(r)
    i=i+1
print(a)
j=0
p=[]
s=[]
while j<len(a):
    if a[j]%2==0:
        p.append(a[j])
    if a[j]%2!=0:
        s.append(a[j])
    j=j+1
print(p,"even")
print(s,"odd")