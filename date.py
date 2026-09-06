# Import date
from datetime import date

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

# Print the date in the format 'YYYY-DDD'
print(zoe.strftime("%Y-%j"))