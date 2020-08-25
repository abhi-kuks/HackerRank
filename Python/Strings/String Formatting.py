Question : https://www.hackerrank.com/challenges/python-string-formatting/problem


Solution


def print_formatted(number):

    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i , width=width))
        
        
        
 Some Explaination
         # Padding
        # '{:10}'.format('test') where 10 is the amount to pad by
        # We inject the width for the number to pad by
        
        # Conversion
        # {:d} is integer, {:o} is octal, {:X} is hexadecimal, {:b} is binary       
        
