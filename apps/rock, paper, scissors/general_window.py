from random import *
from tkinter import *

def game_win():
    def stop_res():
        window_game.destroy()
        result_win()

    def stop_shop():
        window_game.destroy()
        shop()

    def save():
        name = entry.get()
        if name == '':
            name = 'guest'
        
        with open('./apps/rock, paper, scissors/information.txt', 'a') as file:
            if score_per == 0:
                stat = "{} {} {} {} {} {} {}\n".format(name, balance, max_streak, 0, 
                                                       pack1_bool, pack2_bool, pack3_bool, pack4_bool, pack5_bool)
            else:
                stat = "{} {} {} {} {} {} {}\n".format(name, balance, max_streak, round((score_comp + score_per) / score_per * 100), 
                                                       pack1_bool, pack2_bool, pack3_bool, pack4_bool, pack5_bool)
            file.write(stat)

    def per_choice(user_choice):
        global score_per, score_comp, stavka, balance, streak, max_streak, balance, streak, pack1_bool, pack2_bool, pack3_bool, pack4_bool

        name = entry.get()
        comp_choice = choice(choice_pos)
        lbl_per_choice.config(text= user_choice)
        lbl_comp_choice.config(text = comp_choice)

        if name == 'test09qwe12':
            balance = 999999
            streak = 15
            pack5_bool = pack4_bool = pack3_bool = pack2_bool = pack1_bool = True
            streak += 1
            if streak >= 5:
                balance += (round(streak / 1000 * balance) + stavka)
            else:
                balance += stavka
            if streak > max_streak:
                max_streak = streak
            score_per += 1
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#008000')
            lbl_streak.config(text = ('Стрик', streak))
            lbl_balance.config(text = ('Баланс', balance))
        else:
            if user_choice == comp_choice:
                lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                                bg = '#808080')
            elif user_choice == choice_pos[choice_pos.index(comp_choice) - 1]:
                streak += 1
                if streak >= 5:
                    balance += (round(streak / 1000 * balance) + stavka)
                else:
                    balance += stavka
                if streak > max_streak:
                    max_streak = streak
                score_per += 1
                lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                                bg = '#008000')
                lbl_streak.config(text = ('Стрик', streak))
                lbl_balance.config(text = ('Баланс', balance)) 
            else:
                score_comp += 1
                balance -= stavka
                streak = 0
                lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                                bg = '#B22222')
                lbl_streak.config(text = ('Стрик', streak))

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
        global stavka_bool, stavka

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

    def stat_win():
        def stop():
            window_stat.destroy()
        window_stat = Tk()
        window_stat.title('Статистика')
        window_stat.iconbitmap('./apps/rock, paper, scissors/picture/icon_stat.ico')
        window_stat.configure(bg = '#B0E0E6')
        window_stat.geometry('200x200+100+200')
        window_stat.resizable(False, False)
        if score_per == 0 and score_comp == 0:
            stat = 0
        else:
            stat = round(100 * score_per /(score_comp + score_per))
        name = entry.get()
        if name == '':
            name = 'guest'

        btn_stop = Button(window_stat, text = 'Выйти', font = ('Comfortaa'), command= stop)
        btn_stop.place(x = 60, y = 170, width= 60)

        label = Label(window_stat, text = "Имя: {}\n Баланс: {}\n Серия побед: {}\n Проиграл: {}\n Выиграл: {}\n Процент побед: {}%\n".format(name, balance, max_streak, score_comp, score_per, stat),
                      font = ('Comfortaa'))
        label.place(x = 0, y = 0, width=200)

    window_game = Tk()
    window_game.title('Камень, ножницы, бумага')
    window_game.iconbitmap('./apps/rock, paper, scissors/picture/icon_game.ico')
    window_game.configure(bg = '#B0E0E6')
    window_game.geometry('900x750+10+20')
    window_game.resizable(False, False)

    shop_image = PhotoImage(file = './apps/rock, paper, scissors/picture/shop.png')

    rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_1.png')
    paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_1.png')
    scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_1.png')

    if cur_pack == 'pack2':
        rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_2.png')
        paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_2.png')
        scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_2.png')
    elif cur_pack == 'pack3':
        rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_3.png')
        paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_3.png')
        scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_3.png')
    elif cur_pack == 'pack4':
        rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_4.png')
        paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_4.png')
        scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_4.png')
    elif cur_pack == 'pack5':
        rock_image = PhotoImage(file = './apps/rock, paper, scissors/picture/rock_5.png')
        paper_image = PhotoImage(file = './apps/rock, paper, scissors/picture/paper_5.png')
        scissors_image = PhotoImage(file = './apps/rock, paper, scissors/picture/scissors_5.png')

    btn_rock = Button(window_game, image = rock_image, font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = rock )
    btn_paper = Button(window_game, image = paper_image,  font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = paper)
    btn_scissors = Button(window_game, image = scissors_image, font = ('Comfortaa'), borderwidth=0, bg = '#B0E0E6', command = scissors)                      
    btn_stop = Button(window_game, text = 'Стоп', font = ('Comfortaa'), bg = '#1E90FF', command = stop_res)   
    btn_shop = Button(window_game, image = shop_image, command = stop_shop, bg = '#1E90FF')   
    btn_plus = Button(window_game, text = '+', font = ('Comfortaa'), bg = '#1E90FF', command = plus)   
    btn_minus = Button(window_game, text = '-', font = ('Comfortaa'), bg = '#1E90FF', command = minus)   
    btn_no_stavka = Button(window_game, text = '0', font = ('Comforta'), bg = '#1E90FF', command= no_stavka)
    btn_save = Button(window_game, text = 'Save', font = ('Comforta'), bg = '#1E90FF', command= save)
    btn_stat = Button(window_game, text = 'stat', font = ('Comfortaa'), bg = '#1E90FF', command = stat_win)

    entry = Entry(window_game, font = ('Comforta'))

    lbl_comp_choice = Label(window_game, text = 'Выбор компьютера', bg = '#1E90FF', font = ('Comfortaa'))
    lbl_per_choice = Label(window_game, text = 'Ваш выбор', bg = '#1E90FF', font = ('Comfortaa'))
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
    btn_stat.place(y = 700, width=50, height= 50)
    
    lbl_comp_choice.place(x = 550, y = 150, width = 200, height = 200, )   
    lbl_per_choice.place(x = 150, y = 150, width = 200, height = 200, )    
    lbl_score.place(x = 350, width = 200, height = 50, )   
    lbl_stavka.place(x = 650, y = 50, width= 200, height=50)
    lbl_balance.place(x = 650, width = 250, height= 50)
    lbl_streak.place(x = 350, y = 60, height= 50, width= 200)
    
    window_game.mainloop()

