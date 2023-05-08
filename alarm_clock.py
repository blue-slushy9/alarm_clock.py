import datetime
from datetime import timedelta

print("This is an alarm clock app! Please enter the time you wish for your alarm to go off. You may use the format 00:00AM or PM; military time is also acceptable, e.g. 18:00 for 06:00PM.")

alarm_time = input().upper()
print()

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

# Since the AM and military time formats are both using identical code, we can define a function to use
# for both those cases;

def alarm_execution(alarm_time):

    # Create a variable HH that will store the hours portion of the alarm time as an integer;
    HH = int((alarm_time[0:2]))

    # Create a variable MM that will store the minutes portion of the alarm time as an integer;
    # We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

    # Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
    # overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
    # timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0)# + timedelta(days=0)
    
    # Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
    while True:
        now = datetime.datetime.now()
    
    # Create an if statement inside of the while loop that will compare the now variable to the alarm time per
    # user input; if the now variable matches or exceeds the datetime of the input alarm time...
        if now >= alarm_time2:
            # Then the alarm function will run!           
            alarm()
            print()
            
            # Ask the user whether they want the alarm to go off again at the same time tomorrow; 
            print("Do you want this alarm to go off at the same time tomorrow? Please type 'yes' or 'y', 'no' or 'n'.")
            
            # Input can be yes or no, y or n; we use lower() so that it won't matter if they type in upper or lower case;            
            tomorrow = input().lower()
            # If user wants alarm to ring tomorrow, we use continue to skip the code below and proceed to next iteration of the while loop;
            if tomorrow == 'yes' or tomorrow == 'y':
                # However, we first have to adjust the day in the alarm_time2 so that it matches the date tomorrow instead of today;
                # We use the timedelta method to add 1 day to the alarm_time2, in which we previously stored the current month and day;
                alarm_time2 = alarm_time2 + timedelta(days=1)
                # Continue to next iteration of the while loop, this time with the date of the alarm time set to tomorrow;
                continue
            # If user doesn't want alarm to ring tomorrow, we use break to exit the loop;
            elif tomorrow == 'no' or tomorrow == 'n':
                break
            # We use this else statement in the case of invalid input, e.g. 'maybe'; the user will need to rerun the program from the start;
            else:
                print("Invalid input, please rerun the program to set a new alarm.")
                break

#####################

# This if statement will cover AM times, the if statement is there to ensure the format for the 
# alarm time entered is correct;
if len(alarm_time) == 7 and 'AM' in alarm_time:
    alarm_execution(alarm_time)

# Create a variable HH that will store the hours portion of the alarm time as an integer;
#    HH = int((alarm_time[0:2]))
    
# Create a variable MM that will store the minutes portion of the alarm time as an integer;
# We skip over alarm_list[2] because that is the ':' ;
#    MM = int((alarm_time[3:5]))

# Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
# overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
# timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
#    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0)# + timedelta(days=0)
    
# Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
#    while True:
#        now = datetime.datetime.now()
# Create an if statement inside of the while loop that will compare the now variable to the alarm time per
# user input; if the now variable matches or exceeds the datetime of the input alarm time...
#        if now >= alarm_time2:
# Then the alarm function will run!           
#            alarm()
#            print()
# Ask the user whether they want the alarm to go off again at the same time tomorrow; 
#            print("Do you want this alarm to go off at the same time tomorrow? Please type 'yes' or 'y', 'no' or 'n'.")
# Input can be yes or no, y or n; we use lower() so that it won't matter if they type in upper or lower case;            
#            tomorrow = input().lower()
# If user wants alarm to ring tomorrow, we use continue to skip the code below and proceed to next iteration of the while loop;
#            if tomorrow == 'yes' or tomorrow == 'y':
#                continue
# If user doesn't want alarm to ring tomorrow, we use break to exit the loop;
#            elif tomorrow == 'no' or tomorrow == 'n':
#                break

######################

# This if statement will cover PM times;
elif len(alarm_time) == 7 and 'PM' in alarm_time:

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
    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0)# + timedelta(days=0)

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


# This statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:
    alarm_execution(alarm_time)

# Create a variable HH that will store the hours portion of the alarm time as an integer, cast it as an integer
# and then pass it to the replace() function;
#    HH = int((alarm_time[0:2]))

# Create a variable MM that will store the minutes portion of the alarm time as an integer;
# We skip over alarm_list[2] because that is the ':' ;
#    MM = int((alarm_time[3:5]))

# Create an alarm_time2 variable that will store the current datetime; then we use the replace() function to 
# overwrite the hour, minutes, etc. with our target time (the alarm time per user input); then we use the 
# timedelta class to add x days to our alarm_time2, e.g. if we add 1 day the alarm will go off tomorrow;
#    alarm_time2 = datetime.datetime.now().replace(hour=HH, minute=MM, second=0, microsecond=0)# + timedelta(days=0)

# Create a while loop that will constantly check the datetime.now, then assign it to the variable now; 
#    while True:
#        now = datetime.datetime.now()
# Create an if statement inside of the while loop that will compare the now variable to the alarm time per
# user input; if the now variable matches or exceeds the datetime of the input alarm time...
#        if now >= alarm_time2:
# Then the alarm function will run!           
#            alarm()
# Then we break the loop because the alarm has already sounded;
#            break

##################

# This else statement will run when an invalid time format is entered, e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and enter a valid time format per the instructions.")
