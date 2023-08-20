def convert24(hour, minute, period):
    if period == "am":   
        # period is set to am and pm 
        # It checks if the condition is am 
        if hour == 12:  
            # condition checks if the hour is 12
            # The hour is 12 and its set to 0 therefore if the hour is not 12 it is unchanged  
            hour = 0
            # If all conditions are met it will result to 12:00 AM
            # the code sets hour to 0 to convert it to 24 hr representation
    else:
        # Indicates if the period is now PM 
        if hour != 12:
            # checks if the input hour is not equal to 12
            hour += 12
            # if the hour is not 12 meaning its either from 1 to 11 , to convert this you just need to add 12 to it 
            
    return "{:02d}{:02d}".format(hour, minute)
#  its responsible for formatting the hour and the minutes into four digits 
# {:02d} specifies a character with two decimal places 
# the hour and minute are paced as arguments in the format so the values are the ones to be passed there

print(convert24(8 , 26 , "pm"))




def convert24(str1):
     if str1[-2:] == "AM" and str1[:2] == "12":
         return "00" + str1[2:-2]
     
     elif str1[-2:] == "AM":
         return str1[:-2]
     
     elif str1[-2:] == "PM" and str1[:2] == "12":
         return str1[:-2]
     
     else:
         return str(int(str1[:2]) + 12) + str1[2:-2]