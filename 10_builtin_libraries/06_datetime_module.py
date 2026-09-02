from datetime import date, datetime, time, timedelta, timezone

# Current date and time
today = date.today()
now = datetime.now()
print("Today's date:", today)
print("Current date and time:", now)
print("Current UTC time:", datetime.now(timezone.utc))

# Create date, time and datetime objects
training_date = date(2026, 9, 15)
start_time = time(9, 30)
start_datetime = datetime.combine(training_date, start_time)
print("Training starts:", start_datetime)

# Extract individual components
print("Year:", start_datetime.year)
print("Month:", start_datetime.month)
print("Day:", start_datetime.day)
print("Weekday number:", start_datetime.weekday())
print("Weekday name:", start_datetime.strftime("%A"))

# Format a datetime as text
print("Formatted datetime:", start_datetime.strftime("%d-%b-%Y %I:%M %p"))

# Parse text into a datetime
text_date = "25-09-2026 14:30"
parsed_date = datetime.strptime(text_date, "%d-%m-%Y %H:%M")
print("Parsed datetime:", parsed_date)

# Date arithmetic
print("Seven days later:", training_date + timedelta(days=7))
print("Two hours earlier:", start_datetime - timedelta(hours=2))
duration = parsed_date - start_datetime
print("Difference in days:", duration.days)
print("Total difference in seconds:", duration.total_seconds())

# Replace selected components
rescheduled = start_datetime.replace(hour=11, minute=0)
print("Rescheduled time:", rescheduled)
