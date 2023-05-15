from datetime import datetime, timedelta
from time import sleep

print("This is an alarm clock app! Please enter the time you want for your\n"
        "alarm to ring. Please use the format 00:00AM or PM; military time is\n" 
        "also acceptable, e.g. 18:00 for 06:00PM.")

alarm_time = input().upper()
print()

# Since our if statements will compare the alarm_time to the current time, 
# we create a variable (now) to store the current time;
#now = datetime.now()

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

###############

# This function will convert the AM and military alarm_time user inputs into a
# datetime object, to be stored in the global variable alarm_time2;
# Note that a separate function will have to be defined for PM times;
def time_conversion(alarm_time):
    # Create a variable HH that will store the hours portion of the alarm time
    # as an integer;
    HH = int((alarm_time[0:2]))

    # Create a variable MM that will store the minutes portion of the alarm 
    # time as an integer; We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

    # Create an alarm_time2 global variable that will store the current 
    # datetime, then we use the replace() function to overwrite the hour and 
    # minutes with our target time (the alarm time per user input); 
    # using datetime ensures that the alarm will go off on the correct day, 
    # either today or tomorrow if the time has already passed today;
    global alarm_time2 
    alarm_time2 = datetime.now().replace(hour=HH, minute=MM)

###############

# Since the AM and military time formats both use identical code past the if 
# statements, we can define a function to use for both those cases; 
# We will define a separate function for the PM times, as those require some 
# manipulation to convert to military time;
def alarm_execution(alarm_time2):

    # Create a variable HH that will store the hours portion of the alarm time 
    # as an integer;
    #HH = int((alarm_time[0:2]))

    # Create a variable MM that will store the minutes portion of the alarm 
    # time as an integer; we skip over alarm_list[2] because that is the ':' ;
    #MM = int((alarm_time[3:5]))

    # Create an alarm_time2 variable that will store the current datetime, 
    # then we use the replace() function to overwrite the hour and minutes 
    # with our target time (the alarm time per user input); 
    # using datetime ensures that the alarm will go off on the correct day, 
    # either today or tomorrow if the time has already passed today;
    #alarm_time2 = datetime.now().replace(hour=HH, minute=MM)
    
    # Create a while loop that will constantly check the datetime.now, 
    # then assign it to the variable now; 
    while True:
        now = datetime.now()
    
        # Create an if statement inside of the while loop that will compare 
        # the now variable to the alarm time per user input; 
        # if the now variable matches or exceeds the alarm_time....
        if now >= alarm_time2:
            # Then the alarm function will run!           
            alarm()
            print()
            
            # Ask the user whether they want the alarm to go off again at the 
            # same time tomorrow; 
            print("Do you want this alarm to go off at the same time tomorrow?\n" 
                    "Please type 'yes' or 'y', 'no' or 'n'.")
            # Input can be yes or no, y or n; we use lower() so that it won't 
            # matter if they type in upper or lower case;            
            tomorrow = input().lower()
            print()

            # If user wants alarm to ring tomorrow, we use continue to skip 
            # the code below and proceed to next iteration of the while loop;
            if tomorrow == 'yes' or tomorrow == 'y':
                # However, we first have to adjust the day in the alarm_time2 
                # so that it matches the date tomorrow instead of today;
                # We use the timedelta method to add 1 day to the alarm_time2 
                # object, in which we previously stored the current month and day;
                alarm_time2 += timedelta(days=1)
                # Continue to next iteration of the while loop, this time with 
                # the date of the alarm time set to tomorrow;
                continue
            # If user doesn't want alarm to ring tomorrow, we use break to 
            # exit the loop;
            elif tomorrow == 'no' or tomorrow == 'n':
                break
            # We use this else statement in the case of invalid input to the 
            # tomorrow prompt, e.g. 'maybe';
            # the user would then need to rerun the program from the start;
            else:
                print("Invalid input, please rerun the program to set a new\n" 
                        "alarm.")
                break

        # Finally, insert sleep() method to add a 1-second pause between loop 
        # iterations, this helps conserve system resources;
        sleep(1)

####################

# This function will be used to delay the alarm, in the case that the 
# alarm_time (user input) has already passed or is right now; 
# the alarm will be delayed until tomorrow at the same time;
def alarm_delay(alarm_time2):
    #alarm_time2 = datetime.now().replace(hour=HH, minute=MM)
    alarm_time2 += timedelta(days=1)
    alarm_execution(alarm_time2)

####################

