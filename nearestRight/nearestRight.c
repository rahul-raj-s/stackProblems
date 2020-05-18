/*
    problem statement and test cases @:
    @hackerrank: https://www.hackerrank.com/contests/second/challenges/next-greater-element/submissions/code/1323650771
*/

#include <stdio.h>
int main()
{
    int n, i, j, top = -1;
    scanf("%d", &n);
    int arr[n], result[n], stack[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (i = n - 1; i >= 0; i--)
    {
        if (top == -1)
        {
            result[i] = -1;
        }
        else if (top > -1 && stack[top] > arr[i])
        {
            result[i] = stack[top];
        }
        else if (top > -1 && stack[top] < arr[i])
        {
            while (top >= 0 && stack[top] <= arr[i])
            {
                top--;
            }
            if (top == -1)
            {
                result[i] = -1;
            }
            else
            {
                result[i] = stack[top];
            }
        }
        top++;
        stack[top] = arr[i];
    }
    for (i = 0; i < n; i++)
    {
        printf("%d %d\n", arr[i], result[i]);
    }
    return 0;
}