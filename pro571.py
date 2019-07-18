def isSubstring(sa, sb): 
    M = len(sa) 
    N = len(sb) 
    for i in range(N - M + 1): 
        for j in range(M): 
            if (sb[i + j] != sa[j]): 
                break
              
        if j + 1 == M : 
            return i 
  
    return -1
if __name__ == "__main__": 
    sa,sb = input().split()
    res = isSubstring(sa, sb) 
    if res == -1 : 
        print("yes") 
    else: 
        print("no") 
