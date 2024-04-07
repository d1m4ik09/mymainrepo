from random import *

def rand_ID():
    prom = ''
    prom += chr(randint(65, 91))
    for _ in range(10):        
        var = randint(48, 123)
        prom += chr(var)
    return prom


def inf_stud(number):
    numbers = [str(i) for i in range(1, 21)]
    if number in numbers:
        for _ in range(int(number)):
            print('Центр успеха')
            students.append(input('Имя: '))
            lessons.append(input('Курс: '))
            group.append(input("Группа: "))
            ID = rand_ID()           
            prom.append(ID)
            print()
            print('Ваш ID (Запомните его!!!):', ID)
    else:
        print('Некорректный ввод количества учеников')
        number = input('Число учеников(до 20):')
        inf_stud(number)


def inf(word):
    while word != 'ф':
        if word == 'д':
            num_stud = input('Число учеников(до 20):')
            inf_stud(num_stud)
        elif word == 'qwerty':
            print(* students, sep=', ')
        elif word in prom:
            print('Имя:', students[prom.index(word)])
            print('Курс:', lessons[prom.index(word)])
            print('Группа:', group[prom.index(word)])
        else:
            print('Данные не внесены')
        word = input('Ваш ID("ф"-закончить, "д"-дополнить): ')
        print()
    print('Готово')


prom = []
students = []
lessons = []
group = []

num_stud = input('Число учеников(до 20):')
inf_stud(num_stud)

init = input('ID ученика или ("ф"-закончить, "д"-дополнить): ')
inf(init)