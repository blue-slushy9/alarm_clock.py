from datetime import datetime, timedelta
from time import sleep

########### PROGRAM INTRO AND USER INPUT

# Throughout this code, I use many print() statements to enhance legibility in 
# the terminal;
print()
print("This is an alarm clock app! Please enter the time you want for your\n"
        "alarm to ring. Please use the format 00:00AM or PM; military time is\n" 
        "also acceptable, e.g. 18:00 for 06:00PM.")
print()

# Throughout this code, I alse use many lower() and upper() functions to
# control for user input, e.g. below;
alarm_time = input().upper()
print()

############### TIME CONVERSION FUNCTION, MILITARY FORMAT

# This function will convert military alarm_time user inputs into a
# datetime object, to be stored in the global variable alarm_time2;
# note that separate functions will have to be defined for AM and PM times;
def time_conversion(alarm_time):
    # Create a variable HH that will store the hours portion of the alarm time
    # as an integer;
    HH = int((alarm_time[0:2]))

    # Create a variable MM that will store the minutes portion of the alarm 
    # time as an integer; we skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

    # Create an alarm_time2 variable that will store the current 
    # datetime, then we use the replace() function to overwrite the hour and 
    # minutes with our target time (the alarm time per user input); 
    # using datetime ensures that the alarm will go off on the correct day, 
    # either today or tomorrow if the time has already passed today;
    alarm_time2 = datetime.now().replace(hour=HH, minute=MM)

    # Add a return statement so that other functions can receive alarm_time2;
    return alarm_time2

############### ALARM FUNCTION

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    # The original alarm_time, as entered by the user (except for AM/PM
    # altered by the upper() function) will appear as part of the alarm
    # output;
    print(f"Ring! It's {alarm_time}, time to wake up!")

####################### SET_ALARM FUNCTION BLOCK 

# This function will be used to set the alarm; it takes the datetime object, 
# alarm_time2, as its argument;
def set_alarm(alarm_time2):

    # Create a while loop that will continuously check the datetime.now(), 
    # then assign it to the variable now; 
    while True:
        now = datetime.now()
    
        # Create an if statement inside of the while loop that will compare 
        # the now variable to the alarm_time2 datetime object; 
        # if the now variable matches or exceeds the alarm_time....
        if now >= alarm_time2:
            # then the alarm function will run, i.e. the alarm will ring!           
            alarm()
            print()

############################ SNOOZE BLOCK

            # After alarm rings, ask the user whether they would like to hit 
            # snooze;
            print("Would you like to hit snooze? [Y/N]")
            print()
            # Input can be Y or N, we use lower() so that it won't 
            # matter if they type in upper or lower case;            
            snooze = input().lower()
            print()
            
            # If the user says yes to the first snooze...
            if snooze == 'y':
                # We add 10 minutes to alarm_time2, i.e. the alarm will go off
                # again in 10 minutes;
                alarm_time2 += timedelta(minutes=10)

################# SET_SNOOZE FUNCTION
                
                # Create variable, n, which will be the snooze counter,
                # which will keep track of how many times user has hit snooze;
                n = 1
                # Create snooze_again variable and set it equal to 'y' to
                # start, which will be used to keep the snooze loop running,
                # or to exit the loop if user says no;
                snooze_again = 'y'

                # Union is used to specify that the function will return more
                # than one type of value, the values are defined below;
                from typing import Union
                
                # Define the set_snooze function, which is the snooze alarm
                # equivalent of the set_alarm function, i.e. it engages the
                # snooze alarm feature, which makes the alarm go off in ten
                # minutes;
                def set_snooze(
                    n: int,
                    alarm_time2: object,
                    snooze_again: str
                ) -> Union[int, object, str]:

                    # Create while loop that will run for as long as 
                    # snooze_again == 'y';
                    while snooze_again == 'y':
                        # We need to run datetime.now() in this loop as well,
                        # in order stay up to date with the current time, with
                        # as much accuracy as possible;
                        now = datetime.now()
            
                        # Create an if statement inside of the while loop that will compare 
                        # the now variable to the alarm_time2 datetime object; 
                        # if the now variable matches or exceeds the
                        # alarm_time, then the nested snooze_alarm function 
                        # will be called;
                        if now >= alarm_time2:
                            
