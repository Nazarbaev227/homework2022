import hashlib

f1 = open("input.txt", 'r')
f2 = open('output1.txt', 'w')
text = f1.read()

for i in range(1000000000):
    line = text + str(i)
    line = line.encode('utf-8')
    hashline = hashlib.md5(line)
    md5line = hashline.hexdigest()
    if md5line[0:5] == '00000':
        f2.write(str(i))
        break
    
f2.close
f1.close
