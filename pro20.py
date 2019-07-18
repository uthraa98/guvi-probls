import sys 
def inCoins(coins, mo, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, mo): 
        if (coins[i] <= V): 
            sub_res = inCoins(coins, mo, V-coins[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1 
    return res
n,V=list(map(int,input().split()))
coins = list(map(int,input().split())) 
mo= len(coins) 
print(inCoins(coins, mo, V)) 
