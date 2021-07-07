from datetime import datetime, date, time, timedelta

d1 = date(2021, 6, 4)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(15, 11, 25)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

print(date.today())
print(datetime.now())

dt = datetime(2021, 6, 4, 15, 11, 25)
print(dt)

#Parse date in str
dt = datetime.strptime("12:23:2000", "%m:%d:%Y")
print(dt)

dt = datetime.strptime("12#23#2000 15|40", "%m#%d#%Y %H|%M")
print(dt)

dt = datetime.strptime("2002-4-12", "%Y-%m-%d")
print(dt)

print()

now = datetime.now()
print(now.strftime("%y-%B-%d число (%A)"))
