# 13.1: Write the current date to the text file today.txt

import datetime

# Get the current date
current_date = datetime.date.today()

# Open the file in write mode
with open("today.txt", "w") as file:
    # Write the current date to the file
    file.write(str(current_date))