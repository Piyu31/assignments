import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1995,5,31)
print(birthday)

day_since_birth = (today - birthday).days
print(day_since_birth)

tdelta = datetime.timedelta(days =10)
print(today + tdelta)

print(today.day)
print(today.weekday())# monday = 0, sunday = 6


print(datetime.time(7, 2, 20, 15))
print(datetime.datetime.today())


# 10 hours to current time day
hour_delta = datetime.timedelta(hours =10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Us/Pacific'))
print(datetime_pacific)


#for tz in pytz.all_timezones:
#	print(tz)


#string formatting with dates
#2010-03-09 -> March 9,2019
#strftime- string formating time
print(datetime_pacific.strftime('%B %d,%Y'))

# March 09,2019--> datetime(2019,3,9)
#strptime- string parshing time
datetime_thing = datetime.datetime.strptime('March 09,2019','%B %d,%Y')
print(repr(datetime_thing))