# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 2002-02-22 09:45:23

from datetime import datetime

def one_from_two(some_date, some_time):
    year = some_date.year
    month = some_date.month
    day = some_date.day

    hour = some_time.hour
    minute = some_time.minute
    second = some_time.second

    return datetime(year, month, day, hour, minute, second)

