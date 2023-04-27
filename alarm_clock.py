import pytz, datetime

tz = pytz.timezone('US/Pacific')

current_time = datetime.datetime.now(tz)

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off, either AM/PM or 2400 format is fine.")

alarm_time = input()
print()

print("Do you want this alarm to go off every day, or just once?")
print()

print(current_time)
