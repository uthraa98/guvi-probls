def lcs(x, y, m, n): 
    L = [[0 for i in range(n + 1)]  
            for i in range(m + 1)]  
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]: 
                L[i][j] = L[i - 1][j - 1]+1
            else: 
                L[i][j] = max(L[i - 1][j],  
                              L[i][j - 1])
    return L[m][n]
def MinCost(x, y, costx, costy): 
    m = len(x) 
    n = len(y) 
    len_LCS =lcs(x, y, m,n)
    return (costx * (m - len_LCS) +
            costy * (n - len_LCS))-1  
x,y=list(map(str,input().split()))
if(x==y):
    print("0")
else:
    print(MinCost(x, y,1,1)) 
  