######################### DEFINE SNOOZE_ALARM NESTED FUNCTION

                            # Define a nested function, snooze_alarm, that will
                            # ring after the snooze period of 10 minutes, 
                            # and then prompt the user as to whether they
                            # want to hit snooze again; it then continues the
                            # loop or breaks from it based on the user input;
                            # we use Union notation as in the last function;
                            def snooze_alarm(
                                n: int, 
                                alarm_time: str, 
                            ) -> None:
                                
                                # Define a new variable, n_times_10, which
                                # will store the value of n * 10, which
                                # represents the number of times the user has
                                # hit snooze multiplied by ten minutes for
                                # each of those times;
                                n_times_10 = (n * 10)
                                
                                # We then use this new variable to print out
                                # how many total minutes have passed since the
                                # original alarm_time;
                                print(f"Ring! It's {n_times_10} minutes past {alarm_time}!")
                                print()

############################ CALL THE SNOOZE_ALARM NESTED FUNCTION
                            
                            # The snooze_alarm will ring if the above if 
                            # statement is true;
                            snooze_alarm(n, alarm_time)
                    
############################ EXIT SNOOZE_ALARM OR FINISH RUNNING SET_SNOOZE ?

                            # This part of the program had to be separated
                            # from snooze_alarm as it was causing issues for
                            # it to be included; we can either go back into
                            # the snooze loop or move on with the rest of the
                            # set_alarm function based on user input;
                            print("Do you want to hit snooze again? [Y/N]")
                            print()
                            
                            # Again, we use lower() so it won't matter if user
                            # types in upper or lower case;
                            snooze_again = input().lower()
                            print()

                            # If user hits snooze again...
                            if snooze_again == 'y':
                                # snooze counter increases by one;
                                n += 1
                                # Add 10 minutes to alarm_time2, the datetime
                                # object;
                                alarm_time2 += timedelta(minutes=10)
                                # Continue to next iteration of snooze loop;
                                continue
                            
                            # If user does not hit snooze again...
                            elif snooze_again == 'n':
                                # Don't do anything, move onto the next part 
                                # of the program;
                                pass
                           
                           # Else statement is there in case user types in
                            # something other than Y or N into snooze prompt;
                            else:
                                print("Invalid input, snooze will not be\n"
                                        "enabled.")
                                pass
                            
############################ IF ALARM_TIME2 HAS NOT ARRIVED YET...

                        # This else-if statement is here to get the loop to 
                        # reiterate up until the correct time; if it is before
                        # the specified time, now will always be less than 
                        # alarm_time2;
                        elif now < alarm_time2:
                            # We use sleep to wait .5 seconds before each loop
                            # reiteration, to help conserve system resources;
                            sleep(.5)
                            continue

############################ CALL THE SET_SNOOZE FUNCTION
                
                # The variable result does not actually get used, but I didn't
                # want to remove anything it case it might break something;
                # set_snooze gets called nonetheless;
                result = set_snooze(n, alarm_time2, snooze_again)

############################ BACK TO FIRST SNOOZE PROMPT

            # Else, if user does not want to hit snooze...
            elif snooze == 'n':
                # don't do anything, just move on with the program;
                pass
            # This else statement will catch invalid input, e.g. 'maybe';
            else:
                print("Invalid input, snooze will not be enabled.")
                print()
                pass

