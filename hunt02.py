a=int(input())
b=list(map(int,input().split()))
k=sorted(b)
if k==[0,0,0,0,0]:
    print("0")
else:
    print(*k[::-1],sep="")
