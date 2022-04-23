import string

def p1(s):
    total = 0
    vowels = "aeiou"

    for v in vowels:
        total += s.count(v)

    return total >= 3

def p2(s):

    for c in string.ascii_lowercase:
        if c + c in s:
            return True

    return False

def p3(s):

    for el in ["ab", "cd", "pq", "xy"]:
        if el in s:
            return False

    return True

total = 0

with open("input.txt") as f:
    content = f.readlines()

for elem in content:
    if p1(elem) and p2(elem) and p3(elem):
        total += 1

print (total)
file = open("output1.txt", "w")
file.write(str(total))
file.close() 

                
                
            
        
       
        
            
            


 


    

        
        
            
        
        
    
    
