from random import *
from tkinter import *
from PIL import Image

def game_win():
    def stop_res():
        window_game.destroy()
        menu_win()

    def stop_shop():
        window_game.destroy()
        shop()

    def per_choice(user_choice):
        global score_per, score_comp, bet, balance, streak, balance, streak, test

        if test:
            global pack5_bool, pack4_bool, pack3_bool, pack2_bool, balance
            balance = 999999
            pack5_bool = pack4_bool = pack3_bool = pack2_bool = True
            test = False
            lbl_balance.config(text = ('Баланс', balance))

        wti = {'r' : rock_image,
              'p' : paper_image,
              's' : scissors_image
              }
        
        comp_choice = choice(choice_pos)
        lbl_per_choice.config(image = wti[user_choice])
        lbl_comp_choice.config(image = wti[comp_choice])


        if user_choice == comp_choice:
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                            bg = '#808080')
        elif user_choice == choice_pos[choice_pos.index(comp_choice) - 1]:
            streak += 1
            if streak >= 5:
                balance += (round(streak / 1000 * balance) + bet)
            else:
                balance += bet
            score_per += 1
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                                bg = '#008000')
            lbl_streak.config(text = ('Стрик', streak))
            lbl_balance.config(text = ('Баланс', balance)) 
        else:
            score_comp += 1
            balance -= bet
            streak = 0
            lbl_score.config(text = (str(score_per) + ':' + str(score_comp)),
                                bg = '#B22222')
            lbl_streak.config(text = ('Стрик', streak))
            lbl_balance.config(text = ('Баланс', balance))

        if bet > balance:
            bet = balance
            lbl_bet.config(text = ('Ставка', bet))

        if balance <= 0:
            balance = 1000
            stop_res()

    def rock():
        per_choice('r')

    def paper():
        per_choice('p')

    def scissors():
        per_choice('s')

    def plus():
        global bet

        bet += 5
        if bet >= balance:
            bet -= 5
        lbl_bet.config(text = ('Ставка', bet))

    def minus():
        global bet

        bet -= 5
        while bet < 0:
            bet += 1
        lbl_bet.config(text = ('Ставка', bet))

    def no_bet(): #Режим игры без ставок
        global bet_bool, bet

        if bet_bool:
            bet_bool = False
            bet = 10
            lbl_bet.config(text = ('Ставка', bet))
            btn_minus.config(state = 'active')
            btn_plus.config(state = 'active')
        else:
            bet_bool = True
            bet = 0
            lbl_bet.config(text = ('Ставка', bet))
            btn_minus.config(state = 'disabled')
            btn_plus.config(state = 'disabled')

    window_game = Tk()
    window_game.title('Камень, ножницы, бумага')
    window_game.iconbitmap('./apps/rock, paper, scissors/picture/icon_game.ico')
    window_game.configure(bg = '#808080')
    window_game.geometry('900x750+10+20')
    window_game.resizable(True, True)

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

    btn_rock = Button(window_game, image = rock_image, bg = '#808080', borderwidth=0, command = rock )
    btn_paper = Button(window_game, image = paper_image, bg = '#808080', borderwidth=0, command = paper)
    btn_scissors = Button(window_game, image = scissors_image, bg = '#808080', borderwidth=0, command = scissors)                      
    btn_stop = Button(window_game, text = 'Стоп', font = ('Comfortaa'), bg = '#1E90FF', command = stop_res)   
    btn_shop = Button(window_game, image = shop_image, bg = '#1E90FF', command = stop_shop)   
    btn_plus = Button(window_game, text = '+', font = ('Comfortaa'), bg = '#1E90FF', command = plus)   
    btn_minus = Button(window_game, text = '-', font = ('Comfortaa'), bg = '#1E90FF', command = minus)   
    btn_no_bet = Button(window_game, text = '0', font = ('Comforta'), bg = '#1E90FF', command= no_bet)

    lbl_comp_choice = Label(window_game, image = rock_image, bg = '#808080')
    lbl_per_choice = Label(window_game, image = rock_image, bg = '#808080')
    lbl_score = Label(window_game, text = 'Счёт', bg = '#1E90FF', font = ('Comfortaa'))    
    lbl_bet = Label(window_game, text = ('Cтавка', bet), bg = '#1E90FF', font = ('Comfortaa', 13))    
    lbl_balance = Label(window_game, text = ('Баланс', balance), bg = '#1E90FF', font = ('Comfortaa'))
    lbl_streak = Label(window_game, text = ('Стрик', streak), bg = '#1E90FF', font = ('Comfortaa'))

    btn_rock.place(relx = 0.111111, rely = 0.533333, relwidth = 0.222222, relheight = 0.266666, )   
    btn_paper.place(relx = 0.666666, rely = 0.533333, relwidth = 0.222222, relheight = 0.266666, )   
    btn_scissors.place(relx = 0.388888, rely = 0.533333, relwidth = 0.222222, relheight = 0.266666, )    
    btn_stop.place(relx = 0.333333, rely = 0.866666, relwidth = 0.333333, relheight = 0.133333, )
    btn_shop.place(relheight = 0.133333, relwidth = 0.111111 )   
    btn_plus.place(relx = 0.944444, rely = 0.066666, relheight = 0.066666, relwidth = 0.055555, )
    btn_minus.place(relx = 0.666666, rely = 0.066666, relheight = 0.066666, relwidth = 0.055555, )  
    btn_no_bet.place(relx = 0.666666, relheight = 0.066666, relwidth = 0.055555, )
    
    lbl_comp_choice.place(relx = 0.611111, rely = 0.166666, relwidth = 0.222222, relheight = 0.266666, )   
    lbl_per_choice.place(relx = 0.2, rely = 0.166666, relwidth = 0.222222, relheight = 0.266666, )    
    lbl_score.place(relx = 0.388888, relwidth = 0.222222, relheight = 0.066666, )   
    lbl_bet.place(relx = 0.722222, rely = 0.066666, relwidth= 0.222222, relheight = 0.066666)
    lbl_balance.place(relx = 0.722222, relwidth = 0.277777, relheight = 0.066666)
    lbl_streak.place(relx = 0.388888, rely = 0.08, relheight= 0.066666, relwidth = 0.222222)

    window_game.mainloop()

