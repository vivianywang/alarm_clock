import time


print("When would you like your alarm to be set for?")

month = input("Month (input Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec): ")
day = input("Day: ")
timee = input("Time (HH:MM): ")

alarm_time = month + ' ' + day + ' ' + timee

while True:
    current_time = time.ctime()
    day_of_week = current_time[0:4]
    year_and_sec = current_time[len(current_time)-8:len(current_time)]
    current_time = current_time.replace(day_of_week, '')
    current_time = current_time.replace(year_and_sec, '')
    if current_time == alarm_time:
        print("alarm")
        break