def shop():
    def pack_1():
        global cur_pack
        cur_pack = 'pack1'
        shop_win.destroy()
        game_win()

    def pack_2():
        global pack2_bool, balance, cur_pack

        if pack2_bool == False and balance >= 500:
            balance -= 500
            pack2_bool = True
            cur_pack = 'pack2'
            shop_win.destroy()
            game_win()
        else:
            cur_pack = 'pack2'
            shop_win.destroy()
            game_win()

    def pack_3():
        global pack3_bool, balance, cur_pack

        if pack3_bool == False and balance >= 1000:
            balance -= 1000
            pack3_bool = True
            cur_pack = 'pack3'
            shop_win.destroy()
            game_win()
        else:
            cur_pack = 'pack3'  
            shop_win.destroy()
            game_win()

    def pack_4():
        global pack4_bool, balance, cur_pack

        if pack4_bool == False and balance >= 1500:
            balance -= 1500
            pack4_bool = True
            cur_pack = 'pack4'
            shop_win.destroy()
            game_win()
        else:
            cur_pack = 'pack4'
            shop_win.destroy()
            game_win()

    def pack_5():
        global pack5_bool, balance, cur_pack

        if pack5_bool == False and balance >= 2000:
            balance -= 2000
            pack5_bool = True
            cur_pack = 'pack5'
            shop_win.destroy()
            game_win()
        else:
            cur_pack = 'pack5'
            shop_win.destroy()
            game_win()

    shop_win = Tk()
    shop_win.title('Магазин')
    shop_win.geometry('150x250')
    shop_win.iconbitmap('./apps/rock, paper, scissors/picture/icon_shop.ico')
    shop_win.config(bg = '#B0E0E6')
    shop_win.resizable(False, False)
    btn_pack1 = Button(shop_win, bg = '#1E90FF', command = pack_1, text = 'Первый пак')  
    btn_pack2 = Button(shop_win, bg = '#1E90FF', command = pack_2, text = 'Второй пак')
    btn_pack3 = Button(shop_win, bg = '#1E90FF', command = pack_3, text = 'Третий пак')
    btn_pack4 = Button(shop_win, bg = '#1E90FF', command = pack_4, text = 'Четвёртый пак')
    btn_pack5 = Button(shop_win, bg = '#1E90FF', command = pack_5, text = 'Пятый пак')
    btn_pack1.place(height=50, width=150)
    btn_pack2.place(y = 50, height=50, width=150)
    btn_pack3.place(y = 100, height=50, width=150)
    btn_pack4.place(y = 150, height=50, width=150)
    btn_pack5.place(y = 200, height=50, width=150)

def result_win():
    global score_per, score_comp

    def new_game():
        global score_per, score_comp, streak
        score_per = score_comp = streak = 0
        window_result.destroy()
        game_win()

    def stop():
        window_result.destroy()

    window_result = Tk() #создаём окно
    window_result.title('Результаты') #название
    window_result.iconbitmap('./apps/rock, paper, scissors/picture/icon_game.ico') #иконка окна
    window_result.configure(bg = '#B0E0E6', #цвет окна
                        )
    window_result.geometry('350x450+100+20') #750, 400 #где находится окно и размер
    window_result.resizable(False, False) #нельзя изменять размеры

    
    if score_comp > score_per:
        winner = 'Компьютер'
    elif score_comp == score_per:
        winner = 'Ничья'
    else:
        winner = 'Пользователь'

    lbl_win = Label(window_result, text = 'Победитель:', bg = '#B0E0E6', font = ('Comfortaa'), width = 13, height = 2)
    lbl_winner = Label(window_result, bg = '#1E90FF', font = ('Comfortaa'), text= winner, width = 15, height = 3)
    lbl_score = Label(bg = '#1E90FF', text = (str(score_per) + ':' + str(score_comp)), font = ('Comfortaa'), width = 15, height = 3)

    btn_new_game = Button(window_result, text = 'Новая игра!', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 5, command = new_game)
    btn_stop = Button(window_result, text = 'Выйти', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 2, command= stop)
    
    lbl_win.pack()
    lbl_winner.pack()
    lbl_score.pack(pady = 50)
    btn_stop.pack(pady= 10)
    btn_new_game.pack(side = BOTTOM)

    window_result.mainloop()


score_per = 0
score_comp = 0
balance = 10000
stavka = 10
streak = 0
max_streak = 0

pack1_bool = True
pack2_bool = False
pack3_bool = False
pack4_bool = False
pack5_bool = False
stavka_bool = False

cur_pack = 'pack1'

choice_pos = ['Камень', 'Ножницы', 'Бумага']

game_win()