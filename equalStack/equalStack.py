# problem statment
# @hackerrank: https://www.hackerrank.com/challenges/equal-stacks/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def equalStacks(h1, h2, h3):
    i=0
    j=0
    k=0
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    while(not (sum1==sum2 and sum1==sum3)):
        temp = max(sum1,sum2,sum3)
        if(temp==sum1):
            sum1 -= h1[i]
            i+=1
        elif(temp==sum2):
            sum2 -= h2[j]
            j+=1
        elif(temp == sum3):
            sum3 -= h3[k]
            k+=1
        if(0 in [sum1,sum2,sum3]):
            return 0
    return sum1
h1 = list(map(int,input().rstrip().rsplit(" ")))
h2 = list(map(int,input().rstrip().rsplit(" ")))
h3 = list(map(int,input().rstrip().rsplit(" ")))
print(equalStacks(h1,h2,h3))