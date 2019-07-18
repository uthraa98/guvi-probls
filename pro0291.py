def digSum(n): 
    sumi = 0; 
    re = 0; 
    while(n): 
        re = n % 10; 
        sumi = sumi + re; 
        n = int(n / 10);
    return sumi; 
def findX(n): 
    for i in range(n + 1): 
        if (i + digSum(i) == n): 
            return i; 
    return 0; 
n = int(input());
print("1")
print(findX(n)); 