def shop():
    def pack_1():
        global cur_pack
        cur_pack = 'pack1'
        shop_win.destroy()
        game_win()

    def pack_2():
        global pack2_bool, balance, cur_pack

        if pack2_bool == False and balance > 500:
            balance -= 500
            pack2_bool = True
            cur_pack = 'pack2'
            shop_win.destroy()
            game_win()
        elif pack2_bool == True:
            cur_pack = 'pack2'
            shop_win.destroy()
            game_win()
        else:
            shop_win.destroy()
            game_win()

    def pack_3():
        global pack3_bool, balance, cur_pack

        if pack3_bool == False and balance > 1000:
            balance -= 1000
            pack3_bool = True
            cur_pack = 'pack3'
            shop_win.destroy()
            game_win()
        elif pack3_bool == True:
            cur_pack = 'pack3'
            shop_win.destroy()
            game_win()
        else:
            shop_win.destroy()
            game_win()

    def pack_4():
        global pack4_bool, balance, cur_pack

        if pack4_bool == False and balance > 2000:
            balance -= 2000
            pack4_bool = True
            cur_pack = 'pack4'
            shop_win.destroy()
            game_win()
        elif pack4_bool == True:
            cur_pack = 'pack4'
            shop_win.destroy()
            game_win()
        else:
            shop_win.destroy()
            game_win()

    def pack_5():
        global pack5_bool, balance, cur_pack

        if pack5_bool == False and balance > 3000:
            balance -= 3000
            pack5_bool = True
            cur_pack = 'pack5'
            shop_win.destroy()
            game_win()
        elif pack5_bool == True:
            cur_pack = 'pack5'
            shop_win.destroy()
            game_win()
        else:
            shop_win.destroy()
            game_win()

    shop_win = Tk()
    shop_win.title('Магазин')
    shop_win.geometry('150x250')
    shop_win.iconbitmap('./apps/rock, paper, scissors/picture/icon_shop.ico')
    shop_win.config(bg = '#808080')
    shop_win.resizable(True, True)
    btn_pack1 = Button(shop_win, bg = '#1E90FF', command = pack_1, text = 'Первый пак')  
    btn_pack2 = Button(shop_win, bg = '#1E90FF', command = pack_2, text = 'Второй пак (500)')
    btn_pack3 = Button(shop_win, bg = '#1E90FF', command = pack_3, text = 'Третий пак (1000)')
    btn_pack4 = Button(shop_win, bg = '#1E90FF', command = pack_4, text = 'Четвёртый пак (2000)')
    btn_pack5 = Button(shop_win, bg = '#1E90FF', command = pack_5, text = 'Пятый пак (3000)')
    btn_pack1.place(relheight=0.2, relwidth=1)
    btn_pack2.place(rely = 0.2, relheight=0.2, relwidth=1)
    btn_pack3.place(rely = 0.4, relheight=0.2, relwidth=1)
    btn_pack4.place(rely = 0.6, relheight=0.2, relwidth=1)
    btn_pack5.place(rely = 0.8, relheight=0.2, relwidth=1)

def menu_win():
    def new_game():
        global score_per, score_comp, streak, bet, balance, pack2_bool, pack3_bool, pack4_bool, pack5_bool, cur_pack
        score_per = score_comp = streak =  0
        pack2_bool = pack3_bool = pack4_bool = pack5_bool = False
        balance = 1000
        bet  = 10
        cur_pack = ''
        window_result.destroy()
        game_win()

    def stop():
        window_result.destroy()

    window_result = Tk() #создаём окно
    window_result.title('Меню') #название
    window_result.iconbitmap('./apps/rock, paper, scissors/picture/icon_game.ico') #иконка окна
    window_result.configure(bg = '#808080')
    window_result.geometry('140x100+100+20') #750, 400 #где находится окно и размер
    window_result.resizable(False, False) #нельзя изменять размеры

    btn_new_game = Button(window_result, text = 'Новая игра!', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 2, command = new_game)
    btn_stop = Button(window_result, text = 'Выйти', font = ('Comfortaa'), width = 15, bg = '#1E90FF', height = 2, command= stop)

    btn_stop.pack()
    btn_new_game.pack(side = BOTTOM)

    window_result.mainloop()

score_per = 0
score_comp = 0
balance = 1000
bet = 10
streak = 0

pack2_bool = False
pack3_bool = False
pack4_bool = False
pack5_bool = False
bet_bool = False
test = True

cur_pack = ''

choice_pos = ('r', 's', 'p')

game_win()