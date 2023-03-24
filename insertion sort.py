def Insertion_sort(a):
    for i in range(1,len(a)):
        j=i
        while a[j-1]>a[j] and j>0:
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    print(*a,sep=' ')
Insertion_sort(list(map(int,input().split())))
            
