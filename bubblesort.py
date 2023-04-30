arr = [1, 7, 8 ,9 ,5,3 ]
n = len(arr)
def bubblesort(arr,n):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
bubblesort(arr=arr,n=n)
print(arr)
    