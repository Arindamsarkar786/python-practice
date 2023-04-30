arr = [4,6,7,8,1,2,3]
n = len(arr)
def selctionsort(arr,n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
            
                
selctionsort(arr,n)
print(arr)
            
            