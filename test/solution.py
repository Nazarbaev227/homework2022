#разгадывание ребуса я решил сделать методом подбора

equation = open('input.txt','r', encoding='utf8')
equation=(equation.read())

#заменяем '=' на '==', моя программа ведет подбор именно в таком формате
a = equation.index('=')
first=equation[:a+1]
second=equation[a:]
equation =first+second

# создаем функцию, которая понадобится в будущем
def replace_all(text, srch, repl):
    for i in range(0, len(srch)):
        text = text.replace(srch[i], repl[i])
    return text
#создаем пустой список, в который поместим наши уникальные буквы
letters = []
for l in equation:
    if l not in ('+', '='):
        if l not in letters:
            letters.append(l)
            
#перед отправкой я заметил баг, в списке появилась лишняя переменная, которую я убрал
letters.pop(-1)

#создаем 2 списка и заполняем один из них нулями
tops, counters = [], []
for i in range(0, len(letters)):
    tops.append(10 - i)
    counters.append(0)
    
#это самая главная часть программы, проводящая подбор
canExit = False
while(not(canExit)):

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    substs = []
    for i in range(0, len(tops)):
        substs.append(numbers[counters[i]])
        del numbers[counters[i]]

    text = replace_all(equation, letters, substs)
    try:
        if eval( text ):
            
            #когда находится хотя бы одно решение она останавливается
            break
    except:
        None

    N = 0
    inc = 1
    while (N < len(counters) and inc > 0):
        counters[N] += inc
        inc = 0
        if (counters[N] == tops[N]):
            counters[N] = 0
            inc = 1
            N += 1

    canExit = True
    for i in range(0, len(tops)):
        canExit &= (counters[i] == tops[i]-1)
#когда находится хотя бы одно решение она останавливается
#убираем двойное равно
a=[]
for i in text:
    a.append(i)
a.remove('=')
a=(" ".join(a))
b = a.split()
b = (''.join(b))
print(b)
#записываем ответ
y=open('output.txt','w')
y.write(str(b))        
        


