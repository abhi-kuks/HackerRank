Question : https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    line_split = line.split(" ")
    line_join = "-".join(line_split)
    return line_join


