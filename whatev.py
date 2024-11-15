import os
import time

os.system('netstat -ano -> stats.text')

# Define the file name
file_name = "stats.txt"

try:
    # Open the file and process each line
    with open(file_name, "r") as file:
        # Extract the last 7 characters of each line
        last_7_chars_list = [line[-7:].strip() for line in file]

    # Print the result
    print("Last 7 characters of each line:")
    for i, chars in enumerate(last_7_chars_list, 1):
        print(f"Line {i}: {chars}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


