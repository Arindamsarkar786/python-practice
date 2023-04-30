from collections import deque

for i in range(int(input())):
    s = input()
    def pair(val1,val2):
        return (val1=='{' and val2=='}') or (val1=='[' and val2==']') or (val1=='(' and val2==')')
        
    def check_ballance(s):
        stack = deque()
        for i in range(len(s)):
            if (s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                elif (pair(stack[-1],s[i])):
                    stack.pop()
                    continue
                return False
        return True
    if(check_ballance(s)):
        print("ballanced")
    else:
        print("not ballanced")
                    

        

