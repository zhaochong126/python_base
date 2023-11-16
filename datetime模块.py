'''
year,month,day:年月日
isoweekday
weekday
isocalendar
strftime:给时间转换成字符串
'''
import time
from datetime import datetime
# d = datetime.date(2023,10,23)
# print(d.isoweekday())
# print(d.weekday())
# print(d.isocalendar())
# t=datetime.time(10,20,20,300000)
# print(t)

print(datetime.now())
print(datetime.now().strftime('%Y%M%D,%H:%M:%S'))
# a = datetime.datetime.now()
# print(a)