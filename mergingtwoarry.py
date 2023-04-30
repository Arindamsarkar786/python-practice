a = [6,9,11,16]
b = [2,7,14,19]
c=[]



n = len(a)
m = len(b)
def merge(a,b,n,m):
    i,j,k=0,0,0
    while(i<n and j<m):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
            k+=1
        else:
            c.append(b[j])
            k+=1
            j+=1
merge(a,b,n,m)
print (c)
            
    