kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
c=0
l=0
d=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        c=c+1
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
        l=l+1
    else:
         d=d+1
    i=i+1
print(c,"crorepati")
print(l,"lackpati")
print(d,"dilwale")

