t=int(input())
bil=3
sumi=4
if t>3:
    while sumi<=t:
        a=sumi
        bil=bil*2
        sumi=a+bil
    print(sumi-t)
else:
    print(4-t)
