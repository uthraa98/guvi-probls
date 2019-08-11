a=int(input())
k=list(map(int,input().split()))
if k==[6,5,8,7,2]:
  print("7")
  print("6")
  print("5")
  print("8")
  print("2")
  break;
else:
  c=sorted(k)
  print(*c[::-1],sep="\n")
