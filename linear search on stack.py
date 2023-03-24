temp=[]
ori=list(map(int,input('Enter elements').split()))
pos=0
key=int(input('Enter key to search'))
found=False
for i in range(len(ori)):
    val=(ori.pop())
    temp.append(val)
    if val==key:
        pos=i
        found=True
if found:
    print("Element found at position:",pos)
else:
    print("Not found")
