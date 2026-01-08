# open the text file in read mode
with open(r'/content/text_file/example.txt', 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Print the contents of the file
print(file_contents)