my_list = ["one", "two", "three", "four"]

# Open a text file
with open("test.txt", "w") as text_file:
    # Use writelines() to write the list into the file
    text_file.writelines('\n'.join(my_list))

# Open the file again in read (r) mode
with open('test.txt', 'r') as text_file:
    # Use readlines() to print the file contents
    file_contents = text_file.readlines()
    for line in file_contents:
        print(line.strip())  # Strip to remove newline characters
 
