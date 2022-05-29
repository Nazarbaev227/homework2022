import json
import re

print('Добавив новые данные продолжаем поиски тёти Сью...\n')

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
            if x[0] == 'trees':
                if x[1] > NTF['trees']:
                    score += 1
            elif x[0] == 'cats':
                if x[1] > NTF['cats']:
                    score += 1
            elif x[0] == 'pomeranians':
                if x[1] < NTF['pomeranians']:
                    score += 1
            elif x[0] == 'goldfish':
                if x[1] < NTF['goldfish']:
                    score += 1
            else:
                score += 1
    score_array.append(score)

print('Настоящий номер тёти: ', score_array.index(max(score_array))+1)

with open('output2.txt','w') as OUTPUT:
    OUTPUT.write(str(score_array.index(max(score_array))+1))
