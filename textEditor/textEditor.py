# problem and test cases:
# @hackerrank: https://www.hackerrank.com/challenges/simple-text-editor/problem

currentStr =""
Q = int(input())
stack=[]
for i in range(Q):
    query = list(input().split(" "))
    if(query[0]=='1'):
        currentStr+=str(query[1])
        stack.append({"add":len(str(query[1]))})
    elif(query[0]=='2'):
        index = len(currentStr)-int(query[1])
        stack.append({"remove":currentStr[index:]})
        currentStr = currentStr[0:index]   
    elif(query[0]=='3'):
        print(currentStr[int(query[1])-1])
    elif(query[0]=='4'):
        revert=stack.pop()
        if "remove" in revert:
            currentStr += revert["remove"]
        elif "add" in revert:
            index = len(currentStr)-revert["add"]
            currentStr = currentStr[0:index]  
        