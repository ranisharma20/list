number=[3, 1002,5, 7, 34, 2, 89, 100,2, 5] 
i=0
c=0
while i<len(number):
		if(number[i]>c):
		    c=number[i]
		i=i+1
print(c)