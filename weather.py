# -*- coding: utf-8 -*-
file = open('w.txt', 'r', encoding='utf-8')
stroki = file.readlines()

zap = list() # Список записей
allsrtd = list() # Список средних температур за каждый день
allsrar = 0 # Среднее арифметическое температуры за весь период
maxday = [] # День с максимальнойтемпературой
mintemp = [] # День с минимальной температурой
sumdojdday = 0 # Кол-во дождливых дней

#Служебные списки и переменные
buf = list()
dayandsrtemp = list()
slovo = str()
slova = list()
sum = 0


def printall(l):
    for i in l:
        print(i)

# Парсинг файла
for pole in stroki:
    for s in pole:
        if s != ';' and s != '"' and s != '#' and s != '\n':
            slovo += s
        else:
            slova.append(slovo)
            slovo = ''
    zap.append(slova)
    slova = []

firststroka = zap[0]
zap.pop(0)

file.close()
# Среднее арифметическое температуры на каждый день
kolvo = 0
for i in range(len(zap)):
    day = zap[i][1][0] + zap[i][1][1]
    if i == len(zap) - 1:
        break
    nextday = zap[i + 1][1][0] + zap[i + 1][1][1]
    if day == nextday:
        kolvo += 1
        sum += float(zap[i][4])

    else:
        sum = sum / kolvo
        dayandsrtemp.append(zap[i][1])
        dayandsrtemp.append(sum)
        sum = 0
        kolvo = 0
    buf.append(dayandsrtemp)
    dayandsrtemp = []

for i in buf:
    if i != []:
        allsrtd.append(i)
buf = []

#Среднее арифметическое температуры за весь период
sum = 0
kolvo = 0
for i in zap:
    sum += float(i[4])
    kolvo += 1
allsrar = sum/kolvo

#Вычисление макисмальной температуры
Max = 0
for i in range(len(allsrtd)):
    if i == len(allsrtd) - 1:
        break
    nextT = allsrtd[i][1]
    if nextT > Max:
        Max = nextT
        maxday = allsrtd[i]

#Вычисление минимальной температуры
Max = maxday[1]
for i in range(len(allsrtd)):
    if i == len(allsrtd) - 1:
        break
    nextT = allsrtd[i][1]
    if nextT < Max:
        Max = nextT
        mintemp = allsrtd[i]

#Подсчет ливневых дней
for i in zap:
    if i[34] != ' ':
        buf.append(i[34])

for i in buf:
    if i != 'Состояние неба в общем не изменилось. ':
        sumdojdday += 1

print('Средняя температура ' + str(allsrar) + ' дождливых дней ' + str(sumdojdday) + ' самый теплый день ' + maxday[0] + ' самый холодный день ' + mintemp[0])
