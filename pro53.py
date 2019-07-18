import string   
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
st = input()
if(ispangram(st) == True): 
    print("yes") 
else: 
    print("no") 
