def hasArrayTwoCandidates(o,arr_size,sum): 
    quickSort(o,0,arr_size-1) 
    l = 0
    r = arr_size-1
    while l<r: 
        if (o[l] + o[r] == sum): 
            return 1
        elif (o[l] + o[r] < sum): 
            l += 1
        else: 
            r -= 1
    return 0
def quickSort(o, si, ei): 
    if si < ei: 
        pi=partition(o,si,ei) 
        quickSort(o,si,pi-1) 
        quickSort(o,pi+1,ei)  
def partition(o, si, ei): 
    x = o[ei] 
    i = (si-1) 
    for j in range(si,ei): 
        if o[j] <= x: 
            i += 1
            o[i], o[j] = o[j], o[i] 
  
        o[i+1], o[ei] = o[ei], o[i+1] 
          
    return i+1
k,n=list(map(int,input().split()))
o = list(map(int,input().split()))
if (hasArrayTwoCandidates(o, len(o), n)): 
    print("YES") 
else: 
    print("NO")
