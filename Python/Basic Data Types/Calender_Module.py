Question:https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
def findDay(date):
    m,d,y = [int(i) for i in date.split(" ")]
    day_no = calendar.weekday(y,m,d)
    days = ['MONDAY', 'TUEDAY' , 'WEDNESDAY' , 'THURSDAY ', 'FRIDAY' , 'SATURDAY' , 'SUNDAY']
    return days[day_no]

date = input()
print(findDay(date))
