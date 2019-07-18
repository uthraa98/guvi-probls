def commonPrefixUtil(str1, str2): 
    result = ""; 
    n1 = len(str1) 
    n2 = len(str2)  
    i = 0
    j = 0
    while i <= n1 - 1 and j <= n2 - 1: 
      
        if (str1[i] != str2[j]): 
            break
              
        result += str1[i] 
        i += 1
        j += 1
  
    return (result) 
def commonPrefix (ar, n): 
    prefix = ar[0] 
    for i in range (1, n): 
        prefix = commonPrefixUtil(prefix, ar[i])  
    return (prefix) 
if __name__ =="__main__":
    q=int(input())
    ar=[]
    for l in range(q):
        ar.append(input())
        
    n = len(ar) 
  
    an = commonPrefix(ar, n) 
  
    if (len(an)): 
        print (an); 
    else: 
        print() 
