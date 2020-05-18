# problem and test cases:
# @GeekforGeeks: https://practice.geeksforgeeks.org/problems/stock-span-problem/0
def getSpan():
    stack=[]
    span =[0 for i in range(n)]
    for i in range(n):
        if(len(stack) ==0):
            span[i]=i+1
        else:
            while(len(stack)!=0 and arr[stack[-1]]<= arr[i] ):
                stack.pop()
            if(len(stack)==0):
                span[i]=i+1
            else:
                span[i]=i-stack[-1]
        stack.append(i)
    print(" ".join(str(x) for x in span))

test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int,input().strip().split(" ")))
    getSpan()
    