# File Handling and Exception Handling Assignment

## Implementation
try:
    # Step 1: Create and write to input.txt
    with open("input.txt", "w") as file:
        file.write("Python is an amazing language.\n")
        file.write("It is widely used for web development, data science, and automation.\n")
        file.write("File handling in Python is simple and powerful.\n")
        file.write("You can read, write, and modify files easily.\n")
        file.write("This script demonstrates text processing in Python.\n")
    
    # Step 2: Read input.txt and process the text
    with open("input.txt", "r") as file:
        content = file.read()
        word_count = len(content.split())  # Count the number of words
        uppercase_content = content.upper()  # Convert text to uppercase
    
    # Step 3: Write processed text and word count to output.txt
    with open("output.txt", "w") as file:
        file.write(uppercase_content + "\n")
        file.write(f"Word Count: {word_count}\n")
    
    # Step 4: Print success message
    print("Processing complete! 'output.txt' has been created.")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
