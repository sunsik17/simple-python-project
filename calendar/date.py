import datetime

day1 = datetime.date(2023, 11, 19)
day2 = datetime.datetime(2023, 11, 20, 14, 8, 30)
print(datetime.datetime.now())
print(datetime.date.today())

day3 = datetime.date(2022, 11, 19)

diff = day1 - day3
print(diff)

date_plus = datetime.timedelta(days=100)
print(day3 + date_plus)