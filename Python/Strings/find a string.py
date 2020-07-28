Question :https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    counter =0
    l=[]
    s = len(string)
    sb = len(sub_string)
    for i in range(0 ,s):

        a = string[i:i+sb]
        if len(a) == sb:
            l.append(a)
    for x in l:
        if x == sub_string:
            counter+=1
    return counter
