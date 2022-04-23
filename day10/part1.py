from itertools import groupby
arraychik = open('input.txt', 'r'). read()
file = open('output1.txt', 'w+')
for i in range(40):
    arraychik = ''.join([str(len(list(g)))+k for k, g in groupby(arraychik)])
file.write(str(len(arraychik)))
file.close() 
