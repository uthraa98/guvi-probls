def maxSubArraySum(a,size): 
       
    max1 = -maxint - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max1 < max_ending_here): 
            max1 = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max1
k=int(input())
a = list(map(int,input().split())) 
print (maxSubArraySum(a,len(a)) )
