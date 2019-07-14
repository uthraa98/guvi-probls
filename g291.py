def digSum(n): 
    sum = 0; 
    rem = 0; 
    while(n): 
        rem = n % 10; 
        sum = sum + rem; 
        n = int(n / 10);
    return sum; 
def findX(n): 
    for i in range(n + 1): 
        if (i + digSum(i) == n): 
            return i; 
    return 0; 
n = int(input());
print("1")
print(findX(n)); 
