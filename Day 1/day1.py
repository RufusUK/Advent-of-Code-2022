file = open("c:/Users/Ruth/OneDrive/Code/Advent of Code 2022/Day 1/input.txt", "r")
calories = []
x = 0

# reading the file
input = file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
list = input.split("\n")
# print(list)
file.close()

for ele in list:
    if ele == '':
        calories.append(x)
        x = 0
    else:
        x = x + int(ele)
calories.append(x)
maxcal = max(calories)
maxelf = calories.index(maxcal)
print("Part 1 solution: Elf number ", maxelf+1, " is carrying ", maxcal, " calories")
calories.sort(reverse=True)
print("Part 2 solution: ",sum(calories[0:3]))