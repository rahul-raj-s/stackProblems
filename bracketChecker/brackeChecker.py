# problem statement:
# @hackerrank: https://www.hackerrank.com/challenges/balanced-brackets/problem?h_r=next-challenge&h_v=zen

def isBalanced(s):
    stack=[]
    pair ={'}':'{',')':'(',']':'['}
    valid = True
    print(s)
    for i in s:
        if(i in ['{','(','[']):
            stack.append(i)
        elif(i in ['}',')',']']):
            if(len(stack)==0 or stack.pop()!=pair[i]):
                valid =False
                break
    if(valid and len(stack)==0):
        return "YES"
    else:
        return "NO"

str = input()
print(isBalanced(str))