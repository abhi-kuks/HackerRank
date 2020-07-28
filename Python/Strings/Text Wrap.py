Question : https://www.hackerrank.com/challenges/text-wrap/

import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string , max_width)
    return '\n'.join(a)
