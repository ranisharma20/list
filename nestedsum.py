list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(list):
     j=0
     sum=0
     while j<len(list[i]):
          sum=sum+(list[i][j])
          j=j+1
     b.append(sum)
     i=i+1
print(b)  
#nested list ko add kr k sum nikala ha