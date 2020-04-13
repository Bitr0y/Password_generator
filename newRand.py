import time
import random
import numpy as np
from decimal import Decimal
import copy
x = 0

def securityMemory (a, i, j):
    for h in range(i, len(c), 1):
        for g in range(j, len(c[i]), 1):
            if c[h][g] != 0 or c[h][g] != a:
                return True
            else: return False

#Создание случайных чисел из памяти
arr =[]
emptyMemory = np.empty((20, 2))
c= copy.deepcopy(emptyMemory)
c.tolist()
print(type(c))
if c[0,0] == c[1,0]:
    emptyMemory2 = np.empty(20, 2)
    c = copy.deepcopy(emptyMemory2)
    c.tolist()
for i in range (0, len(c), 1):
    for j in range(len(c[i])):
        d = c[i][j]         #число которое нужно проверить
        indexTrue = securityMemory(d,i,j)
        if indexTrue == True:
            if c[i, j] >= 10000000000000000 or c[i, j] <= 0.00001:
                d = Decimal(d)
                #print(type(d))
                b = str(c[i,j])
                print(c[i,j])
                v1 = b.split('e')
                #print(v1)
                poww = str(v1[1])
                #print(poww)
                if ord(poww[0]) == 43:
                    memori = (float(c[i,j])/10**int(poww[1:]))
                elif ord(poww[0]) == 45:
                    #print(type(c[i,0]))
                    memori = (float((d*10**int(poww[1:]))))
                arr.append(memori)
print(arr)

'''

pas = []
#Создание списка простых чисел
n = 1000

lst=[2]
for i in range(3, n+1, 2):
	if (i > 10) and (i%10==5):
		continue
	for j in lst:
		if j*j-1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)

def proverka(bit):
    if bit >= 65 and bit <=90 or bit >= 97 and bit <= 122:
        bit = chr(bit)
    return(bit)

prime_number = random.choice(lst)


def method_square(a):
    b = a * a
    n = str(b)
    y = list(n)
    y = int(len(y))
    d = b // 10 ** (y - 2)
    f = b % 100
    a = d * 100 + f
    return a


first_number = random.random()*10000
first_number = round(first_number)


for i in range(5):
    square = method_square(first_number)
    rand_time = random.random() * 10
    arr = time.time()
    secund = arr*10**5
    secund = round(secund)
    modul = (secund * prime_number) % square
    time.sleep(rand_time)
    print('----')
    print(modul)
    modul = modul // 10
    number_for_password = proverka(modul)
    pas.append(str(number_for_password))

f = open('password.txt', 'w')

for index in pas:
    f.write(index)

f.close()

print(pas)

'''
