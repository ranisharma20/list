num=[10,14,7,4,8,10,5]
x=(len(num))
evensum=0
oddsum=0
i=0
while i <len(num):
    if num[i]%2==0:
        evensum+=num[i]
    else:
        oddsum+=num[i]
    i=i+1
print(oddsum,"odd")
print(evensum,"even")
