# 13.3: Parse the date from today_string

import datetime

# Open the file in read mode
with open("today.txt", "r") as file:
    # Read the contents of the file into the today_string variable
    today_string = file.read()

# Parse the date from the today_string
parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d").date()

# Print the parsed date
print("Parsed date:", parsed_date)