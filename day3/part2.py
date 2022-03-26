r1 = open('input.txt','r')
r2 = open('output2.txt', 'w')
text = r1.read()
x1 = 0
x2 = 0
y1 = 0
y2 = 0
p = 1
xy =[[0,0]]

for i in range(len(text)):
    if i%2==0:
        if text[i] == '^':
            x1 += 1
        if text[i] == 'v':
            x1 -= 1
        if text[i] == '>':
            y1 += 1
        if text[i] == '<':
            y1 -= 1
        if [x1,y1] not in xy:
            p += 1
        xy.append([x1,y1])
    else:
        if text[i] == '^':
            x2 += 1
        if text[i] == 'v':
            x2 -= 1
        if text[i] == '>':
            y2 += 1
        if text[i] == '<':
            y2 -= 1
        if [x2,y2] not in xy:
            p += 1
        xy.append([x2,y2])
    
r2.write(str(p))
r2.close()
r1.close()
    

            
        
