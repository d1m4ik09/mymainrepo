a = int(input())
count = len(str(a))
sm = sum(int(i) for i in str(a))

avg = sm / count
count_fives = 0

print('средний балл:', round(avg, 2))

while avg < 4.6:
    sm += 5
    count += 1
    count_fives += 1
    avg = sm / count

print('Кол-во пятерок до 4.60 и выше:', count_fives)