def find_all_divisors(num):
    div = []

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            div.append(i)

    return sorted(set(div))

print(find_all_divisors(256))