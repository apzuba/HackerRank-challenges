# Sample Input: 08 05 2015

#Example of using the calendar module


import calendar

m, d, y = input().split()

day = calendar.weekday(int(y), int(m), int(d))

print(calendar.day_name[day].upper())
