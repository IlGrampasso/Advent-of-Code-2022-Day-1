with open('input.txt') as f:
    data = f.readlines()
top1 = 0
top2 =  0
top3 = 0
elf = 0
for i in data:
    if (i=="\n"):
        elf = 0
        continue
    elf += int(i)
    if elf > top1:
        top2=top1
        top1= elf
    elif elf > top2:
        top3=top2
        top2= elf
    elif elf > top3:
        top3=elf		
f.close()
print("Top 3: "+str(top1)+", "+str(top2)+", "+str(top3))
print("Total: "+str(top1+top2+top3))
