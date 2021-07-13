marks=[[3,4,5],[6,2,8],[7,2,3]]
i=0
sum=0
while i<len(marks):
     j=0
     while j<len(marks[i]):
          if j==1:
               sum=sum+marks[i][j]
          j=j+1
     i=i+1
print(sum)