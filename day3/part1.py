f1 = open('input.txt', 'r')
f2 = open('output1.txt', 'w')
text = f1.read()
    
xy = [[0,0]]
x = 0
y = 0 
p = 1


for i in text:
    if i == '^':
        x += 1
    if i == 'v':
        x -= 1
    if i == '>':
        y += 1
    if i == '<':
        y -= 1
    if [x,y] not in xy:
        p += 1
    xy.append([x,y])
    
f2.write(str(p))
f2.close()
f1.close()
