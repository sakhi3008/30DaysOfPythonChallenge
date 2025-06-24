# Challenge - Calculate the days between two dates
from datetime import datetime

# Step 1: Input two dates in the format YYYY-MM-DD
date1_str = input("Enter the first date (DD-MM-YYYY): ")
date2_str = input("Enter the second date (DD-MM-YYYY): ")

# Step 2: Convert string to datetime object
date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

# Step 3: Calculate the difference
difference = abs((date2 - date1).days)

# Step 4: Display result
print(f"The number of days between {date1_str} and {date2_str} is {difference} days.")
