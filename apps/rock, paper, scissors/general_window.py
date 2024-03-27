from random import *
from tkinter import *
from PIL import Image

def game_win():
    def stop_res():
        window_game.destroy()
        result_win()

    def stop_shop():
        window_game.destroy()
        shop()

    def save():
<<<<<<< HEAD
        name = entry.get()
        if name == '':
            name = 'guest'
        with open('C:/Users/213-16/Downloads/mymainrepo/apps/rock, paper, scissors/information.txt', 'a') as file:
            stat = "{} {} {} {} {} {} {}\n".format(name, balance, max_streak, round((score_comp + score_per) / score_per * 100), pack1_bool, pack2_bool, pack3_bool)
            file.write(stat)
        file.close()
=======
        pass
>>>>>>> 45720eb117f6c756a2b0e8974c18b30690459e0a

    def per_choice(user_choice):
        global score_per
        global score_comp
        global stavka
        global balance
        global streak

        comp_choice = choice(choice_pos)
        lbl_per_choice.config(text= user_choice)
        lbl_comp_choice.config(text = comp_choice)

<<<<<<< HEAD
        # if user_choice == comp_choice:
        #     lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
        #                     bg = '#808080')
        if user_choice == choice_pos[choice_pos.index(comp_choice) - 1]:
            streak += 1
            if streak >= 5:
                if stavka != 0:
                    balance += (round(streak / 1000 * balance) + stavka)
=======
        if user_choice == comp_choice:
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#808080')
        elif user_choice == choice_pos[choice_pos.index(comp_choice) - 1]:
            streak += 1
            if streak >= 5:
                balance += (round(streak / 1000 * balance) + stavka)
>>>>>>> 45720eb117f6c756a2b0e8974c18b30690459e0a
            else:
                balance += stavka
            score_per += 1
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#008000')
            lbl_streak.config(text = ('Стрик', streak))
            lbl_balance.config(text = ('Баланс', balance))
<<<<<<< HEAD
        # else:
        #     score_comp += 1
        #     balance -= stavka
        #     streak = 0
        #     lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
        #                     bg = '#B22222')
        #     lbl_streak.config(text = ('Стрик', streak))
=======
        else:
            score_comp += 1
            balance -= stavka
            streak = 0
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#B22222')
            lbl_streak.config(text = ('Стрик', streak))
>>>>>>> 45720eb117f6c756a2b0e8974c18b30690459e0a

        if stavka > balance:
            stavka = balance
            lbl_stavka.config(text = ('Ставка', stavka))

        if balance > 0:
            lbl_balance.config(text = ('Баланс', balance))
        else:
            balance = 1000
            streak = 0
            stop_res()

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

    def no_stavka(): #Режим игры без ставок
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
    window_game.iconbitmap('./apps/rock, paper, scissors/picture/icon.png')
    window_game.configure(bg = '#B0E0E6')
    window_game.geometry('900x750+10+20')
    window_game.resizable(False, False)
    
    shop_image = PhotoImage(file = './apps/rock, paper, scissors/picture/shop.png')

    rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_1.png')
    paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_1.png')
    scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_1.png')

    #Кнопка выбора камня
    btn_rock = Button(window_game, image = rock_image, font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = rock )
    #Кнопка выбора бумаги
    btn_paper = Button(window_game, image = paper_image,  font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = paper)
    #Кнопка выбора ножниц
    btn_scissors = Button(window_game, image = scissors_image, font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = scissors)
    #кнопка стоп                        
    btn_stop = Button(window_game, text = 'Стоп', font = ('Comfortaa'), bg = '#1E90FF', command = stop_res)   
    btn_shop = Button(window_game, image = shop_image, command = stop_shop, bg = '#1E90FF')   
    btn_plus = Button(window_game, text = '+', font = ('Comfortaa'), bg = '#1E90FF', command = plus)   
    btn_minus = Button(window_game, text = '-', font = ('Comfortaa'), bg = '#1E90FF', command = minus)   
    btn_no_stavka = Button(window_game, text = '0', font = ('Comforta'), bg = '#1E90FF', command= no_stavka)
    btn_save = Button(window_game, text = 'Save', font = ('Comforta'), bg = '#1E90FF', command= save)

    entry = Entry(window_game, font = ('Comforta'))

    #Что выбрал комп
    lbl_comp_choice = Label(window_game, text = 'Выбор компьютера', bg = '#1E90FF', font = ('Comfortaa'))
    #Что выбрал пользователя
    lbl_per_choice = Label(window_game, text = 'Ваш выбор', bg = '#1E90FF', font = ('Comfortaa'))
    #счёт
    lbl_score = Label(window_game, text = 'Счёт', bg = '#1E90FF', font = ('Comfortaa'))    
    lbl_stavka = Label(window_game, text = ('Cтавка', stavka), bg = '#1E90FF', font = ('Comfortaa', 13))    
    lbl_balance = Label(window_game, text = ('Баланс', balance), bg = '#1E90FF', font = ('Comfortaa'))
    lbl_streak = Label(window_game, text = ('Стрик', streak), bg = '#1E90FF', font = ('Comfortaa'))

    entry.place(x = 400, y = 150, width = 100)

    btn_rock.place(x = 100, y = 400, width = 200, height = 200, )   
    btn_paper.place(x = 600, y = 400, width = 200, height = 200, )   
    btn_scissors.place(x = 350, y = 400, width = 200, height = 200, )    
    btn_stop.place(x = 300, y = 650, height = 100, width = 300, )   
    btn_shop.place(height=100, width=100, )   
    btn_plus.place(x = 850, y = 50, height= 50, width = 50, )
    btn_minus.place(x = 600, y = 50, height= 50, width = 50, )  
    btn_no_stavka.place(x = 600, height = 50, width = 50, )
    btn_save.place(x = 425, y = 190, width=50)
    
    lbl_comp_choice.place(x = 550, y = 150, width = 200, height = 200, )   
    lbl_per_choice.place(x = 150, y = 150, width = 200, height = 200, )    
    lbl_score.place(x = 350, width = 200, height = 50, )   
    lbl_stavka.place(x = 650, y = 50, width= 200, height=50)
    lbl_balance.place(x = 650, width = 250, height= 50)
    lbl_streak.place(x = 350, y = 60, height= 50, width= 200)
