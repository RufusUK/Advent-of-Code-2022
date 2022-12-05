# Setting up variables. 
first_half = []
second_half = []
Total = 0

# Set up reference data
letters = ['',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Open File
file = open("c:/Users/Ruth/OneDrive/Code/Advent of Code 2022/Day 3/input.txt", "r")
input = file.read()

# Create a List of the file entries
list = input.split("\n")

# Close the file
file.close()

for i in range(0,len(list),3):
    for letter in range(len(list[i])):
        if list[i][letter] in list[i+1]:
            if list[i][letter] in list[i+2]:
                Total = Total + letters.index(list[i][letter])
                break
print(Total)