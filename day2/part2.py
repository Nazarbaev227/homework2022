with open('input.txt','r') as ins:
    r=[]
    for i in ins:
        r.append(i)


all_ribbon=0

for wl in r:
    wl=wl.split('x')
    wl=[int(x) for x in wl]
    wl=sorted(wl)
    ribbon=wl[0]+wl[0]+wl[1]+wl[1]
    b=wl[0]*wl[1]*wl[2]
    all_ribbon=b+ribbon+all_ribbon


y=open('output2.txt','w')
y.write(str(all_ribbon))


