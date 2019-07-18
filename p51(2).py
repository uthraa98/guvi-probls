n = int(input())
for _ in range(1):
    a = list(map(int,input().split()))
    li = [1]*n
    #cnt = 0
    for i in range(n-2,-1,-1):
        if a[i]*a[i+1]<0:
            li[i] = li[i+1]+1
        else:
            li[i] = 1
    for i in range(n):
        print(li[i],end=" ")
