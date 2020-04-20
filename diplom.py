import time, threading, os, string, copy
import numpy as np
from decimal import Decimal
import tkinter as tk
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



    def open_txt(self):
        os.startfile('password.txt')


    def check_number(self, t1):
        try:
            t1 = int(t1)
        except:
            messagebox.showerror('Ошибка','Введите число!')
        return 5<= t1<=20, t1

    def wait(self):
        lab = Label(text = "Будь-ласка, зачекайте")
        lab.place(x = 450, y = 350)



    def schet(self, *args):
        self.wait()

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
            self.text.insert(END, '*')
            time.sleep(maybe_time)
            if self.cvar.get() == 0:
                self.proverka(modul)
            else: self.proverkaIzSimvolami(modul)

        abd = self.p.join(self.pas)
        self.text.configure(state='disabled')
        self.button_generation.configure(state = NORMAL)


    def clear(self):
        self.button_generation.configure(state = DISABLED)
        self.arr.clear()
        self.pas.clear()
        self.text.config(state='normal')
        self.text.delete(0, END)
        self.s = self.number_column.get()
        Tit,self.s = self.check_number(self.s)
        if Tit == True:
            #self.t.start()
            self.schet()
        else: messagebox.showerror('Ошибка','Ведите число от 5 до 20')

    def see(self):
        if self.cvar1.get() == 1:
            self.text.config(state='normal')
            self.text.delete(0, END)
            self.text.insert(0, self.p.join(self.pas))
            self.text.config(state='readonly')
        else:
            self.text.config(state='normal')
            self.text.delete(0, END)
            self.text.insert(0, "*"*len(self.pas))
            self.text.config(state='readonly')

    def writting_file(self):
        f = open('password.txt', 'w')
        for index in self.pas:
            f.write(str(index))
        f.close()
        Label(text = "Збережено!", font = "roboto 13").place(x = 305, y = 530)







    def __init__(self):
        self.x = 0
        self.arr = []
        self.pas = []
        self.p = ''
        self.initUI()

    def initUI(self):
        f_generate = ttk.Frame(width = 340, height = 80)
        f_generate.pack_propagate(0)
        f_generate.place(x = 280, y = 250)
        f_see = ttk.Frame(width = 120, height = 40)
        f_see.place(x = 275, y = 445)
        f_open = ttk.Frame(width = 120, height = 40)
        f_open.pack_propagate(0)
        f_open.place(x = 488, y = 480)
        f_save = ttk.Frame(width = 120, height = 40)
        f_save.pack_propagate(0)
        f_save.place(x = 295, y = 480)

        but_style = ttk.Style()
        but_style.configure ("Generation.TButton", font = ("SF UI",20, "bold"))
        but_style.configure ("Other.TButton", font = ("roboto",12))
        but_style.configure("Check.TCheckbutton", font = ("roboto", 12))
        but_style.configure("Number.TSpinbox", font = ("roboto", 12))




        Label(text = 'Генератор паролів', justify = CENTER, font=("Comic Sans MS", 24, "bold")).place(x = 320, y = 0)
        self.button_generation = ttk.Button(f_generate,text = 'Генерувати', command = self.clear, style = "Generation.TButton")
        button_write = ttk.Button(f_save,text = 'Зберегти', command = self.writting_file, style = "Other.TButton")
        button_open = ttk.Button(f_open,text = 'Відкрити файл', command = self.open_txt, style = "Other.TButton")
        self.cvar1 = BooleanVar()
        self.cvar1.set(0)
        button_see = ttk.Checkbutton(f_see,text = 'Показати пароль', command = self.see, variable=self.cvar1, onvalue=1, offvalue=0, style = "Check.TCheckbutton")
        self.text = Entry(width = 23,  font = ("roboto",20), state = "readonly")
        self.number_column = ttk.Spinbox(width=20, from_=6, to=20, style = "Number.TSpinbox")
        self.number_column.set(6)
        self.cvar = BooleanVar()
        self.cvar.set(0)
        c1 = ttk.Checkbutton(text="Використовувати спеціальні символи", variable=self.cvar, onvalue=1, offvalue=0, style = "Check.TCheckbutton")
        #self.progress = ttk.Progressbar(orient = HORIZONTAL, mode = 'indeterminate')
        #self.progress.place(x = 450, y = 350)
        #self.t = threading.Thread()
        #self.t.__init__(target = self.progress.start, args = ('1.'))


        Label(text = 'Для генерації паролю заповніть форму нижче та натисніть кнопку "Генерувати"', font = ("roboto",)).place(x = 116, y = 80)
        Label(text = 'Довжина: ', font = ("roboto",14)).place(x = 20, y = 125)
        self.number_column.place(x = 160, y = 130)
        Label(text = 'Від 6 до 20 символів', font = ("roboto", 10)).place(x = 160, y = 150)
        #Label(text = 'Символи:', font = ("roboto", 14)).place(x = 10, y = 180)

        c1.place(x = 155, y = 175)
        self.button_generation.pack(fill=tk.BOTH, expand=1)
        self.text.place(x = 275, y = 400)
        button_see.pack(fill=tk.BOTH, expand=1)
        button_write.pack(fill=tk.BOTH, expand=1)
        button_open.pack(fill=tk.BOTH, expand=1)


        #self.pb = Label(text = 'timer')
        #self.pb = ttk.Progressbar(mode="determinate", length = 100)
        #self.pb.place(x = 450, y = 350)









def main():
    root = Tk()
    root.geometry('900x600+320+240')
    #root.minsize(width = 800, height = 600)
    app = Password()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.title('Pentagon')
    root.mainloop()

if __name__ == '__main__':
    main()
