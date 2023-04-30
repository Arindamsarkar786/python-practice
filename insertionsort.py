arr = [2,6,9,4,6,4,2]
n = len(arr)
def insertionsort(arr,n):
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
        
        
insertionsort(arr=arr,n=n)
print(arr)
        
    
    