# Set up variables
window = []
character = 4

# Open data file
file = open("Day 6\input.txt", "r")
input = file.read()

# Close the file
file.close()


# Create initial block of 4 characters to test
for i in range(0,4):
    window.append(input[i])


# Loop through input string until 4 unique characters are in the block of 4
while len(set(window)) != 4:
    character = character +1
    window.pop(0)
    window.append(input[character-1])
print(character)


# Report the character number