# Import date
from datetime import date, datetime

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)


hurricane_andrew = date(1992, 8, 24)

print(hurricane_andrew.weekday())


# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month

  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime("%Y-%m"))

# Create a date object
andrews = date(1992, 8, 26)

# Print the date in the format 'MONTH (YYYY)'
print(andrews.strftime("%B (%Y)"))


john = date(1992, 8, 26)

# Print the date in the format 'YYYY-DDD'
print(john.strftime("%Y-%d"))


zoe = date(1992, 8, 26)

# Print the date in the format 'YYYY-DDD' %j days in a year how astronant
print(zoe.strftime("%Y-%j"))


# Create a datetime object
dt = datetime(2007, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())


dts = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dts_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print(dts_old.isoformat())


# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts["AM"] += 1
  else:
    # Increment the counter for after noon
    trip_counts["PM"] += 1
  
print(trip_counts)