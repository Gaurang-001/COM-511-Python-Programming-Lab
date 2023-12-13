# Get user input for three lines
lines = []
for i in range(3):
    line = input(f"Enter line {i+1}: ")
    lines.append(line)

# Write the lines to a text file
with open("MyFile.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
