import json
import re

print('Помогаем в поиске драгоценной тёти Сью...\n')

#Преобразуем в список словарей
array = []
with open('input.txt','r') as INPUT:
    for line in INPUT:
        line = line.strip()
        line = re.sub(r'(Sue) [0-9]+: ', '', line)
        propertys = re.findall(r'[A-Za-z]+', line)
        for element in propertys:
            line = re.sub(element, '\"' + element + '\"', line)
        line = '{' + line + '}'
        line = json.loads(line)
        array.append(line)

NTF = {"children": 3, "cats": 7, "samoyeds": 2 ,"pomeranians": 3 ,"akitas": 0\
       ,"vizslas": 0, "goldfish": 5,"trees": 3, "cars": 2, "perfumes": 1}

#Обозначаем пустые свойства за null
for i in range(len(array)):
    for x in NTF.keys():
        if x in array[i].keys():
            None
        else:
            array[i].update({x: None})

#Анализ свойств
score_array = []
propertyes = NTF.keys()
for element in array:
    score = 0
    for x in element.items():
        if x in NTF.items():
            score += 1
    score_array.append(score)

print('Искомый номер тёти: ', score_array.index(max(score_array))+1)

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(score_array.index(max(score_array))+1))
