# Set up variables
location = ["HOME"]
folders = {}

# Open File
file = open("Day 7\input.txt", "r")
input = file.read()

# Create a List of the file entries
list = input.split("\n")

# Close the file
file.close()

for ele in list:
    test = ele.split()
    # print(test)
    if (test[0] == "$") and (test[1] == "cd"):
        if test[2] == "..":
            #move location back one level
            location.pop()
            # print(location)
        elif test[2] != "/":
            #append location
            location.append(test[2])
            # print(location)
    elif test[0].isdigit():
        # Need to add file size not only to current location but all locations in path
        # print("size")
        path = ""
        for loc in location:
            path = path + "/" + loc
            if not path in folders:
                folders[path] = 0
            folders[path] = folders[path] + int(test[0])
            
total = 0
for folder_size in folders.values():
    if folder_size <= 100000:
        total = total + folder_size

print(total)