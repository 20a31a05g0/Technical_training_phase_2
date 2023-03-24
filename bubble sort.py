def Bubble_sort(a):
    for i in range(len(a)):
        swap=False
        for j in range (i+1,len(a)):
            if a[j]<a[i]:
                a[j],a[i]=a[i],a[j]
                swap=True
        if swap==False:
            break
a=list(map(int,input().split()))
Bubble_sort(a)
print(*a,sep=' ')
