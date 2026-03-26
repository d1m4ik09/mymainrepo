goal = float(input('Цель -->'))
grades = int(input('Ваши оценки -->'))

count = len(str(grades))
sm = sum(int(i) for i in str(grades))
avg = sm / count
fives = 0

print(f'средний балл: {avg}')

while avg < goal:
    count += 1
    sm += 5
    fives += 1
    avg = sm / count

print(f'Кол-во пятерок до {goal} и выше: {fives}')