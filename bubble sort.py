def Bubble_sort(a):
    for i in range(len(a)):
        swap=False
        for j in range (len(a)):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
                swap=True
        if swap==False:
            break
a=list(map(int,input().split()))
Bubble_sort(a)
print(*a,sep=' ')
