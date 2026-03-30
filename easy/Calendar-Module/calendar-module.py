import calendar

# Read input
date_input = input().strip()
month, day, year = map(int, date_input.split())

# Create a TextCalendar object (0 = Monday, 6 = Sunday)
cal = calendar.TextCalendar(calendar.SUNDAY)

# Get the weekday (0 = Monday, 6 = Sunday)
weekday = calendar.weekday(year, month, day)

# Convert to day name
day_name = calendar.day_name[weekday]

# Print in uppercase
print(day_name.upper())
