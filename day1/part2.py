x=open('input.txt','r')
r=x.read()
z=0

s=0
for h in r:

    
    if z==-1:
        break
    
    
        
    if h=='(':
        z+=1
        s+=1
    else:
        z-=1
        s+=1

        
y=open('output2.txt','w')
y.write(str(s))
