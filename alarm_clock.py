import sched, time

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off. You may use the format 00:00AM or PM; military time is also acceptable, e.g. 18:00 for 06:00PM.")

alarm_time = input().lower()
print()

# print("Do you want this alarm to go off every day, or just once?")

# alarm_frequency = input().lower()
# print()

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

# Create a scheduler object where time.time is the current time, and time.sleep is
# how long Python should wait to run the program?
scheduler = sched.scheduler(time.time, time.sleep)

# Create a list we will use to manipulate the string time input in various ways;
alarm_list = []

# This if statement will cover AM times;
if len(alarm_time) == 7 and 'am' in alarm_time:
   
# Turn the string time input into a list in order to remove the 'AM';

# Loop through the string characters and add them to alarm_list one by one;
    for char in alarm_time:
        alarm_list.append(char)
   
# Remove the 'a' and 'm' from the list by looping through 'am' string;  
    for char in 'am':
        alarm_list.remove(char)

# Create a new string by joining the list elements, which is now only numbers;
    alarm_joined = (''.join(alarm_list))

# Converts the alarm_joined string into a time.struct_time object; strptime() parses the alarm_joined string
# and returns the time.struct_time object, which in turn represents the specified time, i.e. the input; the
# time.struct_time object contains the hour, minute, second, and other attributes of the specified time, which
# are then passed to the alarm_time2 variable;
    alarm_time2 = time.strptime(f'{alarm_joined}', '%H:%M')
    alarm_time2 = time.mktime(alarm_time2)
    scheduler.enterabs(alarm_time2, 1, alarm)

# This if statement will cover PM times;
elif len(alarm_time) == 7 and 'pm' in alarm_time:

# Turn the string time input into a list in order to remove the 'PM';

# Loop through the string characters and add them to alarm_list one by one;
    for char in alarm_time:
        alarm_list.append(char)

# Remove the 'p' and 'm' from the list by looping through 'pm' string;  
    for char in 'pm':
        alarm_list.remove(char)

# We need to add 12 hours to the first two digits for PM times, since Python doesn't understand AM/PM;

# Join the list that we created from the string input, turning it into a new string;
    alarm_first_two = (''.join(alarm_list[0]+alarm_list[1]))

# Cast the new string as an integer so we can add 12 to it, thereby converting it to military format; 
    military_format = int(alarm_first_two) + 12

# Revert back to string so we can loop through it in next step; 
    military_format = str(military_format)

# Loop through the new military time we created, as well as our original alarm list, and replace the alarm 
# list elements with our new military time digits;
    for x in range(len(military_format)):
        alarm_list[x] = military_format[x]

# Create a new string by joining the list elements, which consists of the military time digits;
    alarm_joined = (''.join(alarm_list))

# Converts the alarm_joined string into a time.struct_time object; strptime() parses the alarm_joined string
# and returns the time.struct_time object, which in turn represents the specified time, i.e. the input; the
# time.struct_time object contains the hour, minute, second, and other attributes of the specified time, which
# are then passed to the alarm_time2 variable;
    alarm_time2 = time.strptime(f'{alarm_joined}', '%H:%M')
    
# Converts the time.struct_time object into a Unix timestamp using the mktime() method, which returns a floating-
# point number that represents the Unix timestamp, which then gets assigned to the variable alarm_time2; 
    alarm_time2 = time.mktime(alarm_time2)
    
# Uses the enterabs() method to schedule a function call to our alarm function at a specific absolute time;
# sched.scheduler class provides event scheduler for Python; alarm_time2 is the time at which the function 
# alarm will be run, with a priority level of 1 (the lower the number, the higher the priority);
    scheduler.enterabs(alarm_time2, 1, alarm)


# This statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:
    alarm_time2 = time.strptime(f'{alarm_time}', '%H:%M')
    alarm_time2 = time.mktime(alarm_time2)
    scheduler.enterabs(alarm_time2, 1, alarm)

# This else statement will run when an invalid time format is entered, e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and enter a valid time format per the instructions.")

# Initiate the scheduler, which tells Python to run the 'alarm' function at the specified time (alarm_time2);
scheduler.run()
