# Initialise Variables
score_total = 0

# Create reference dictionary for lookups
scoring = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7
}

# Open File
file = open("c:/Users/Ruth/OneDrive/Code/Advent of Code 2022/Day 2/input.txt", "r")
input = file.read()

# Create a List of the file entries
list = input.split("\n")

# Close the file
file.close()

#Loop through the list, matchiing to our score dictionary and incrementing the score variable
for ele in list:
    try:
        score_total = score_total + scoring[ele]
# It's throwing an error because the final element is '' and I can't be bothered to figure out how to either handle that or clean up the input file!
    except KeyError:
        pass

print("The final score is ", score_total)