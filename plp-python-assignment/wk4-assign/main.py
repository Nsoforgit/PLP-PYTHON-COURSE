def process_file():
    while True:
        filename = input("Enter the filename to read: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\nOriginal content:\n{content}")
                
                # Modify content (in this case, uppercase it)
                modified = content.upper()
                
                # Write modified content to a new file
                output_filename = f"modified_{filename}"
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified)
                    
                print(f"\nModified content has been written to {output_filename}")
                break
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: No permission to access '{filename}'. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    process_file()