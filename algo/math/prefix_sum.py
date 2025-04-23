def prefix_sum(a: list) -> list[int]:
    s = [0]

    for i in range(len(a)):
        s.append(s[i] + a[i])
    
    return s