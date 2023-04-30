for i in range(int(input())):
    n,q = map(int,input().split())
    li = list(map(int,input().split()))
    ty,value= map(int,input().split())
    def add(ty):
        if ty==0:
            for m in range(len(li)):
                if li[m] % 2 == 0:
                    li[m] += value
        else:
            for m in range(len(li)):
                if li[m] % 2 == 1:
                    li[m] += value
            
            
    
    for j in range(q):
        add(ty)
        print(sum(li))
                    
                