<<<<<<< HEAD
=======

    name = entry.get()
>>>>>>> 45720eb117f6c756a2b0e8974c18b30690459e0a
    
    window_game.mainloop()

def shop():
    def pack_1():
        global rock_image
        global paper_image
        global scissors_image
        rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_1.png')
        paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_1.png')
        scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_1.png')
        game_win()
        shop_win.destroy()

    def pack_2():
        global pack2_bool
        global balance
        global rock_image
        global paper_image
        global scissors_image
        if pack2_bool == False and balance >= 500:
            balance -= 500
            pack2_bool = True
            rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_2.png')
            paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_2.png')
            scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_2.png')
            game_win()
            shop_win.destroy()
        else:
            rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_2.png')
            paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_2.png')
            scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_2.png')
            game_win()
            shop_win.destroy()

    def pack_3():
            global pack3_bool
            global balance
            global rock_image
            global paper_image
            global scissors_image

            if pack3_bool == False and balance >= 1000:
                balance -= 1000
                rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')    
                paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')    
                scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')
                game_win()
                shop_win.destroy()

            else:
                rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')    
                paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')    
                scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')    
                game_win()
                shop_win.destroy()

    shop_win = Tk()
    shop_win.title('Магазин')
    shop_win.geometry('300x300')
    shop_win.config(bg = '#B0E0E6')
    shop_win.resizable(False, False)
    btn_pack1 = Button(shop_win, bg = '#1E90FF', command = pack_1, text = 'Первый пак')  
    btn_pack2 = Button(shop_win, bg = '#1E90FF', command = pack_2, text = 'Второй пак')
    btn_pack3 = Button(shop_win, bg = '#1E90FF', command = pack_3, text = 'Третий пак')
    btn_pack1.place(height=50, width=150)
    btn_pack2.place(y = 50, height=50, width=150)
    btn_pack3.place(y = 100, height=50, width=150)

def result_win():
    global score_per
    global score_comp

    def new_game():
        global score_per
        global score_comp
        score_per, score_comp = 0, 0
        window_result.destroy()
        game_win()

    def stop():
        window_result.destroy()

    window_result = Tk() #создаём окно
    window_result.title('Камень, ножницы, бумага') #название
    window_result.iconbitmap('./apps/rock, paper, scissors/picture/icon.png') #иконка окна
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

    btn_stop = Button(window_result, text = 'Выйти', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 2, command= stop)
    
    lbl_win.pack()
    pri_win.pack()
    score.pack(pady = 50)
    btn_stop.pack(pady= 10)
    btn_new_game.pack(side = BOTTOM)

    window_result.mainloop()


score_per = 0
score_comp = 0

balance = 10000
stavka = 10
streak = 0
max_streak = 0

pack1_bool = False
pack2_bool = False
pack3_bool = False

stavka_bool = False

choice_pos = ['Камень', 'Ножницы', 'Бумага']

game_win()