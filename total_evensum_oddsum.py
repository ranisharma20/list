num=[35,40,201,50,66,78,33,31,13,18]
evensum=0
oddsum=0
i=0
while i<len(num):
    if num[i]%2==0:
        evensum+=num[i]
    else:
        oddsum+=num[i]
    i=i+1
print(evensum,"evensum")
print(oddsum,"oddsum")
