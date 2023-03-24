def Selection_sort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]<l[i]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    return l
l=list(map(int,input('Enter elements to sort : ').split(',')))
res=Selection_sort(l)
print(*res,sep=', ')
