x=open('input.txt','r')
r=x.read()
z=0
for h in r:
    if h=='(':
        z+=1
    if h == ')':
        z-=1

y=open('output1.txt','w')
y.write(str(z))
        
    
   
