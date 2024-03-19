def is_password_good(password):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if len(password) == 8:
        count1 += 1
    for i in password:
        if i.islower():
            count2 += 1
        if i.isupper():
            count3 += 1
        if i.isdigit():
            count4 += 1
    if (count1, count2, count3, count4) >= 1:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))