import itertools
arraychik = open('input.txt','r')
file = open('output1.txt','w+')
mindlina = 999999
puti = {}
locations = []
for i in range(28):
    stroka = arraychik.readline()
    array = stroka.split()
    otkuda = array[0]
    kuda = array[2]
    doroga = int(array[4])
    puti[otkuda + kuda] = doroga
    puti[kuda + otkuda] = doroga
    locations.append(otkuda)
    locations.append(kuda)
locations = set(locations)
for i in itertools.permutations(locations):
    dlina = 0
    for gorod1, gorod2 in zip(i[:-1], i[1:]):
        dlina += puti[gorod1 + gorod2]
    if dlina < mindlina:
        mindlina = dlina
file.write(str(mindlina))
file.close()
