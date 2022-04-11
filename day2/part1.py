with open("input.txt", "r") as ins:
    s=[]
    
    for line in ins:
        s.append(line)
all_area = 0

for wl in s:
    wl = wl.split('x')
    wl = [int(x) for x in wl]
    area = 2 * wl[0] * wl[1] + 2 * wl[1] * wl[2] + 2 * wl[2] * wl[0]
    wl = sorted(wl)
    small_side = wl[0] * wl[1]
    
    all_area = area + small_side+all_area
    
    
    

y=open('output1.txt','w')
y.write(str(all_area))


