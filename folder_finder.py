import os
import re

# Define the special characters that might cause issues with compression
special_chars = re.compile(r'[<>:"/\\|?*\x00-\x1F+.]')


# Function to find folders with special characters in their names
def find_folders_with_special_chars(starting_path):
    folders_with_special_chars = []
    for root, dirs, files in os.walk(starting_path):
        for dir_name in dirs:
            if special_chars.search(dir_name):
                folder_path = os.path.join(root, dir_name)
                folders_with_special_chars.append(folder_path)
    return folders_with_special_chars


# Function to find all folders
def find_all_folders(starting_path):
    all_folders = []
    for root, dirs, files in os.walk(starting_path):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            all_folders.append(folder_path)
    return all_folders


# Define the starting path to search
starting_path = r"your desired path"

# Ask user for the desired operation
print("Select the operation:")
print("1. Find folders with special characters")
print("2. List all folders")
choice = input("Enter the number of your choice: ")
# Define the output file path
output_file_path = r"\your desired path\folders_with_special_chars.txt"

if choice == "1":
    # Find folders with special characters
    folders = find_folders_with_special_chars(starting_path)
    # Write the results to the output file with UTF-8 encoding
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        if folders:
            output_file.write("Folders with special characters in their names:\n")
            for folder in folders:
                output_file.write(folder + "\n")
        else:
            output_file.write("No folders with special characters found.\n")
    print(f"Results written to {output_file_path}")

elif choice == "2":
    # Find all folders
    folders = find_all_folders(starting_path)
    # Write the results to the output file with UTF-8 encoding
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        if folders:
            output_file.write("All folders:\n")
            for folder in folders:
                output_file.write(folder + "\n")
        else:
            output_file.write("No folders found.\n")
    print(f"Results written to {output_file_path}")

else:
    print("Invalid choice. Please run the script again and select a valid option.")
