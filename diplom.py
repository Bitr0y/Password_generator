import time
import numpy as np
from decimal import Decimal
import copy
import string
from tkinter import *



root = Tk()
x = 0



def proverkaIzSimvolami(bit):
    if bit >= 33 and bit <= 126:
        bit = chr(bit)
    return (bit)

def securityMemory (a, i, j,c):
    for h in range(i, len(c), 1):
        for g in range(j, len(c[i]), 1):
            if c[h][g] != 0 or c[h][g] != a:
                return True
            else: return False

def proverka(bit):
    bit = bit %62
    pas.append(string.printable[bit])



def method_square(a):
    b = a * a
    n = str(b)
    y = list(n)
    y = int(len(y))
    d = b // 10 ** (y - 2)
    f = b % 100
    a = d * 100 + f
    return a


arr = []
pas = []
emptyMemory = np.empty((20, 2))
c = copy.deepcopy(emptyMemory)
c.tolist()
#Создание случайных чисел из памяти
for o in range(5):
    emptyMemory = np.empty((20, 2))
    c= copy.deepcopy(emptyMemory)
    c.tolist()
    if c[0,0] == c[1,0]:
        emptyMemory2 = np.empty(20, 2)
        c = copy.deepcopy(emptyMemory2)
        c.tolist()
    for i in range (0, len(c), 1):
        for j in range(len(c[i])):
            d = c[i][j]         #число которое нужно проверить
            indexTrue = securityMemory(d,i,j,c)
            if indexTrue == True:
                if c[i, j] >= 10000000000000000 or c[i, j] <= 0.00001:
                    d = Decimal(d)
                    b = str(c[i,j])
                    v1 = b.split('e')
                    poww = str(v1[1])
                    if ord(poww[0]) == 43:
                        memori = (float(c[i,j])/10**int(poww[1:]))
                    elif ord(poww[0]) == 45:
                        #print(type(c[i,0]))
                        memori = (float((d*10**int(poww[1:]))))
                    arr.append(memori)

square = arr[0]*10000
square = round(square)


for i in range(1,8,1):
    square = method_square(square)
    rand_time = arr[i]
    myTime = time.time()
    secund = myTime*10**5
    secund = round(secund)
    modul = (secund) % square
    maybe_time = myTime-round(myTime-1)
    time.sleep(maybe_time)
    proverka(modul)

f = open('password.txt', 'w')
for index in pas:
    f.write(str(index))

pp = ''
abd = pp.join(pas)
#print(o)
f.close()

"""Генерация окна приложения"""
root.minsize(width = 800, height = 600)
text = Text(width = 25, height = 3)
text.insert(1.0, abd)

text.pack()



root.mainloop()
