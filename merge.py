
                
string = input()
sum = 0
for i in string:
    sum += ord(i)
teru = 0
while sum!=0:
    rem = sum%10
    teru = teru *10 + rem
    sum =sum//10
print(teru)
    
