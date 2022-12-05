# Set up variables
count = 0

# Import libraries
import re

# Open File
file = open("Day 4\input.txt", "r")
input = file.read()

# Create a List of the file entries
list = input.split("\n")

# Close the file
file.close()

# Work through each entry in the list
for ele in list:
    # Split based on , and - characters so you end up with a list of 4 values - elf 1 start and finish, elf 2 start and finish
    values = re.split(r"[,-]",ele)
    # Now check if the start or end value for either elf is between the start and end values of the other elf. 
    # If either true, then increment count by 1.
    if (int(values[0]) >= int(values[2]) and int(values[0]) <= int(values[3])) or (int(values[2]) >= int(values[0]) and int(values[2]) <= int(values[1])) or (int(values[1]) >= int(values[2]) and int(values[1]) <= int(values[3])) or (int(values[3]) >= int(values[0]) and int(values[3]) <= int(values[1])) :
        count = count + 1

print(count)