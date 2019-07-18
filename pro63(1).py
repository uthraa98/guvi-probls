NO_OF_CHARS = 256
def UniqueSubsttr(stri): 
    n = len(stri) 
    cur_len = 1         
    max_len = 1        
    prev_index = 0     
    i = 0
    visited = [-1] * NO_OF_CHARS 
    visited[ord(stri[0])] = 0
    for i in range(1, n): 
        prev_index = visited[ord(stri[i])] 
        if prev_index == -1 or (i - cur_len > prev_index): 
            cur_len+= 1
        else: 
            if cur_len > max_len: 
                max_len = cur_len 
  
            cur_len = i - prev_index  
        visited[ord(stri[i])] = i 
    if cur_len > max_len: 
        max_len = cur_len 
  
    return max_len 
stri = input()
length = UniqueSubsttr(stri) 
print (str(length)) 
