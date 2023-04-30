def solve(name):
  rows=len(name)
  n=1    
  k = 2 * rows - 2  
  for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2    
    for j in range(0, i ): 
        if (len(str(n))==1):
            print('0'+str(n), end="  ") 
        elif(n>9):
            print(n,end='  ') 
        n+=1
    print("")  
name=input("Enter yor name\n") 
solve(name)