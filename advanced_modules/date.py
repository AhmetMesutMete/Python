# dir() function returns all properties and methods of the specified object.
# import datetime  

# r = dir(datetime)

# print(r)

##############################
from datetime import datetime
from datetime import timedelta
# from datetime import time
# from datetime import date

Info = datetime.now() # Can be written as "Info = datetime.today()" also.
# result2 = datetime.date(Info)
# result3 = datetime.time(Info)

# print(Info.year)
# print(Info.month)
# print(Info.day)
# print(Info.hour)
# print(Info.minute)
# print(Info.second)

result = datetime.ctime(Info) #It gives a little bit more descriptive information
result = datetime.strftime(Info, '%Y') #Only year
result = datetime.strftime(Info, '%X')   #Only time info
result = datetime.strftime(Info, '%d') #Only day
result = datetime.strftime(Info, '%A') #Only day in string format
result = datetime.strftime(Info, '%B') #Only month in string format
result = datetime.strftime(Info, '%Y %B %A') 

# t = '10 August 2020'

# day, month, year = t.split()
# print(day)
# print(month)
# print(year)

# print(result)

t = '14 February 2000 hour 14:42:20'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

result = result.year

birthday = datetime(1974, 1, 10)

# result = timestamp(birthday) #second
# result = datetime.fromtimestamp(result) #second to datetime

result = Info -birthday #timedelta

# result = result.days
# result = result.seconds
result = result.microseconds

# result = Info + timedelta(days = 30)
# result = Info + timedelta(days = 360, minutes = 91)

result = Info - timedelta(days = 7)
print(result)