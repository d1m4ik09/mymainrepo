from random import *

list = []
target = randint(1, 50)
ln = int(input('Кол-во символов: '))
n = int(input('Диапозон до: '))
for i in range(ln):
    list.append(randint(1, n))
list.sort()
print(list)