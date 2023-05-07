import datetime
from datetime import timedelta

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off. You may use the format 00:00AM or PM; military time is also acceptable, e.g. 18:00 for 06:00PM.")

alarm_time = input().upper()
print()

# print("Do you want this alarm to go off every day, or just once?")

# alarm_frequency = input().lower()
# print()

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

# Create a function that will get you the current time in seconds (we need it in seconds
# in order to pass it to the scheduler a few lines down); 1970 is when the current epoch 
# began, so we subtract it from the datetimenow because Python only counts time FROM 1970;
# then we use the total_seconds() method to convert this elapsed time to seconds;
#def current_time():
#    return (datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()

# Create a scheduler object where current_time is the current time in seconds, and time.sleep is
# how long Python should wait to run the program;
#scheduler = sched.scheduler(current_time, time.sleep)

# Create a list we will use to manipulate the string time input in various ways;
#alarm_list = []

# This if statement will cover AM times, the if statement is there to ensure the format for the 
# alarm time entered is correct;
if len(alarm_time) == 7 and 'AM' in alarm_time:
   
# Turn the string time input into a list in order to remove the 'AM';

# Loop through the string characters and add them to alarm_list one by one;
#    for char in alarm_time:
#        alarm_list.append(char)
   
# Remove the 'A' and 'M' from the list by looping through 'AM' string;  
#    for char in 'AM':
#        alarm_list.remove(char)

# Create a variable HH that will store the hours portion of the alarm time as an integer;
    HH = int((alarm_time[0:2]))
    
# Create a variable MM that will store the minutes portion of the alarm time as an integer;
# We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

# Create a new string by joining the list elements, which is now only numbers;
#    alarm_joined = (''.join(alarm_list))

# Converts the alarm_joined string into a time.struct_time object; strptime() parses the alarm_joined string
# and returns the time.struct_time object, which in turn represents the specified time, i.e. the input; the
# time.struct_time object contains the hour, minute, second, and other attributes of the specified time, which
# are then passed to the alarm_time2 variable;

# Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
# overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
# timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0) + timedelta(days=0)
    
# Create a datetime variable that will store the current date and time;
#    datetime_var = datetime.datetime.now()
    
# timetuple() method converts our alarm_time2 variable into a time.struct_time object;
#    time_tuple = alarm_time2.timetuple()
    
# mktime() method converts the time.struct_time object into a Unix timestamp, a floating point number equal to 
# the seconds that have passed since the current epoch began to whatever endtime we specify, in this case the 
# the alarm time (but we use alarm_time2 because that's the one that's in the correct format);
#    alarm_time2 = time.mktime(time_tuple)

# Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
    while True:
        now = datetime.datetime.now()
# Create an if statement inside of the while loop that will compare the now variable to the alarm time per
# user input; if the now variable matches or exceeds the datetime of the input alarm time...
        if now >= alarm_time2:
# Then the alarm function will run!           
            alarm()
# Then we break the loop because the alarm has already sounded;
            break

# Uses the enterabs() method to schedule a function call to our alarm function at a specific absolute time;
# sched.scheduler class provides event scheduling for Python; alarm_time2 is the time at which the function 
# alarm will be run, with a priority level of 1 (the lower the number, the higher the priority);
#    scheduler.enterabs(alarm_time2, 1, alarm)

# This if statement will cover PM times;
elif len(alarm_time) == 7 and 'PM' in alarm_time:

# Turn the string time input into a list in order to remove the 'PM';

# Loop through the string characters and add them to alarm_list one by one;
#    for char in alarm_time:
#        alarm_list.append(char)

# Remove the 'P' and 'M' from the list by looping through 'PM' string;  
#    for char in 'PM':
#        alarm_list.remove(char)

# We need to add 12 hours to the first two digits for PM times, since Python doesn't understand AM/PM;

# Join the list that we created from the string input, turning it into a new string;
#    alarm_first_two = (''.join(alarm_list[0]+alarm_list[1]))

# Create a variable HH that will store the hours portion of the alarm time as an integer, and cast it as an
# integer so we can add 12 to it (military format) and pass it to the replace() function;
    HH = int((alarm_time[0:2]))

# Add 12 to HH, thereby converting it to military format; 
    military_HH = (HH + 12)

# Create a variable MM that will store the minutes portion of the alarm time as an integer;
# We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

# Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
# overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
# timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0) + timedelta(days=0)

# Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
    while True:
        now = datetime.datetime.now()
# Create an if statement inside of the while loop that will compare the now variable to the alarm time per
# user input; if the now variable matches or exceeds the datetime of the input alarm time...
        if now >= alarm_time2:
# Then the alarm function will run!           
            alarm()
# Then we break the loop because the alarm has already sounded;
            break

# timetuple() method converts our alarm_time2 variable into a time.struct_time object;
#    time_tuple = alarm_time2.timetuple()

# mktime() method converts the time.struct_time object into a Unix timestamp, a floating point number equal to 
# the seconds that have passed since the current epoch began to whatever endtime we specify, in this case the 
# the alarm time (but we use alarm_time2 because that's the one that's in the correct format);
#    alarm_time2 = time.mktime(time_tuple)

# Revert back to string so we can loop through it in next step; 
#    military_format = str(military_format)

# Loop through the new military time we created, as well as our original alarm list, and replace the alarm 
# list elements with our new military time digits;
#    for x in range(len(military_format)):
#        alarm_list[x] = military_format[x]

# Create a new string by joining the list elements, which consists of the military time digits;
#    alarm_joined = (''.join(alarm_list))

# Converts the alarm_joined string into a time.struct_time object; strptime() parses the alarm_joined string
# and returns the time.struct_time object, which in turn represents the specified time, i.e. the input; the
# time.struct_time object contains the hour, minute, second, and other attributes of the specified time, which
# are then passed to the alarm_time2 variable;
#    alarm_time2 = time.strptime(f'{alarm_joined}', '%H:%M')
    
# Converts the time.struct_time object into a Unix timestamp using the mktime() method, which returns a floating-
# point number that represents the Unix timestamp, which then gets assigned to the variable alarm_time2; 
#    alarm_time2 = time.mktime(alarm_time2)
    
# Uses the enterabs() method to schedule a function call to our alarm function at a specific absolute time;
# sched.scheduler class provides event scheduler for Python; alarm_time2 is the time at which the function 
# alarm will be run, with a priority level of 1 (the lower the number, the higher the priority);
#    scheduler.enterabs(alarm_time2, 1, alarm)

# This statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:

# Create a variable HH that will store the hours portion of the alarm time as an integer, cast it as an integer
# and then pass it to the replace() function;
    HH = int((alarm_time[0:2]))

# Create a variable MM that will store the minutes portion of the alarm time as an integer;
# We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

# Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
# overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
# timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0) + timedelta(days=0)

#    alarm_time2 = time.strptime(f'{alarm_time}', '%H:%M')
#    alarm_time2 = time.mktime(alarm_time2)
#    scheduler.enterabs(alarm_time2, 1, alarm)

# Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
    while True:
        now = datetime.datetime.now()
# Create an if statement inside of the while loop that will compare the now variable to the alarm time per
# user input; if the now variable matches or exceeds the datetime of the input alarm time...
        if now >= alarm_time2:
# Then the alarm function will run!           
            alarm()
# Then we break the loop because the alarm has already sounded;
            break

# This else statement will run when an invalid time format is entered, e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and enter a valid time format per the instructions.")

# Initiate the scheduler, which tells Python to run the 'alarm' function at the specified time (alarm_time2);
#scheduler.run()
