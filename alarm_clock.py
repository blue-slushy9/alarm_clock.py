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

alarm_time = input().upper()
print()

############### TIME CONVERSION MILITARY

# This function will convert military alarm_time user inputs into a
# datetime object, to be stored in the global variable alarm_time2;
# Note that separate functions will have to be defined for AM and PM times;
def time_conversion(alarm_time):
    # Create a variable HH that will store the hours portion of the alarm time
    # as an integer;
    HH = int((alarm_time[0:2]))

    # Create a variable MM that will store the minutes portion of the alarm 
    # time as an integer; We skip over alarm_list[2] because that is the ':' ;
    MM = int((alarm_time[3:5]))

    # Create an alarm_time2 variable that will store the current 
    # datetime, then we use the replace() function to overwrite the hour and 
    # minutes with our target time (the alarm time per user input); 
    # using datetime ensures that the alarm will go off on the correct day, 
    # either today or tomorrow if the time has already passed today;
    alarm_time2 = datetime.now().replace(hour=HH, minute=MM)

    # Add a return statement so that other functions can receive alarm_time2;
    return alarm_time2

#alarm_time2 = time_conversion(alarm_time)

################ RUN TIME CONVERSION, GET ALARM_TIME2

# Run time conversion function as alarm_time2 will be used for most subsequent
# functions;
#time_conversion(alarm_time)

# Define alarm_time2 variable at the top, as it will be used in all of the 
# subsequent functions;
#alarm_time2 = datetime.now()#.replace(hour=HH, minute=MM)

############### ALARM FUNCTION

# Define the alarm function, which will run at the time specified in the input;
def alarm():
    print(f"Ring! It's {alarm_time}, time to wake up!")

############### SET ALARM BLOCK 

# This function will be used to set the alarm, it takes the datetime object as
# its argument;

alarm_time2 = time_conversion(alarm_time)
def set_alarm(alarm_time2):

    # Create a while loop that will constantly check the datetime.now, 
    # then assign it to the variable now; 
    while True:
        now = datetime.now()
    
        # Create an if statement inside of the while loop that will compare 
        # the now variable to the alarm_time2 datetime object; 
        # if the now variable matches or exceeds the alarm_time....
        if now >= alarm_time2:
            # then the alarm function will run, i.e. the alarm will ring!           
            alarm()
            # Print a new line to improve legibility in terminal;
            print()

############################ SNOOZE BLOCK

            # Ask the user whether they would like to hit snooze;
            print("Would you like to hit snooze? [Y/N]")
            print()
            # Input can be Y or N; we use lower() so that it won't 
            # matter if they type in upper or lower case;            
            snooze = input().lower()
            print()
            
            # If the user says yes to the first snooze...
            if snooze == 'y':
                # Set the global variable snooze counter, n, equal to 1;
                #global n 
                #n = 1
                # Add 1 to the n counter, which we will use in the
                # snooze_alarm function below;
                # we add 10 minutes to alarm_time2, i.e. the alarm will go off
                # again in 10 minutes;
                alarm_time2 += timedelta(minutes=10)

################# SET_SNOOZE FUNCTION
                
                # Create variable, n, which will be the snooze counter;
                n = 1
                #print(n) -- yes
                # Create snooze_again variable and set it equal to 'y' to
                # start;
                snooze_again = 'y'
                #print(snooze_again) -- yes
                # Define a function, set_snooze, that will be the snooze
                # version of set_alarm;

                # Union is used to specify that the function will return more
                # than one type of value;
                from typing import Union
                def set_snooze(
                    n: int,
                    alarm_time2: object,
                    snooze_again: str
                ) -> Union[int, object, str]:

                    #n = 1
                    # Create snooze_again variable and set it equal to 'y' to
                    # start;
                    #snooze_again = 'y'
                    # Create while loop that will run for as long as 
                    # snooze_again == 'y';

                    #print(snooze_again)
                    while snooze_again == 'y':
                        now = datetime.now()
            
                        # Create an if statement inside of the while loop that will compare 
                        # the now variable to the alarm_time2 datetime object; 
                        # if the now variable matches or exceeds the alarm_time....
                        #print(snooze_again)
                        #print(n)
                        #print(now)
                        #print(alarm_time2)
                        if now >= alarm_time2:
                            
