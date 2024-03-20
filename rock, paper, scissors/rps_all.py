from random import *
from tkinter import *

def game_win():
    def stop():
        window_game.destroy()
        result_win()

    def per_choice(user_choice):
        global score_per
        global score_comp
        global stavka
        global balance

        comp_choice = choice(choice_pos)
        lbl_per_choice.config(text= user_choice)
        lbl_comp_choice.config(text = comp_choice)

        if user_choice == comp_choice:
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#808080')
        elif user_choice == choice_pos[choice_pos.index(comp_choice) - 1]:
            score_per += 1
            balance += stavka
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#008000')
            lbl_balance.config(text = ('Баланс', balance))
        else:
            score_comp += 1
            balance -= stavka
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#B22222')
              
        if stavka > balance:
            stavka = balance
            lbl_stavka.config(text = ('Ставка', stavka))

        if balance > 0:
            lbl_balance.config(text = ('Баланс', balance))
        else:
            balance = 1000
            stop()

    def rock():
        per_choice('Камень')

    def paper():
        per_choice('Бумага')

    def scissors():
        per_choice('Ножницы')

    def plus():
        global stavka

        stavka += 5
        if stavka >= balance:
            stavka -= 5
        lbl_stavka.config(text = ('Ставка', stavka))

    def minus():
        global stavka

        stavka -= 5
        while stavka < 0:
            stavka += 1
        lbl_stavka.config(text = ('Ставка', stavka))

    def no_stavka():
        global stavka_bool
        global stavka

        if stavka_bool:
            stavka_bool = False
            stavka = 10
            lbl_stavka.config(text = ('Ставка', stavka))
            btn_minus.config(state = 'active')
            btn_plus.config(state = 'active')
        else:
            stavka_bool = True
            stavka = 0
            lbl_stavka.config(text = ('Ставка', stavka))
            btn_minus.config(state = 'disabled')
            btn_plus.config(state = 'disabled')

    window_game = Tk()
    window_game.title('Камень, ножницы, бумага')
    window_game.iconbitmap('./rock, paper, scissors/picture/icon.png')
    window_game.configure(bg = '#B0E0E6')
    window_game.geometry('900x750+10+20')
    window_game.resizable(False, False)

    rock_image_1 = PhotoImage(file = './rock, paper, scissors/picture/rock.png')
    paper_image_1 = PhotoImage(file = './rock, paper, scissors/picture/paper.png')
    scissors_image_1 = PhotoImage(file = './rock, paper, scissors/picture/scissors.png')

    rock_image_2 = PhotoImage(file = '')
    paper_image_2 = PhotoImage(file = '')
    scissors_image_2 = PhotoImage(file = '')
    
    shop_image = PhotoImage(file = './rock, paper, scissors/picture/shop.png')

    rock_image = rock_image_1
    paper_image = paper_image_1
    scissors_image = scissors_image_1

    #Кнопка выбора камня
    btn_rock = Button(window_game, image = rock_image, font = ('Comfortaa'), bg = '#1E90FF', command = rock )

    #Кнопка выбора бумаги
    btn_paper = Button(window_game, image = paper_image, bg = '#1E90FF', font = ('Comfortaa'), command = paper)

    #Кнопка выбора ножниц
    btn_scissors = Button(window_game, image = scissors_image, font = ('Comfortaa'), bg = '#1E90FF', command = scissors)

    #кнопка стоп
    btn_stop = Button(window_game, text = 'Стоп', font = ('Comfortaa'), bg = '#1E90FF', command = stop)
    
    btn_shop = Button(window_game, image = shop_image, command = shop, bg = '#1E90FF')
    
    btn_plus = Button(window_game, text = '+', font = ('Comfortaa'), bg = '#1E90FF', command = plus)
    
    btn_minus = Button(window_game, text = '-', font = ('Comfortaa'), bg = '#1E90FF', command = minus)
    
    btn_no_stavka = Button(window_game, text = '0', font = ('Comforta'), bg = '#1E90FF', command= no_stavka)

    #Что выбрал комп
    lbl_comp_choice = Label(window_game, text = 'Выбор компьютера', bg = '#1E90FF', font = ('Comfortaa'))

    #Что выбрал пользователя
    lbl_per_choice = Label(window_game, text = 'Ваш выбор', bg = '#1E90FF', font = ('Comfortaa'))

    #счёт
    lbl_score = Label(window_game, text = 'Счёт', bg = '#1E90FF', font = ('Comfortaa'))
    
    lbl_stavka = Label(window_game, text = ('Cтавка', stavka), bg = '#1E90FF', font = ('Comfortaa', 13))
    
    lbl_balance = Label(window_game, text = ('Баланс', balance), bg = '#1E90FF', font = ('Comfortaa'))

    btn_rock.place(x = 100, y = 400, width = 200, height = 200, )
    
    btn_paper.place(x = 600, y = 400, width = 200, height = 200, )
    
    btn_scissors.place(x = 350, y = 400, width = 200, height = 200, )
    
    btn_stop.place(x = 300, y = 650, height = 100, width = 300, )
    
    btn_shop.place(height=100, width=100, )
    
    btn_plus.place(x = 850, y = 50, height= 50, width = 50, )

    btn_minus.place(x = 600, y = 50, height= 50, width = 50, )
    
    btn_no_stavka.place(x = 600, height = 50, width = 50, )
    
    lbl_comp_choice.place(x = 550, y = 150, width = 200, height = 200, )
    
    lbl_per_choice.place(x = 150, y = 150, width = 200, height = 200, )
    
    lbl_score.place(x = 350, width = 200, height = 100, )
    
    lbl_stavka.place(x = 650, y = 50, width= 200, height=50)

    lbl_balance.place(x = 650, width = 250, height= 50)
    
    window_game.mainloop()


