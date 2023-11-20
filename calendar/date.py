import datetime
import calendar

day1 = datetime.date(2023, 11, 19)
day2 = datetime.datetime(2023, 11, 20, 14, 8, 30)
print(datetime.datetime.now())
print(datetime.date.today())

day3 = datetime.date(2022, 11, 19)

diff = day1 - day3
print(diff)

date_plus = datetime.timedelta(days=100)
print(day3 + date_plus)

print(calendar.isleap(2020))
print(calendar.isleap(2022))

print(calendar.leapdays(1990, 2022))
print(calendar.weekday(2023, 11, 20))
# print(calendar.calendar(2023))

tmpTime_str = '2023-11-08 16:04:30'
tmpTime = datetime.datetime.strptime(tmpTime_str, '%Y-%m-%d %H:%M:%S')
print(type(tmpTime))

now = datetime.datetime.now()
print(now)
now_str = now.strftime('%Y-%m-%d')
print(type(now_str))
print(now_str)
now_str2 = now.strftime('%H:%M:%S')
print(type(now_str2))
print(now_str2)

from dateutil.parser import parse

date = '2023-11-20'
parsed = parse(date)
print(parsed)
print(parse("Oct 15, 2022 04:05:32 PM"))

log = 'INFO 2022-01-01T00:00:01 Happy new year, human.'
print(parse(log, fuzzy=True))

import time

print(time.time())
print(time.ctime())

print('1초 대기 시작')
time.sleep(1)
print('대기 끝')

start = time.time()

for i in range(5):
    time.sleep(1)
    print('반복 회수', i + 1)

end = time.time()

print('경과 시간은 {}초 입니다'.format(end - start))
