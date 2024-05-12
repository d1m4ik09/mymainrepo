from tkinter import *

def convert():
    lbl_res.config(text = f"{((int(entry.get()) * 9/5) + 32)} фаренгейтов")

def stop():
    window.destroy()

window = Tk()
window.geometry('300x300')
window.title('Конвертатер градусов')
window.resizable(False, False)

lbl_inform = Label(window, text = 'Конвертатор цельсии в фаренгейты', font = ('Arial', 10, 'bold'))
lbl_res = Label(window, text = 'Кол-во фарен', font = ('Arial', 15, 'bold'))
btn_start = Button(window, command = convert, text = 'Конвертировать', font = ('Arial', 15, 'bold'))
btn_stop = Button(window, text = 'Stop', command=stop, font = ('Arial', 15, 'bold'))
entry = Entry(window, font = ('Arial', 15, 'bold'))

lbl_inform.pack()
entry.pack(pady=10)
btn_start.pack(pady=10)
lbl_res.pack(pady=10)
btn_stop.pack(side = BOTTOM)

window.mainloop()