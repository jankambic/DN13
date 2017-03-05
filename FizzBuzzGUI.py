#coding: utf-8

import Tkinter
import tkMessageBox

def naloga():
    i = 0
    izbrano_stevilo = int(vnos.get())
    while i < izbrano_stevilo:
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            rezultat_text = ("FizzBuzz")
        elif i % 3 == 0:
            rezultat_text = ("Fizz")
        elif i % 5 == 0:
            rezultat_text = ("Buzz")
        else:
            rezultat_text = (i)

        tkMessageBox.showinfo("Rezultat", rezultat_text)

fizzbuzz = Tkinter.Tk()
fizzbuzz.title("Fizzbuzz")
fizzbuzz.geometry("300x300")

navodilo = Tkinter.Label(fizzbuzz, text="Vpišite številko med 1 in 50.")
navodilo.pack()

vnos = Tkinter.Entry(fizzbuzz)
vnos.pack()

zazeni = Tkinter.Button(fizzbuzz, text="Zaženi", command=naloga)
zazeni.pack()

fizzbuzz.mainloop()