################# SNOOZE ALARM NESTED FUNCTION

                            # Define a nested function, snooze_alarm, that will
                            # ring and then prompt the user as to whether they
                            # want to hit snooze again; it then continues the
                            # loop or breaks from it based on the input;
                            def snooze_alarm(
                                n: int,
                                alarm_time: str,
                                #snooze_again: str
                            ) -> None:
                                n_times_10 = (n * 10)
                                print(f"Ring! It's {n_times_10} minutes past {alarm_time}!")
                                print()

############################ CALL THE SNOOZE_ALARM FUNCTION;

                            snooze_alarm(n, alarm_time)
                            
                            # Run the rest of the SET_SNOOZE FUNCTION;
                            print("Do you want to hit snooze again? [Y/N]")
                            print()
                            snooze_again = input().lower()
                            print()

                            if snooze_again == 'y':
                                n += 1
                                alarm_time2 += timedelta(minutes=10)
                                #continue
                            elif snooze_again == 'n':
                                pass
                                #break
                            else:
                                print("Invalid input, snooze will not be\n"
                                        "enabled.")
                                pass
                            
                            return [n, alarm_time2, snooze_again]
                            
                            #result = snooze_alarm(n, alarm_time2, snooze_again)
                            #print(result)
                            #n = int(result[0])
                            #alarm_time2 = result[1]
                            #snooze_again = result[2]

                            #print(n)
                            #print(alarm_time2)
                            #print(snooze_again)

############################ CALL THE SNOOZE_ALARM FUNCTION

                            # then the alarm function will run, i.e. the alarm will ring!           
                            #snooze_alarm(n, alarm_time2, snooze_again)
                            # Print a new line to improve legibility in terminal;
                            print()
                        
                        elif now < alarm_time2:
                            sleep(.5)
                            continue

                        #yield [n, alarm_time2, snooze_again]
                        
                #    result = set_snooze(n, alarm_time2, snooze_again)

                #    n = int(result[0])
                #    alarm_time2 = result[1]
                #    snooze_again = result[2]

                #     print(n)
                #     print(alarm_time2)
                #     print(snooze_again)

#################### CALL THE SET_SNOOZE FUNCTION;
                
                result = set_snooze(n, alarm_time2, snooze_again)

                # Create while True loop that will go for as long as user
                # keeps hitting snooze (we will use break to exit);
                #while True:
                    #if snooze_again == 'y':

            # Create a counter, n, that will keep track of how many times
            # the user has hit snooze, in order to pass the value to the
            # alarm_time2 and include it in alarm() output;
            #n == 0
            # If user wants to hit snooze...
            #while snooze == 'y':
                # Create a counter, n, that will keep track of how many times
                # the user has hit snooze, in order to pass the value to the
                # alarm_time2 and include it in alarm() output;
                #n == 0

                # Create while True loop that will run for as long as user
                # enables snooze;
                #while True:
                
                        # Add 1 to the n counter, which we will use in the
                        # snooze_alarm function below;
                        # we add 10 minutes to alarm_time2, i.e. the alarm will go off
                        # again in 10 minutes;
                        #alarm_time2 += timedelta(minutes=10)
               
                                            # Nest set_alarm function inside of this function;

                # Call the snooze_alarm function;
                #snooze_alarm()
                
                # Then we use continue to move onto the next iteration of the
                # while loop;
                #continue
           
            # Else, if user does not want to hit snooze...
            elif snooze == 'n':
                # don't do anything, just move on with the program;
                pass
            # This statement will catch invalid input, e.g. 'maybe';
            else:
                print("Invalid input, snooze will not be enabled.")
                print()
                pass

############################# TOMORROW BLOCK

# Ask the user whether they want the alarm to go off again at the 
            # same time tomorrow; 
            print("Do you want this alarm to go off at the same time tomorrow?\n" 
                    "Please note it will go off at your original alarm time,\n"
                    "rather than the time the snooze alarm went off. [Y/N]")
            print()
            # Input can be Y or N; we use lower() so that it won't 
            # matter if they type in upper or lower case;            
            tomorrow = input().lower()
            # Print a new line to improve legibility in terminal;
            print()

            # If user wants alarm to ring tomorrow, we use continue to skip 
            # the code below and proceed to next iteration of the while loop;
            if tomorrow == 'y':
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
            elif tomorrow == 'n':
                break
            # We use this else statement in the case of invalid input to the 
            # tomorrow prompt, e.g. 'maybe';
            # the user would then need to rerun the program from the start;
            else:
                print("Invalid input, please rerun the program to set a new\n" 
                        "alarm.")
                print()
                break

        # Finally, insert sleep() method to add a 1-second pause between loop 
        # iterations, this helps conserve system resources;
        sleep(.5)

