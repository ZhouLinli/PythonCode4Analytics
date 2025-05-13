import json

#---save txt---
# with open('/Users/linlizhou/Downloads/lasellchatgptexport/conversations.json', 'r') as file:

#     data = json.load(file)        
#     text_data = json.dumps(data, indent=4) # indent for pretty printing
#     print(text_data)

#     # To save to a text file
# with open('/Users/linlizhou/Downloads/lasellchatgptexport/output.txt', 'w') as outfile:
#     outfile.write(text_data)
    
    
    
#----------view indexed conversation data------

import json

def extract_chatgpt_data(file_path):
    """
    Extracts and prints conversation data from a ChatGPT export JSON file.

    Args:
        file_path (str): The path to the conversations.json file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None

# Example usage:
file_path = '/Users/linlizhou/Downloads/chatgptexport/conversations.json'  # Replace with your file path
conversation_data = extract_chatgpt_data(file_path)
conversation_data

# if conversation_data:
#     # Process the extracted data (example: print the first conversation)
#     print(conversation_data[0])
        
#use the parsed data
conversation_data[0]#["content"][0]["content"]
        
#------------------extract parts----------

parts_content = []

def extract_parts(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'parts' and isinstance(value, list):
                parts_content.extend(value)
            else:
                extract_parts(value)
    elif isinstance(data, list):
        for item in data:
            extract_parts(item)

extract_parts(conversation_data[0])

for content in parts_content:
    print(content)
    #option 1: just copy this cell output
    
    #option 2: save the following cell output that is one line
    
# Initialize an empty string to store the content
all_content = ""
for content in parts_content:
    all_content += content + "\n"  # Append content with newline for readability

all_content

#autosave into a file
# Specify the filename
filename = "extracted_content.txt"

# Open the file in write mode ('w')
with open(filename, 'w', encoding='utf-8') as file:
    # Write the combined content to the file
    file.write(all_content)

print(f"Extracted content has been saved to {filename}")