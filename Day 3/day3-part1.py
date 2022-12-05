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

for ele in list:
    half = len(ele) // 2
    first_half = ele[:half]
    second_half = ele[half:]
    for i in range(half):
        if first_half[i] in second_half:
            Total = Total + letters.index(first_half[i])
            break

print(Total)