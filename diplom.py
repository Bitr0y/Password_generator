import time, threading, os, string, copy
import numpy as np
from decimal import Decimal
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import tkinter.ttk as ttk


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

    def proverkaIzSimvolami(self,bit):
        bit = bit % 94
        self.pas.append(string.printable[bit])

    def writting_file(self):
        f = open('password.txt', 'w')
        for index in self.pas:
            f.write(str(index))
        f.close()

    def open_txt(self):
        os.startfile('password.txt')


    def check_number(self, t1):
        try:
            t1 = int(t1)
        except:
            messagebox.showerror('Ошибка','Введите число!')
        return 5<= t1<=20, t1


    def schet(self, *args):

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
            myTime = time.time()
            secund = myTime*10**5
            secund = round(secund)
            modul = (secund) % square
            maybe_time = myTime-round(myTime-1)
            time.sleep(maybe_time)
            self.text.insert(END, '*')
            if self.cvar.get() == 0:
                self.proverka(modul)
            else: self.proverkaIzSimvolami(modul)

        p = ''
        global abd
        abd = p.join(self.pas)


    def clear(self):
        self.arr.clear()
        self.pas.clear()
        self.text.delete(1.0, END)
        self.s = self.number_column.get()
        Tit,self.s = self.check_number(self.s)
        if Tit == True:
            self.schet()
        else: messagebox.showerror('Ошибка','Ведите число от 5 до 20')

    def see(self):
        self.text.delete(1.0, END)
        self.text.insert(1.0, abd)




    def __init__(self):
        self.x = 0
        self.arr = []
        self.pas = []
        self.initUI()

    def initUI(self):
        Label(text = 'Генератор паролів', justify = CENTER, font=("Comic Sans MS", 24, "bold")).place(x = 320, y = 0)
        button_generation = Button(text = 'Генерувати', font = ("SF UI",20, "bold"), width = 20, height = 2, command = self.clear)
        button_write = Button(text = 'Записати в\n текстовий документ', font = ("roboto",12), width = 15, height = 2, command = self.writting_file)
        button_open = Button(text = 'Відкрити файл', font = ("roboto",12), width = 15, height = 2, command = self.open_txt)
        button_see = Button(text = 'Показати', font = ("roboto",12), width = 15, height = 2, command = self.see)
        self.text = Text(width = 47, height = 5)
        self.number_column = Spinbox(width=20, from_=5, to=20)
        self.cvar = BooleanVar()
        self.cvar.set(0)
        c1 = Checkbutton(text="Використовувати спеціальні символи", font = ("roboto"), variable=self.cvar, onvalue=1, offvalue=0)

        Label(text = 'Для генерації паролю заповніть форму нижче та натисніть кнопку "Генерувати"', font = ("roboto",)).place(x = 116, y = 80)
        Label(text = 'Довжина: ', font = ("roboto",14)).place(x = 20, y = 125)
        self.number_column.place(x = 160, y = 130)
        Label(text = 'Від 5 до 20 символів', font = ("roboto", 10)).place(x = 160, y = 150)
        #Label(text = 'Символи:', font = ("roboto", 14)).place(x = 10, y = 180)

        c1.place(x = 155, y = 175)
        button_generation.place(x = 280, y = 250)
        self.text.place(x = 230, y = 400)
        button_see.place(x = 620, y = 416)
        button_write.place(x = 250, y = 520)
        button_open.place(x = 450, y = 520)


        self.pb = Label(text = 'timer')
        #self.pb = ttk.Progressbar(mode="determinate", length = 100)
        self.pb.place(x = 450, y = 350)









def main():
    root = Tk()
    root.geometry('900x600+320+240')
    #root.minsize(width = 800, height = 600)
    app = Password()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()

if __name__ == '__main__':
    main()
