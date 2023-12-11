import json

# Open your text file and a new JSONL file
with open('TD.txt', 'r') as txt_file, open('output.jsonl', 'w') as jsonl_file:
    # Read each line in the text file
    for line in txt_file:
        # Create a dictionary with the structure you want
        data = {"sentence": line.strip()}
        
        # Write this dictionary as a JSON object to the JSONL file
        jsonl_file.write(json.dumps(data) + '\n')
