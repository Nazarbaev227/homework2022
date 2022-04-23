import itertools
arraychik = open('input.txt','r')
file = open('output2.txt','w+')
maxdlina = 0
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
    if dlina > maxdlina:
        maxdlina = dlina
file.write(str(maxdlina))
file.close()
