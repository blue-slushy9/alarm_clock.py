import sched, time

#tz = pytz.timezone('US/Pacific')

#current_time = datetime.datetime.now(tz)

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off, either AM/PM or 2400 format is fine.")

alarm_time = input().lower()
print()

print("Do you want this alarm to go off every day, or just once?")

alarm_frequency = input().lower()
print()

#print(current_time)

# Define the alarm function

def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

# Create a scheduler object

scheduler = sched.scheduler(time.time, time.sleep)

# Schedule the function to run at specified time

alarm_list = []

if 'am' in alarm_time:
    for char in alarm_time:
        alarm_list.append(char)
    for char in 'am':
        alarm_list.remove(char)
    if len(alarm_list) == 1:
        alarm_time = time.strptime(f'0{alarm_list[0]}:00', '%H:%M')
        alarm_time = time.mktime(alarm_time)
        scheduler.enterabs(alarm_time, 1, alarm)




scheduler.run()
