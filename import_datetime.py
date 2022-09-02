import datetime

print(f'datetime.datetime.min   :   {datetime.datetime.min}')
print(f'datetime.datetime.max   :   {datetime.datetime.max}')
print("------------------------------------------------------------------------")

today = datetime.datetime.now()
print(f'today               :   {today}')
print(f'today.now()         :   {today.now()}')
print(f'today.date()        :   {today.date()}')
print(f'today.year          :   {today.year}')
print(f'today.month         :   {today.month}')
print(f'today.day           :   {today.day}')
print(f'today.weekday()     :   {today.weekday()}')
print(f'today.hour          :   {today.hour}')
print(f'today.minute        :   {today.minute}')
print(f'today.second        :   {today.second}')
print(f'today.microsecond   :   {today.microsecond}')
# print(dir(today))
print("------------------------------------------------------------------------")

dt = datetime.datetime(2021, 12, 31, 23, 59, 0)
print(dt)
print(f'dt                  :   {dt}')
print(f'dt.now()            :   {dt.now()}')
print(f'dt.date()           :   {dt.date()}')
print(f'dt.year             :   {dt.year}')
print(f'dt.month            :   {dt.month}')
print(f'dt.day              :   {dt.day}')
print(f'dt.weekday()        :   {dt.weekday()}')
print(f'dt.hour             :   {dt.hour}')
print(f'dt.minute           :   {dt.minute}')
print(f'dt.second           :   {dt.second}')
print(f'dt.microsecond      :   {dt.microsecond}')
print("------------------------------------------------------------------------")

# # The strftime() Method, format codes #
print("Hour (00-23)         => ", dt.strftime("%H"))
print("Minute (00-59)       => ", dt.strftime("%M"))
print("Second (00-59)       => ", dt.strftime("%S"))

print("Hour (01-12)         => ", dt.strftime("%I"))
print("AM/PM                => ", dt.strftime("%p"))

print("Weekday              => ", dt.strftime("%a"))  # Weekday, short version
print("Weekday              => ", dt.strftime("%A"))  # Weekday, full version

print("Day of Month         => ", dt.strftime("%d"))  # Day of month 01-31
print("Date                 => ", dt.strftime("%D"))  # MM/DD/YY

print("Month(number 1-12)   => ", dt.strftime("%m"))  # Month as a number 01-12

print("Month-name(short)    => ", dt.strftime("%b"))  # Month name, short version
print("Month-name(long)     => ", dt.strftime("%B"))  # Month name, full version

print("Year(short)          => ", dt.strftime("%y"))  # Year, short version, without century
print("Year(long)           => ", dt.strftime("%Y"))  # Year, full version

print("date (local version) => ", dt.strftime("%x")) # Local version of date
print("time (local version) => ", dt.strftime("%X")) # Local version of time

print(dt.strftime("%%"))

print(dt.strftime("%H:%M:%S %A, %d %b, %Y"))
print("------------------------------------------------------------------------")

# # creating date objects #
# print(datetime.datetime(2021)) # TypeError: function missing required argument 'month' (pos 2)
# print(datetime.datetime(2021, 7)) # TypeError: function missing required argument 'day' (pos 3)
print(datetime.datetime(2021, 7, 23))
print(datetime.datetime(2021, 7, 23, 12))
print(datetime.datetime(2021, 7, 23, 12, 56))
print(datetime.datetime(2021, 7, 23, 12, 56, 59))
print(datetime.datetime(2021, 7, 23, 12, 56, 59, 456041))
print("------------------------------------------------------------------------")

# # Difference between two dates #
print(dt - today)
print(today - dt)