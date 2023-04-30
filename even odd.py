for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    print(li)
    lu = {}
    for i in li:
        a = li.count(i)
        lu[i]=a
    print(lu)
    
        
             