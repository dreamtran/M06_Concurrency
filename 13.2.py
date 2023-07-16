# 13.2: Read the text file today.txt into the string today_string

import datetime

# Open the file in read mode
with open("today.txt", "r") as file:
    # Read the contents of the file into the today_string variable
    today_string = file.read()