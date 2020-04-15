import time
import numpy as np
from decimal import Decimal
import copy
import string
from tkinter import *
import os
from tkinter.filedialog import *
from tkinter import messagebox

"""Объявление функций для полноценной работы программы"""


class Password:
    def securityMemory (self,a, i, j,c):
        for h in range(i, len(c), 1):
            for g in range(j, len(c[i]), 1):
                if c[h][g] != 0 or c[h][g] != a:
                    return True
                else: return False

    def method_square(self,a):
        b = a * a
        n = str(b)
        y = list(n)
        y = int(len(y))
        d = b // 10 ** (y - 2)
        f = b % 100
        a = d * 100 + f
        return a

    def proverka(self, bit):
        bit = bit %62
        self.pas.append(string.printable[bit])

    def proverkaIzSimvolami(bit):
        if bit >= 33 and bit <= 126:
            bit = chr(bit)
        return (bit)

    def writting_file(self):
        f = open('password.txt', 'w')
        for index in self.pas:
            f.write(str(index))
        f.close()

    def open_txt(self):
        os.startfile('password.txt')

    """Объявление переменных"""





    def check_number(self, t1):
        try:
            t1 = int(t1)
        except:
            messagebox.showerror('Ошибка','Введите число!')
        return 5<= t1<=20, t1

    def schet(self):
        self.arr.clear()
        self.pas.clear()
        self.text.delete(1.0, END)
        self.s = self.number_column.get()
        Tit,self.s = self.check_number(self.s)
        print(Tit)
        if Tit == True:
            for o in range(self.s):
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
                        indexTrue = self.securityMemory(d,i,j,c)
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
                                self.arr.append(memori)

            square = self.arr[0]*10000
            square = round(square)

            for i in range(1,self.s+1,1):
                square = self.method_square(square)
                rand_time = self.arr[i]
                myTime = time.time()
                secund = myTime*10**5
                secund = round(secund)
                modul = (secund) % square
                maybe_time = myTime-round(myTime-1)
                time.sleep(maybe_time)
                self.proverka(modul)

            p = ''
            global abd
            abd = p.join(self.pas)

            self.text.insert(1.0, abd)
        else: messagebox.showerror('Ошибка','Ведите число от 5 до 20')



    def __init__(self):
        self.x = 0
        self.arr = []
        self.pas = []
        self.initUI()

    def initUI(self):
        button_generation = Button(text = 'Генерировать', width = 30, height = 4, command = self.schet)
        button_write = Button(text = 'Записать в\n текстовый документ', width = 15, height = 2, command = self.writting_file)
        button_open = Button(text = 'Open file', width = 15, height = 2, command = self.open_txt)
        self.text = Text(width = 25, height = 3)
        self.number_column = Spinbox(width=7, from_=5, to=20)
        print(type(self.number_column.get()))
        self.number_column.pack()
        button_generation.pack(pady = 15)
        self.text.pack(pady = 10)

        button_write.pack(pady = 15)
        button_open.pack()





def main():
    root = Tk()
    root.minsize(width = 800, height = 600)
    app = Password()
    root.mainloop()


if __name__ == '__main__':
    main()
