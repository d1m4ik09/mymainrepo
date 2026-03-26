def romanToInt(s: str) -> int:
    roman = {'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000
            }
    
    ind = -1
    ans = 0

    while - ind != len(s):
        if roman[s[ind - 1]] < roman[s[ind]]:
            loc = roman[s[ind]]
            while roman[s[ind - 1]] < roman[s[ind]]:
                loc -= roman[s[ind - 1]]
                ind -= 1
            ind -= 1
            ans += loc

    
    return ans

print(romanToInt(input()))