############################# TOMORROW BLOCK of SET_ALARM LOOP

            # Ask the user whether they want the alarm to go off again at the 
            # same time tomorrow; 
            print("Do you want this alarm to go off at the same time tomorrow?\n" 
                    "Please note it will go off at your original alarm time,\n"
                    "rather than the time the last snooze alarm went off.\n" 
                    "[Y/N]")
            print()
            # Input can be Y or N; we use lower() so that it won't 
            # matter if they type in upper or lower case;            
            tomorrow = input().lower()
            print()

            # If user wants alarm to ring tomorrow...
            if tomorrow == 'y':
                
                # We first have to readjust the minutes in the alarm_time2 
                # in the case that we changed them during the process of
                # using the snooze feature; if the user did NOT hit snooze,
                # this will not do anything as n == 0 in that case;
                alarm_time2 -= timedelta(minutes=(n*10))
                
                # Then we use the timedelta method to add 1 day to the 
                # alarm_time2 object, in which we previously stored the current
                # month and day; this will make the alarm go off at the
                # specified time tomorrow instead of today;
                alarm_time2 += timedelta(days=1)
                
                # Continue to next iteration of the set_alarm loop, this time 
                # with the date of the alarm_time2 set to tomorrow;
                continue
            
            # If user doesn't want alarm to ring tomorrow, we use break to 
            # exit the set_alarm loop;
            elif tomorrow == 'n':
                break
            
            # We use this else statement in the case of invalid input to the 
            # tomorrow prompt, e.g. 'maybe'; the user would then need to rerun
            # the program from the start if they want to set an alarm again;
            else:
                print("Invalid input, please rerun the program to set a new\n" 
                        "alarm.")
                print()
                break

#################### LAST PART OF SET_ALARM LOOP, SLEEP

        # Finally, insert sleep() method to add a half-second pause between
        # loop iterations, this helps conserve system resources;
        sleep(.5)

#################### DELAY ALARM FUNCTION

# This function will be used to delay the alarm, in the case that the 
# alarm_time (user input) has already passed or is right now; 
# the alarm will be delayed until tomorrow at the same time;
def delay_alarm(alarm_time2):
    # We use the timedelta method to add 1 day to the alarm_time2 object,
    # the alarm gets rescheduled for tomorrow;
    alarm_time2 += timedelta(days=1)
    # Call the set_alarm function with the new alarm_time2 object;
    set_alarm(alarm_time2)

#################### AM TIME CONVERSION FUNCTION

# This function will cover AM time conversion, which only applies during the
# 12:xxAM times;
def am_time_conversion(alarm_time):

    # Cast original alarm_time string as list so we can replace first two 
    # digits;
    alarm_time_list = list(alarm_time)
    # Pop the 'M' from the end of the list;
    alarm_time_list.pop(6)
    # Pop the 'A' from the list;
    alarm_time_list.pop(5)
    # Replace first two characters in list (first two digits) with new 
    # military time format;
    alarm_time_list[0:2] = ['0','0']
    # Join list back into a string we can pass the alarm_time argument to the 
    # set_alarm function;
    alarm_time = (''.join(alarm_time_list))

    # Finally, we nest the time_conversion function inside of
    # this one, as we still need to convert the alarm_time string into a
    # datetime object, i.e. alarm_time2;
    alarm_time2 = time_conversion(alarm_time)
    # We return alarm_time2 so that other functions can receive the new value;
    return alarm_time2

#################### PM TIME CONVERSION FUNCTION

# This function will be used to convert any PM time inputs---OTHER THAN 12:xxPM
# times---into 24-hour format as Python does not understand AM/PM format; 
# all we need is the alarm_time, which is entered by the user;
def pm_time_conversion(alarm_time):
    
    # Cast first two digits in alarm time as integers so we can exclude 12:xxPM
    # times from the conversion; also we will need to cast the first two digits
    # as integers in order to convert the alarm_time into a datetime object;
    HH = int((alarm_time[0:2]))
    
    # Add 12 as that is the difference between PM and military times;
    HH += 12
    
    # Recast first two digits as string so we can reinsert into original 
    # alarm_time string;
    HH = str(HH)
    
    # Create a variable, alarm_time_list, which will hold the new list we are
    # creating from the alarm_time string; then cast alarm_time string as list
    # so we can replace first two digits using list manipulation, then assign
    # it to the new variable;
    alarm_time_list = list(alarm_time)
    
    # Replace first two characters in list (first two digits) with new 
    # military time format digits;
    alarm_time_list[0:2] = HH
    
    # Pop the 'M' from the end of the list;
    alarm_time_list.pop(6)
    
    # Pop the 'P' from the end of the list;
    alarm_time_list.pop(5)
    
    # Join list back into a string we can pass the alarm_time argument to the 
    # time_conversion function in the next step;
    alarm_time = (''.join(alarm_time_list))
    
    # Finally, we nest the time_conversion function inside of
    # this one, as we still need to convert the alarm_time string into a
    # datetime object, i.e. alarm_time2;
    alarm_time2 = time_conversion(alarm_time)
    
    # Return alarm_time2 so other functions can interact with the new value;
    return alarm_time2

