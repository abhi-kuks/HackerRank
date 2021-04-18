Question
https://www.hackerrank.com/challenges/collections-counter/problem

Solution
from collections import Counter

no_of_shoes = int(input())

shoe_sizes = Counter(map(int,input().split()))

no_of_customers = int(input())

revenue = 0
for x in range((no_of_customers)):
    size , price = map(int , input().split())
    if shoe_sizes[size]:
        revenue +=price
        shoe_sizes[size] -=1
    
print(revenue)
