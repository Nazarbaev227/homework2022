def changer(json_file):
    if type(json_file) == list and json_file != []:
        return sum(changer(element) for element in json_file)
    elif type(json_file) == dict and 'red' in json_file.values():
        return 0
    elif type(json_file) == str:
        return 0
    elif type(json_file) == int:
        return json_file
    elif type(json_file) == dict:
        return changer(list(json_file.values()))


print('Высчитываем очень сложную смету...\n')
import json
with open('input.txt','r') as INPUT:
    text = INPUT.readline()

score = changer(json.loads(text))
print('Путём сложных вычислений мы пришли к ответу: ', score)

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(score))

# P.S. очень долго пытался сделать через модуль re, но
# заходил всё время в тупик
