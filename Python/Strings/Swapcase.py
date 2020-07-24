Question : https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    t = ''
    for l in s:
        if l == l.upper():
            t += l.lower()
        elif l== l.lower():
            t += l.upper()
    return t
