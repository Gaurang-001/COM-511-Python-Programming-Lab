# Specify the file path
file_path = r"C:\Users\ACER\OneDrive\Desktop\Python\input.txt"

# Read and print the content of the file
with open(file_path, "r") as file:
    file_content = file.read()
    print("Content of the file:")
    print(file_content)

# Extract unique words and sort them alphabetically
words = file_content.split()
unique_words = sorted(set(words))

# Print unique words
print("\nUnique words in alphabetical order:")
for word in unique_words:
    print(word)