#################### DELAY_ALARM

# This function will be used to delay the alarm, in the case that the 
# alarm_time (user input) has already passed or is right now; 
# the alarm will be delayed until tomorrow at the same time;
def delay_alarm(alarm_time2):
    alarm_time2 += timedelta(days=1)
    set_alarm(alarm_time2)

#################### AM TIME CONVERSION

# This function will cover AM time conversion, which only applies during the
# 12:xxAM times;
def am_time_conversion(alarm_time):
    #HH = int((alarm_time[0:2]))
    #if HH == 12:
    # Recast first two digits as string so we can reinsert into original 
    # alarm_time string;
    #HH = str(HH)

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
    time_conversion(alarm_time)
    
#################### PM TIME CONVERSION

# This function will be used to convert any PM time inputs---OTHER THAN 12:xxPM
# times---into 24-hour format as Python does not understand AM/PM format; 
# all we need is the alarm_time, which is entered by the user;
def pm_time_conversion(alarm_time):
    # Cast first two digits in alarm time as integers so we can exclude 12:xxPM
    # times from the conversion; also we will need to cast the first two digits
    # as integers in order to convert the alarm_time into a datetime object;
    HH = int((alarm_time[0:2]))
    #if HH < 12 and HH >= 1:
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
    
    # Finally, we nest the time_conversion function inside of
    # this one, as we still need to convert the alarm_time string into a
    # datetime object, i.e. alarm_time2;
    time_conversion(alarm_time)

##################### SET OR DELAY

# Define a function, delay_or_execute, which will be used to decide whether
# the alarm should be delayed until tomorrow (in the case that the alarm_time
# has already passed for today's date) or whether the alarm_execution function
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
        # The function alarm_delay will run, which simply delays the alarm to the 
        # same time tomorrow;
        delay_alarm(alarm_time2)
    # This if statement will apply if the alarm_time is in the future, 
    # ergo the alarm_execution function will run;
    elif alarm_time2 > now: 
        set_alarm(alarm_time2)

##################### AM IF STATEMENT

# This if statement will cover AM times, the if statement is there to ensure 
# the format for the alarm time entered is correct;
if len(alarm_time) == 7 and 'AM' in alarm_time:
    HH = int(alarm_time[0:2])
    if alarm_time[0:2] == '12':
        am_time_conversion(alarm_time)
        # This if statement covers 12:xxAM times, where we need to subtract 12;
        #if HH == 12:
        #    HH -= 12
        # Run the time_conversion function to convert the alarm_time into a 
        # datetime object, which then gets assigned to the global variable 
        # alarm_time2;
    elif HH < 12 and HH >= 1: 
        time_conversion(alarm_time)

    else:
        print("This is an invalid time format, please rerun the program from\n"
                "the start.")
        print()

    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    set_or_delay(alarm_time2)

##################### PM IF STATEMENT

# This if statement will cover PM times;
elif len(alarm_time) == 7 and 'PM' in alarm_time:
    if alarm_time[0:2] != '12':
    # Call PM time conversion function to convert alarm_time into military 
    # format; the AM and military time_conversion function is also nested
    # inside of pm_time_conversion, so that the converted PM alarm_time can be
    # converted into the datetime object, alarm_time2;
        pm_time_conversion(alarm_time)

    elif alarm_time[0:2] == '12':
        time_conversion(alarm_time)
    
    else:
        print("Invalid time format, please rerun the program from the start.")
        print()

    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    set_or_delay(alarm_time2)

################## MILITARY IF STATEMENT

# This statement will cover military time input;
elif len(alarm_time) == 5 and ':' in alarm_time:
    # Run the time_conversion function to convert the alarm_time string into a
    # datetime object, assigned to the variable alarm_time2;
    alarm_time2 = time_conversion(alarm_time)

    # Call the function, delay_or_execute, which will decide what to do based
    # on the alarm_time2;
    set_or_delay(alarm_time2)

################## FINAL ELSE STATEMENT FOR INVALID TIME INPUT

# This else statement will run when an invalid time format is entered, 
# e.g. '630AM';
else:
    print("This is an invalid time format, please run the program again and\n" 
            "enter a valid time format per the instructions.")
    print()
