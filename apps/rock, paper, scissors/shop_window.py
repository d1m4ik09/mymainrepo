from tkinter import *

def shop():
    shop_win = Tk()
    shop_win.title('Магазин')
    shop_win.geometry('300x300')
    shop_win.config(bg = '#B0E0E6')
    shop_win.resizable(False, False)

    pack1 = False
    pack2 = False
    pack3 = False

    def pack_1():
        if pack1 == False and balance >= 250:
            balance -= 250
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')

    def pack_2():
        if pack2 == False and balance >= 500:
            balance -= 500
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')
    
    def pack_3():
        if pack3 == False and balance >= 1000:
            balance -= 1000
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')



    btn_pack1 = Button(shop_win,
                               bg = '#1E90FF',
                               command = pack_1,
                               text = 'Первый пак')
    
    btn_pack2 = Button(shop_win,
                               bg = '#1E90FF',
                               command = pack_2,
                               text = 'Второй пак')
    
    btn_pack3 = Button(shop_win,
                               bg = '#1E90FF',
                               command = pack_3,
                               text = 'Третий пак')