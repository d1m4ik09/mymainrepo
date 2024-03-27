from random import *

list = []
target = randint(1, 50)
for i in range(15):
    list.append(randint(1, 50))
list.sort()
print(list)