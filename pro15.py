a=int(input())
k=list(map(int,input().split()))
a=sorted(k)
print(*a[::-1],sep="\n")
