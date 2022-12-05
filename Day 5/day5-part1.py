# Set up variables
Crates = {}
toplist = ''

# Import libraries

# Open File
file = open("Day 5\input.txt", "r")
input = file.read()

# Create a List of the file entries
list = input.split("\n")

# Close the file
file.close()

# Find location of blank line
blank = list.index('')

#Initialise the crates - work upwards from the blank line to populate the initial position
for i in range(len(list[blank-1].split())):
    Crates[i+1] = []
    for ele in range(blank-2,-1,-1):
        if list[ele][1 + (i * 4)] != ' ':
            Crates[i+1].append(list[ele][1 + (i * 4)])

#Now undertake the moves
for ele in range(blank+1,len(list)):
    instruction=list[ele].split()
    for i in range(int(instruction[1])):
        temp = Crates[int(instruction[5])].append(Crates[int(instruction[3])].pop())

# Now we need the top crate from each stack, which will be the last entry in the list

for ele in Crates:
    toplist = toplist + Crates[ele][-1]

print(toplist)
    