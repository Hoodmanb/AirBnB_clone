import sys

# Print out all directories in sys.path
print(sys.path)

# Check if a specific directory is in sys.path
directory_to_check = "/path/to/your/directory"
if directory_to_check in sys.path:
    print("The directory is in sys.path")
else:
    print("The directory is not in sys.path")
