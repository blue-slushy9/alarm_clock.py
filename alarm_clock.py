import sched, time

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off. You may use the format 00:00AM or PM; military time is also acceptable, e.g. 18:00 for 06:00PM.")

alarm_time = input().lower()
print()

print("Do you want this alarm to go off every day, or just once?")

alarm_frequency = input().lower()
print()

# Define the alarm function

def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

# Create a scheduler object

scheduler = sched.scheduler(time.time, time.sleep)

# Schedule the function to run at specified time

alarm_list = []

if len(alarm_time) == 7 and 'am' in alarm_time:
   
    for char in alarm_time:
        alarm_list.append(char)
   
    for char in 'am':
        alarm_list.remove(char)
   
    if len(alarm_list) == 1:
        alarm_time2 = time.strptime(f'0{alarm_list[0]}:00', '%H:%M')
        alarm_time2 = time.mktime(alarm_time2)
        scheduler.enterabs(alarm_time2, 1, alarm)

    elif len(alarm_list) == 2:
        alarm_time2 = time.strptime(f'{alarm_list[0]}{alarm_list[1]}:00', '%H:%M')
        alarm_time2 = time.mktime(alarm_time2)
        scheduler.enterabs(alarm_time2, 1, alarm)
            
elif len(alarm_time) == 7 and 'pm' in alarm_time:
    
    for char in alarm_time:
        alarm_list.append(char)
   
    for char in 'pm':
        alarm_list.remove(char)
    alarm_first_two = (''.join(alarm_list[0]+alarm_list[1]))
    military_format = int(alarm_first_two) + 12
    military_format = str(military_format)
   
    for x in range(len(military_format)):
        alarm_list[x] = military_format[x]
    alarm_joined = (''.join(alarm_list))    
    alarm_time2 = time.strptime(f'{alarm_joined}', '%H:%M')
    alarm_time2 = time.mktime(alarm_time2)
    scheduler.enterabs(alarm_time2, 1, alarm)

elif len(alarm_time) == 5 and ':' in alarm_time:
    alarm_time2 = time.strptime(f'{alarm_time}', '%H:%M')
    alarm_time2 = time.mktime(alarm_time2)
    scheduler.enterabs(alarm_time2, 1, alarm)

else:
    print("This is an invalid time format, please run the program again and enter a valid time format per the instructions.")

scheduler.run()
