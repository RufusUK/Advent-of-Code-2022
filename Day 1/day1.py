file = open("input.txt", "r")
calories = []
twocal = []
threecal = []
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
print("\nElf number ", maxelf+1, " is carrying ", maxcal, " calories")