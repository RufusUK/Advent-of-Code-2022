# Set up variables
window = []
character = 14

# Open data file
file = open("Day 6\input.txt", "r")
input = file.read()

# Close the file
file.close()


# Create initial block of 4 characters to test
for i in range(0,14):
    window.append(input[i])


# Loop through input string until 14 unique characters are in the block of 14
while len(set(window)) != 14:
    character = character +1
    window.pop(0)
    window.append(input[character-1])
print(character)


# Report the character number