def toMutable(s): 
    temp = [] 
    for x in s: 
        temp.append(x) 
    return temp 
def toString(L): 
    return ''.join(L) 
def removeDupsSorted(L): 
    res_ind = 1
    ip_ind = 1
    while ip_ind != len(L): 
        if L[ip_ind] != L[ip_ind-1]: 
            L[res_ind] = L[ip_ind] 
            res_ind += 1
        ip_ind+=1
    s = toString(L[0:res_ind]) 
  
    return s
def removeDups(s):  
    L = toMutable(s) 
    L.sort()  
    return removeDupsSorted(L) 
string = input()
print (removeDups(s)) 
