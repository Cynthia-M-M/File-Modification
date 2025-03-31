import os
 
# Putting a loop until a valid filename is provided
while True:
    # To ask user for filename to read from
    filename = input("Please enter the filename you want to read from: ")
    # To check if the file exists
    if os.path.exists(filename): 
        try:
            # To read from an existing file and modify it's content
            with open(filename, "r") as file: 
                content = file.read()
            if not content:
                print(f"The file '{filename}' is empty.")
            else:
                print(f"The content of the file '{filename}' is:")
                print(content)
                # Modification of content
                modified_content = content.replace("Jane", "Mary") 
                print(f"modified content:")
                print(modified_content)
            # If the file is found and modified,break the loop 
            break
        except PermissionError:
            print(f"Ooops! Permission denied to read or write the file '{filename}'.Please try again.")
        except Exception as e:
            print(f"An error occured:{e}") 
    else:
        print(f"Ooops! The file '{filename}' does not exist.Please try again.") 
# To ask user for filename to write into  
output_filename = input("Please enter the filename you want to write/modify into:")
try:
    with open(output_filename, "w") as newfile:
        newfile.write(modified_content)
    print(f"The modified content has been written to '{output_filename}' successfully.")              
except Exception as e:
        print(f"An error occured while writing to '{output_filename}': {e}")        
finally:
       print("Thank you for using the file modification tool.") 

     