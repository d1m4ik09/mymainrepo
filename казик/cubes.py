from random import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

def quit():
    window.destroy()

def throw():
    global money
    global stavka
    per_choice = choice_num.get()
    comp_choice1 = randint(1, 6)
    lbl_comp_choice.config(text = ('Выбор компьютера:', str(comp_choice1)))
    if comp_choice1 == int(per_choice):
        money += stavka
        window.config(bg = '#008000')
    else:
        money -= stavka
        window.config(bg = '#FF0000')
    lbl_bal.config(text = ('Баланс:', money))

def plus():
    global stavka
    stavka += 1
    if stavka - 1 == money:
        stavka -= 1
    lbl_stavka.config(text = ('Ставка:', stavka))

def minus():
    global stavka
    stavka -= 1
    while stavka < 1:
        stavka += 1
    lbl_stavka.config(text = ('Ставка:', stavka))


window = Tk()
window.title('Кубы')
window.iconbitmap('C:\кухарев\-----------------main\казик\Casino.png')
window.configure(bg = '#B0E0E6',
                 )
window.geometry('500x500+10+20')
window.resizable(False, False)

money = 100
stavka = 5


choice_num = Combobox(window,
                      state='abled')
choice_num['values'] = (1, 2, 3, 4, 5, 6)
choice_num.grid()


btn_quit = Button(window,
                  text = 'Stop',
                  command=quit)
btn_quit.grid()


btn_random = Button(window,
                    text = 'Бросить',
                    command = throw)
btn_random.grid()

btn_plus = Button(window,
                  text = '+',
                  command= plus)
btn_plus.grid()


btn_minus = Button(window,
                   text = '-',
                   command= minus)
btn_minus.grid()


lbl_comp_choice = Label(window,
                        text = 'Выбор компьютера:')
lbl_comp_choice.grid()


lbl_bal = Label(window,
                text = ('Баланс:', money))
lbl_bal.grid()


lbl_stavka = Label(window,
                   text = ('Ставка:', stavka))
lbl_stavka.grid()

window.mainloop()