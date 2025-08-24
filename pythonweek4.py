# File Read & Write Challenge 🖋️:
# This program asks the user for a filename, reads its contents,
# converts the text to uppercase, and writes it to a new file called 'modified_<originalfilename>'.
# Error Handling Lab 🧪:
# The program handles errors if the file doesn't exist or can't be read.

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        content = infile.read()
        print("Original file content read successfully.")

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Prepare new filename
    new_filename = f"modified_{filename}"

    with open(new_filename, 'w') as outfile:
        outfile.write(modified_content)
        print(f"Modified content written to {new_filename}.")

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read or written.")