import time
import random

pas = []
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