##################### SET OR DELAY FUNCTION

# Define a function, set_or_delay, which will be used to decide whether
# the alarm should be delayed until tomorrow (in the case that the alarm_time
# has already passed for today's date) or whether the set_alarm function
# should run normally;
def set_or_delay(alarm_time2):
    
    # Create a local variable, now, that will store the value of datetime.now()
    # for comparison to alarm_time2;
    now = datetime.now()
    
    # This if statement will apply if alarm_time2 is in the past or present; 
    if alarm_time2 <= now:
        print("You've entered a time that has already passed for today's date.\n"
                "The alarm will ring at the specified time tomorrow.")
        print()
        
        # The function delay_alarm will run, which simply delays the alarm to the 
        # same time tomorrow;
        delay_alarm(alarm_time2)
    
    # This if statement will apply if the alarm_time is in the future, 
    # ergo the set_alarm function will run normally;
    elif alarm_time2 > now: 
        # Call the set_alarm function;
        set_alarm(alarm_time2)

##################### AM IF STATEMENT

# This if statement will cover AM times, the if statement is there to ensure 
# the format for the alarm time entered is correct;
if len(alarm_time) == 7 and 'AM' in alarm_time:
    
    # First two digits, cast as integers, will be assigned to the variable HH;
    HH = int(alarm_time[0:2])
    
    # 12:xx AM times are the only times that need to be run through the 
    # specialized AM time conversion function;
    if alarm_time[0:2] == '12':
        alarm_time2 = am_time_conversion(alarm_time)
   
    # All other valid AM times can be handled with standard time conversion
    # function;
    elif HH < 12 and HH >= 1: 
        # Run the time_conversion function to convert the alarm_time into a 
        # datetime object, which then gets assigned to the global variable 
        # alarm_time2;
        alarm_time2 = time_conversion(alarm_time)

    else:
        print("This is an invalid time format, please rerun the program from\n"
                "the start.")
        print()

    # Call the function, set_or_delay, which will decide whether to set or 
    # delay the alarm based on the alarm_time2;
    set_or_delay(alarm_time2)

##################### PM IF STATEMENT

# This else-if statement will cover PM times;
elif len(alarm_time) == 7 and 'PM' in alarm_time:
    # We make an exception for 12:xx PM times as those are the only ones that
    # do NOT need to be converted, i.e. the military time is the same; 
    # all other PM times DO need to be converted; we determine this based on
    # the first two digits of the alarm_time string;
    if alarm_time[0:2] != '12':
        
        # Call PM time conversion function to convert alarm_time into military 
        # format; the standard time_conversion function is also nested
        # inside of pm_time_conversion, so that the converted PM alarm_time can be
        # converted into the datetime object, alarm_time2;
        alarm_time2 = pm_time_conversion(alarm_time)
    
    # 12:xx PM times do NOT need to be converted to military format, so we run
    # the standard time_conversion function; we determine this based on the
    # first two digits of the alarm_time string;
    elif alarm_time[0:2] == '12':
        alarm_time2 = time_conversion(alarm_time)
   
    # This else statement is there to catch possible invalid alarm_time inputs
    # that still contain 7 characters and 'PM' in the string, e.g. '25:30PM';
    else:
        print("Invalid time format, please rerun the program from the start.")
        print()

    # Call the function, set_or_delay, which will decide whether to set or 
    # delay the alarm based on the alarm_time2;
    set_or_delay(alarm_time2)

################## MILITARY IF STATEMENT

# This else-if statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:
    # Run the time_conversion function to convert the alarm_time string into a
    # datetime object, assigned to the variable alarm_time2;
    alarm_time2 = time_conversion(alarm_time)

    # Call the function, set_or_delay, which will decide what to do based
    # on the alarm_time2;
    set_or_delay(alarm_time2)

################## FINAL ELSE STATEMENT FOR INVALID TIME INPUT

# This else statement will run when an invalid time format is entered, 
# e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and\n" 
            "enter a valid time format per the instructions.")
    print()
