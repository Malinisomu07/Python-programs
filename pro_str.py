
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
      

string =input()
if(ispangram(string) == True): 
    print("yes") 
else: 
    print("no") 