def result_win():
    global score_per
    global score_comp

    def new_game():
        global score_per
        global score_comp
        score_per, score_comp = 0, 0
        window_result.destroy()
        game_win()

    window_result = Tk() #создаём окно
    window_result.title('Камень, ножницы, бумага') #название
    window_result.iconbitmap('./rock, paper, scissors/picture/icon.png') #иконка окна
    window_result.configure(bg = '#B0E0E6', #цвет окна
                        )
    window_result.geometry('350x450+100+20') #750, 400 #где находится окно и размер
    window_result.resizable(False, False) #нельзя изменять размеры

    #надпись победитель
    lbl_win = Label(window_result, text = 'Победитель:', bg = '#B0E0E6', font = ('Comfortaa'), width = 13, height = 2)
    
    if score_comp > score_per:
        winner = 'Компьютер'
    elif score_comp == score_per:
        winner = 'Ничья'
    else:
        winner = 'Пользователь'

    #Имя победителя/комп
    pri_win = Label(window_result, bg = '#1E90FF', font = ('Comfortaa'), text= winner, width = 15, height = 3)

    #Счёт
    score = Label(bg = '#1E90FF', text = (str(score_per) + ':' + str(score_comp)), font = ('Comfortaa'), width = 15, height = 3)

    #Новая игра
    btn_new_game = Button(window_result, text = 'Новая игра!', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 5, command = new_game)
    
    lbl_win.pack()
    pri_win.pack()
    score.pack(pady = 50)
    btn_new_game.pack(side = BOTTOM)

    window_result.mainloop()

def shop():
    shop_win = Tk()
    shop_win.title('Магазин')
    shop_win.geometry('300x300')
    shop_win.config(bg = '#B0E0E6')
    shop_win.resizable(False, False)

    def pack_1():
        if pack1_bool == False and balance >= 250:
            balance -= 250
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')

    def pack_2():
        if pack2_bool == False and balance >= 500:
            balance -= 500
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')
    
    def pack_3():
        if pack3_bool == False and balance >= 1000:
            balance -= 1000
            rock_image = PhotoImage(file = '')
            paper_image = PhotoImage(file = '')
            scissors_image = PhotoImage(file = '')

    btn_pack1 = Button(shop_win, bg = '#1E90FF', command = pack_1, text = 'Первый пак')
    
    btn_pack2 = Button(shop_win, bg = '#1E90FF', command = pack_2, text = 'Второй пак')
    
    btn_pack3 = Button(shop_win, bg = '#1E90FF', command = pack_3, text = 'Третий пак')


score_per = 0
score_comp = 0

balance = 1000
stavka = 10

pack1_bool = False
pack2_bool = False
pack3_bool = False

stavka_bool = False

choice_pos = ['Камень', 'Ножницы', 'Бумага']

game_win()