# This function will be used to convert any PM time inputs into 24-hour format,
# as Python does not understand AM/PM format; 
# all we need is the alarm_time, which is entered by the user;
def pm_time_conversion(alarm_time):
    # Cast first two digits in alarm time as integers so we can add 12;
    HH = int((alarm_time[0:2]))
    # Add 12;
    HH += 12
    # Recast first two digits as string so we can reinsert into original 
    # alarm_time string;
    HH = str(HH)
    # Cast original alarm_time string as list so we can replace first two 
    # digits;
    alarm_time_list = list(alarm_time)
    # Replace first two characters in string (first two digits) with new 
    # military time format;
    alarm_time_list[0:2] = HH
    # Join list back into a string we can pass the alarm_time argument to the 
    # alarm_execution function; 
    alarm_time = (''.join(alarm_time_list))

    # Finally, we nest the AM and military time_conversion function inside of
    # this one, as we still need to convert the alarm_time string into a
    # datetime object, i.e. alarm_time2;
    time_conversion(alarm_time)

    # Nest the alarm_execution function inside of pm_time_conversion with 
    # modified alarm_time as argument;
    #alarm_execution(alarm_time2)

#####################

# Define a function, delay_or_execute, which will be used to decide whether
# the alarm should be delayed until tomorrow (in the case that the alarm_time
# has already passed for today's date) or whether the alarm_execution function
# should run normally;
def delay_or_execute(alarm_time2):
    # Create a local variable, now, that will store the value of datetime.now()
    # for comparison to alarm_time2;
    now = datetime.now()
    # This if statement will apply if alarm_time2 is in the past or present; 
    if alarm_time2 <= now:
        print("You've entered a time that has already passed for today's date.\n"
                "The alarm will ring at the specified time tomorrow.")
        print()
        # The function alarm_delay will run, which simply delays the alarm to the 
        # same time tomorrow;
        alarm_delay(alarm_time2)
    # This if statement will apply if the alarm_time is in the future, 
    # ergo the alarm_execution function will run;
    elif alarm_time2 > now: 
        alarm_execution(alarm_time2)

#####################

# This if statement will cover AM times, the if statement is there to ensure 
# the format for the alarm time entered is correct;
if len(alarm_time) == 7 and 'AM' in alarm_time:
    # Run the time_conversion function to convert the alarm_time into a 
    # datetime object, which then gets assigned to the global variable 
    # alarm_time2;
    time_conversion(alarm_time)

    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    delay_or_execute(alarm_time2)

    # Create a local variable, now, that will store the value of datetime.now()
    # for comparison to alarm_time2;
    #now = datetime.now()
    # This if statement will apply if alarm_time2 is in the past or present; 
    #if alarm_time2 <= now:
    #    print("You've entered a time that has already passed for today's date.\n"
    #            "The alarm will ring at the specified time tomorrow.")
    #    print()
        # The function alarm_delay will run, which simply delays the alarm to the 
        # same time tomorrow;
    #    alarm_delay(alarm_time2)
    # This if statement will apply if the alarm_time is in the future, 
    # ergo the alarm_execution function will run;
    #elif alarm_time2 > now: 
    #    alarm_execution(alarm_time2)
    
######################

# This if statement will cover PM times;
elif len(alarm_time) == 7 and 'PM' in alarm_time:
    # Call PM time conversion function to convert alarm_time into military 
    # format; the AM and military time_conversion function is also nested
    # inside of pm_time_conversion, so that the converted PM alarm_time can be
    # converted into the datetime object, alarm_time2;
    pm_time_conversion(alarm_time)
   
    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    delay_or_execute(alarm_time2)

    # Create a variable, now, that will store the value of datetime.now() for 
    # comparison to alarm_time2;
    #now = datetime.now()
    # This if statement will apply if alarm_time2 is in the past or present; 
    # the function alarm_delay will run, which simply delays the alarm to the 
    # same time tomorrow;
    #if alarm_time <= now:
    #    alarm_delay(alarm_time2)
    # This if statement will apply if the alarm_time is in the future, ergo 
    # the alarm_execution function will run;
    #elif alarm_time2 > now: 
    #    alarm_execution(alarm_time2)
    
##################

# This statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:
    # Run the time_conversion function to convert the alarm_time string into a
    # datetime object, assigned to the global variable alarm_time2;
    time_conversion(alarm_time)
    
    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    delay_or_execute(alarm_time2)

    # Create a variable, now, that will store the value of datetime.now() for 
    # comparison to alarm_time2;
    #now = datetime.now()
    # This if statement will apply if alarm_time2 is in the past or present; 
    # the function alarm_delay will run, which simply delays the alarm to the 
    # same time tomorrow;
    #if alarm_time2 <= now:
    #    alarm_delay(alarm_time2)
    # This if statement will apply if the alarm_time is in the future, ergo the
    # alarm_execution function will run;
    #elif alarm_time2 > now: 
    #    alarm_execution(alarm_time2)

##################

# This else statement will run when an invalid time format is entered, 
# e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and\n" 
    "enter a valid time format per the instructions.")
