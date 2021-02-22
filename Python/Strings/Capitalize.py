Question : https://www.hackerrank.com/challenges/capitalize/problem

Solution :
def solve(s):
    a=s.split(' ')
    return (' '.join((word.capitalize() for word in a)))
