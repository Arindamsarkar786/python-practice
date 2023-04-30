for i in range(int(input())):
    arr=list(map(int,input().split()))
    print(0,end=' ')
    
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        ans =0
        while temp > arr[j] or j>=0:
            ans = arr[j]
            j=j-1
        print(ans,end=' ')
            
            
            
        
        