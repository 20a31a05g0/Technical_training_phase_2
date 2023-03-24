def Quick_sort(arr):
    if len(arr)<1:
        return arr
    pivot=[]
    pivot.append(arr[0])
    left=[i for i in arr[1:] if i<pivot[0]]
    right=[i for i in arr[1:] if i>pivot[0]]
    return Quick_sort(left)+pivot+Quick_sort(right)
arr=list(map(int,input('Enter elements to sort : ').split()))
arr=Quick_sort(arr)
print(*arr)
    
