import re
import sys


def main():
    print(convert(input("Hours:")))

def convert(s):
    match = re.search(r"^(\d{1,2})(?::([0-5][0-9]))? (AM|PM) to (\d{1,2})(?::([0-5][0-9]))? (AM|PM)$",s)
    if not match:
        raise ValueError("Invalid")
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()
    time1 = convert_time(hour1,minute1,period1)
    time2 = convert_time(hour2,minute2,period2)
    return f"{time1} to {time2}"

def convert_time(hour_str,minute_str,period):
    hour = int(hour_str)
    minute= int(minute_str) if minute_str else 0 

    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")
    
    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute")
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()